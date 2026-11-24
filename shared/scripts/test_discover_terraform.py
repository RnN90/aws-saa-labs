"""Guard matrix discovery against missing root requirements and cache contamination."""
import runpy
import unittest
from pathlib import Path

discover = runpy.run_path(str(Path(__file__).with_name("discover-terraform.py")))["discover"]


def files(root):
    return [f"{root}/{name}" for name in ("main.tf", "versions.tf", ".terraform.lock.hcl")]


class DiscoveryTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(discover([]), [])

    def test_sorted_unique_roots(self):
        roots = ["labs/lab02-storage/terraform", "labs/lab01-network/terraform"]
        self.assertEqual(discover(files(roots[0]) + files(roots[1]) + files(roots[0])), sorted(roots))

    def test_ignore_nested_cache_and_modules(self):
        root = "labs/lab01-network/terraform"
        paths = files(root) + [f"{root}/.terraform/providers/main.tf", f"{root}/modules/vpc/main.tf"]
        self.assertEqual(discover(paths), [root])

    def test_missing_lock(self):
        with self.assertRaisesRegex(ValueError, "missing tracked .terraform.lock.hcl"):
            discover(["labs/lab01-network/terraform/main.tf", "labs/lab01-network/terraform/versions.tf"])

    def test_missing_versions(self):
        with self.assertRaisesRegex(ValueError, "missing tracked versions.tf"):
            discover(["labs/lab01-network/terraform/main.tf"])

    def test_invalid_layout_is_not_a_root(self):
        self.assertEqual(discover(["labs/lab1-network/terraform/main.tf", "shared/main.tf"]), [])

    def test_matrix_limit(self):
        paths = [path for i in range(257) for path in files(f"labs/lab01-example-{i}/terraform")]
        with self.assertRaisesRegex(ValueError, "256 matrix jobs"):
            discover(paths)


if __name__ == "__main__":
    unittest.main()
