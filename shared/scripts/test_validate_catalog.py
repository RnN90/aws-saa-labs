"""Testes de integridade do catálogo, sem acesso à AWS."""
import copy
import tempfile
import unittest
from pathlib import Path

from jsonschema import SchemaError, ValidationError
from validate_catalog import ROOT, load, validate_labs, validate_coverage, validate_docs


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.schema = load(ROOT / 'shared/schemas/lab-v1.schema.json')
        self.capabilities = load(ROOT / 'catalog/capabilities.json')['capabilities']
        self.certifications = load(ROOT / 'certifications/catalog.json')['certifications']
        self.entries = []
        for p in sorted((ROOT / 'labs').glob('*/lab.yaml')):
            target = self.root / p.relative_to(ROOT)
            target.parent.mkdir(parents=True)
            target.write_text(p.read_text())
            (target.parent / 'README.md').write_text('# Laboratório\n')
            lab = load(p)
            if lab['terraform']:
                tf = target.parent / lab['terraform']
                tf.mkdir()
                (tf / 'versions.tf').touch()
                (tf / '.terraform.lock.hcl').touch()
            self.entries.append((target, lab))

    def validate(self):
        return validate_labs(self.entries, self.schema, self.capabilities, {c['code'] for c in self.certifications}, self.root)

    def test_repository_catalog_and_order(self):
        labs, order = self.validate()
        self.assertEqual(len(labs), 7)
        self.assertLess(order.index('vpc-networking'), order.index('ec2-connectivity'))

    def test_invalid_schema(self):
        self.schema['type'] = 'invalid-type'
        with self.assertRaises(SchemaError): self.validate()

    def test_missing_required_field(self):
        del self.entries[0][1]['id']
        with self.assertRaises(ValidationError): self.validate()

    def test_invalid_status(self):
        self.entries[0][1]['status'] = 'running'
        with self.assertRaises(ValidationError): self.validate()

    def test_unknown_schema_version(self):
        self.entries[0][1]['schema_version'] = 2
        with self.assertRaises(ValidationError): self.validate()

    def test_duplicate_identifier(self):
        self.entries.append(copy.deepcopy(self.entries[0]))
        with self.assertRaisesRegex(ValueError, 'duplicado'): self.validate()

    def test_missing_dependency(self):
        self.entries[2][1]['dependencies'][0]['lab'] = 'unknown'
        with self.assertRaises(ValueError): self.validate()

    def test_cycle(self):
        self.entries[0][1]['dependencies'] = [{'id':'cycle','lab':'ec2-connectivity','type':'educational','scenario':None}]
        with self.assertRaisesRegex(ValueError, 'circular'): self.validate()

    def test_missing_capability(self):
        self.entries[2][1]['consumes'][0]['capability'] = 'unknown'
        with self.assertRaises(ValueError): self.validate()

    def test_wrong_contract_owner(self):
        self.entries[2][1]['dependencies'][0]['lab'] = 'identity-governance'
        with self.assertRaisesRegex(ValueError, 'incompatível'): self.validate()

    def test_contract_version(self):
        self.entries[2][1]['consumes'][0]['contract_version'] = '2'
        with self.assertRaises(ValidationError): self.validate()

    def test_duplicate_capability_owner(self):
        self.entries[0][1]['provides'].append({'capability':'network-foundation','contract_version':'1'})
        with self.assertRaises(ValueError): self.validate()

    def test_missing_optional_scenario(self):
        self.entries[4][1]['dependencies'][0]['scenario'] = None
        with self.assertRaisesRegex(ValueError, 'sem cenário'): self.validate()

    def test_missing_directory(self):
        self.entries[0][0].unlink()
        with self.assertRaisesRegex(ValueError, 'inexistente'): self.validate()

    def test_planned_terraform(self):
        self.entries[2][1]['terraform'] = 'terraform'
        with self.assertRaises(ValidationError): self.validate()

    def test_missing_readme(self):
        (self.entries[0][0].parent / 'README.md').unlink()
        with self.assertRaises(ValueError): self.validate()

    def test_unknown_certification(self):
        self.entries[0][1]['certifications'] = ['XXX-C01']
        with self.assertRaises(ValueError): self.validate()

    def test_published_without_url(self):
        self.entries[0][1]['publication']['article']['status'] = 'published'
        with self.assertRaisesRegex(ValueError, 'sem URL'): self.validate()

    def test_invalid_dependency_type(self):
        self.entries[2][1]['dependencies'][0]['type'] = 'automatic'
        with self.assertRaises(ValidationError): self.validate()

    def test_ownership_mismatch(self):
        self.entries[0][1]['ownership']['resource_owner'] = 'vpc-networking'
        with self.assertRaisesRegex(ValueError, 'Ownership'): self.validate()

    def test_duplicate_yaml_json_keys(self):
        p = self.root / 'bad.yaml'
        p.write_text('{"id":"one","id":"two"}')
        with self.assertRaisesRegex(ValueError, 'duplicada'): load(p)

    def test_broken_relative_link(self):
        p = self.root / 'README.md'
        p.write_text('[Link](missing.md)')
        with self.assertRaises(ValueError): validate_docs(self.root, [p])

    def test_escaping_link(self):
        p = self.root / 'README.md'
        p.write_text('[Link](../outside.md)')
        with self.assertRaises(ValueError): validate_docs(self.root, [p])

    def test_unclosed_diagram(self):
        p = self.root / 'README.md'
        p.write_text('```mermaid\nflowchart TD\n subgraph a["A"]\n```\n')
        with self.assertRaises(ValueError): validate_docs(self.root, [p])

    def test_unknown_sequence_participant(self):
        p = self.root / 'README.md'
        p.write_text('```mermaid\nsequenceDiagram\n participant A\n A->>Missing: Mensagem\n```\n')
        with self.assertRaises(ValueError): validate_docs(self.root, [p])

    def test_unknown_lab_in_coverage(self):
        labs, _ = self.validate()
        coverage = load(ROOT / 'certifications/saa-c03.json')
        coverage['coverage'][0]['labs'] = ['missing']
        with self.assertRaises(ValueError): validate_coverage(coverage, self.certifications, labs, self.root)

    def test_no_evidence_no_coverage(self):
        labs, _ = self.validate()
        coverage = load(ROOT / 'certifications/saa-c03.json')
        coverage['coverage'][0]['evidence'] = []
        with self.assertRaises(ValueError): validate_coverage(coverage, self.certifications, labs, self.root)


if __name__ == '__main__':
    unittest.main()
