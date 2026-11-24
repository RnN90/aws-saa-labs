#!/usr/bin/env python3
"""Valida metadados e referências locais; não consulta nem modifica a AWS."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator, SchemaError, ValidationError

ROOT = Path(__file__).resolve().parents[2]
COVERAGE_STATUSES = {"not-mapped", "planned", "partial", "covered", "validated"}


def load(path):
    """JSON é o subconjunto de YAML 1.2 adotado, sem aliases ou expressões."""
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Chave duplicada: {key} em {path}")
            result[key] = value
        return result
    if Path(path).is_symlink():
        raise ValueError(f"Arquivo declarativo não pode ser symlink: {path}")
    return json.loads(Path(path).read_text(), object_pairs_hook=unique)


def local_path(root, value):
    path = (root / value).resolve()
    if not path.is_relative_to(root.resolve()) or not path.exists():
        raise ValueError(f"Caminho local inexistente ou fora do repositório: {value}")
    return path


def topological_order(labs):
    """Inclui todos os tipos e cenários opcionais para rejeitar ciclos potenciais."""
    visiting, visited, order = set(), set(), []
    def visit(key):
        if key in visiting:
            raise ValueError(f"Dependência circular envolvendo {key}")
        if key in visited:
            return
        visiting.add(key)
        for dep in labs[key]["dependencies"]:
            target = dep["lab"]
            if target not in labs:
                raise ValueError(f"Dependência inexistente: {target}")
            visit(target)
        visiting.remove(key)
        visited.add(key)
        order.append(key)
    for key in sorted(labs):
        visit(key)
    return order


def validate_labs(entries, schema, capabilities, certification_codes, root):
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    labs, owners, numbers = {}, {}, set()
    for path, lab in entries:
        validator.validate(lab)
        key = lab["id"]
        if key in labs or lab["number"] in numbers:
            raise ValueError(f"Identificador ou número duplicado: {key}")
        local_path(root, str(path.relative_to(root)))
        if path.parent.name != f'lab{lab["number"]:02}-{key}':
            raise ValueError(f"Diretório inconsistente: {path}")
        local_path(root, str((path.parent / "README.md").relative_to(root)))
        if lab["ownership"]["resource_owner"] != key:
            raise ValueError(f"Ownership inconsistente: {key}")
        if not set(lab["certifications"]) <= certification_codes:
            raise ValueError(f"Certificação inexistente em {key}")
        if lab["terraform"] is not None:
            tf = local_path(root, str((path.parent / lab["terraform"]).relative_to(root)))
            if not tf.is_relative_to(path.parent.resolve()):
                raise ValueError(f"Terraform fora do LAB: {key}")
            for filename in ("versions.tf", ".terraform.lock.hcl"):
                local_path(root, str((tf / filename).relative_to(root)))
        if lab["status"] == "planned" and any(path.parent.rglob("*.tf")):
            raise ValueError(f"LAB planejado contém Terraform: {key}")
        for item in lab["provides"]:
            cap = item["capability"]
            if cap not in capabilities or cap in owners:
                raise ValueError(f"Capacidade inexistente ou proprietário duplicado: {cap}")
            owners[cap] = (key, item["contract_version"])
        for channel in lab["publication"].values():
            if channel["status"] == "published" and not channel["url"]:
                raise ValueError(f"Publicação sem URL em {key}")
        labs[key] = lab
        numbers.add(lab["number"])
    if set(owners) != set(capabilities):
        raise ValueError("Catálogo contém capacidade sem LAB proprietário")
    for key, lab in labs.items():
        deps = {d["id"]: d for d in lab["dependencies"]}
        if len(deps) != len(lab["dependencies"]):
            raise ValueError(f"Identificador de dependência duplicado em {key}")
        for dep in deps.values():
            if dep["type"] == "infrastructure-optional" and not dep["scenario"]:
                raise ValueError(f"Dependência opcional sem cenário em {key}")
            if dep["type"] != "infrastructure-optional" and dep["scenario"] is not None:
                raise ValueError(f"Cenário reservado para dependência opcional em {key}")
        for item in lab["consumes"]:
            cap, dep_id = item["capability"], item["dependency"]
            if cap not in owners or dep_id not in deps:
                raise ValueError(f"Referência de capacidade/dependência inexistente em {key}")
            if owners[cap] != (deps[dep_id]["lab"], item["contract_version"]):
                raise ValueError(f"Contrato ou proprietário incompatível em {key}: {cap}")
    return labs, topological_order(labs)


def validate_coverage(coverage, certifications, labs, root):
    codes = {c["code"] for c in certifications}
    if len(codes) != len(certifications):
        raise ValueError("Código de certificação duplicado")
    if coverage["exam_code"] not in codes:
        raise ValueError("Exame da matriz inexistente")
    tasks = {t["id"] for t in coverage["official_tasks"]}
    if len(tasks) != len(coverage["official_tasks"]):
        raise ValueError("Objetivo oficial duplicado")
    seen = set()
    for row in coverage["coverage"]:
        if row["task"] not in tasks or row["task"] in seen:
            raise ValueError("Objetivo inexistente ou duplicado na cobertura")
        seen.add(row["task"])
        if row["level"] not in {f"L{i}" for i in range(1, 6)}:
            raise ValueError("Nível de competência inválido")
        if not set(row["labs"]) <= set(labs):
            raise ValueError("LAB inexistente na cobertura")
        if set(row["modes"]) != {"theoretical", "practical", "architectural"}:
            raise ValueError("Modalidades de cobertura incompletas")
        if not set(row["modes"].values()) <= COVERAGE_STATUSES:
            raise ValueError("Status de cobertura inválido")
        for evidence in row["evidence"]:
            local_path(root, evidence)
        if any(s in {"covered", "validated", "partial"} for s in row["modes"].values()) and not row["evidence"]:
            raise ValueError("Cobertura sem evidência")
        if any(s in {"covered", "validated", "partial"} for s in row["modes"].values()) and not any(labs[k]["status"] == "implemented" for k in row["labs"]):
            raise ValueError("Cobertura atribuída somente a LAB planejado")
    if seen != tasks:
        raise ValueError("Matriz deve explicitar objetivos ainda não mapeados")


def validate_docs(root, paths):
    """Verifica links locais e estrutura básica; não equivale a renderização Mermaid."""
    links, diagrams = 0, 0
    for path in paths:
        text = path.read_text()
        if sum(line.startswith("```") for line in text.splitlines()) % 2:
            raise ValueError(f"Cerca Markdown sem fechamento: {path}")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            if urlsplit(target).scheme or target.startswith("#"):
                continue
            value = unquote(target.split("#")[0])
            local_path(root, str((path.parent / value).relative_to(root)))
            links += 1
        for diagram in re.findall(r"```mermaid\n(.*?)```", text, re.S):
            diagrams += 1
            if diagram.startswith("flowchart"):
                if len(re.findall(r"^\s*subgraph ", diagram, re.M)) != len(re.findall(r"^\s*end\s*$", diagram, re.M)) or diagram.count("[") != diagram.count("]"):
                    raise ValueError(f"Estrutura Mermaid inconsistente: {path}")
            elif diagram.startswith("sequenceDiagram"):
                participants = set(re.findall(r"^\s*(?:actor|participant) (\w+)", diagram, re.M))
                for source, target in re.findall(r"^\s*(\w+)-[-]?>>(\w+):", diagram, re.M):
                    if not {source, target} <= participants:
                        raise ValueError(f"Participante Mermaid inexistente: {path}")
            else:
                raise ValueError(f"Tipo Mermaid ainda não suportado: {path}")
    return links, diagrams


def validate_repository(root=ROOT):
    entries = [(p, load(p)) for p in sorted((root / "labs").glob("*/lab.yaml"))]
    all_lab_dirs = {p.parent for p in (root / "labs").glob("*/README.md")}
    if all_lab_dirs != {p.parent for p, _ in entries}:
        raise ValueError("Todo LAB documentado deve possuir manifesto")
    certs = load(root / "certifications/catalog.json")["certifications"]
    labs, order = validate_labs(entries, load(root / "shared/schemas/lab-v1.schema.json"), load(root / "catalog/capabilities.json")["capabilities"], {c["code"] for c in certs}, root)
    validate_coverage(load(root / "certifications/saa-c03.json"), certs, labs, root)
    # Somente conteúdo Git evita ler artefatos privados locais.
    import subprocess
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=root, text=True).split("\0")
    docs = [root / p for p in tracked if p.endswith(".md")]
    links, diagrams = validate_docs(root, docs)
    print(f"Catálogo válido: {len(labs)} LABs; {links} links; {diagrams} diagramas estruturais.")
    print("Ordem conceitual do DAG (não é plano de execução): " + ", ".join(order))
    return labs


if __name__ == "__main__":
    try:
        validate_repository()
    except (ValueError, OSError, KeyError, SchemaError, ValidationError) as exc:
        raise SystemExit(str(exc)) from exc
