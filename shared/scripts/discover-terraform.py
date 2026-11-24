#!/usr/bin/env python3
"""Gera uma matriz determinística de CI com os diretórios raiz Terraform versionados, sem acesso à AWS."""
import json
import re
import subprocess
from pathlib import PurePosixPath


def discover(files):
    tracked = set(files)
    roots = sorted({
        str(PurePosixPath(name).parent)
        for name in tracked
        if re.fullmatch(r"labs/lab[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*/terraform/[^/]+\.tf", name)
    })
    if len(roots) > 256:
        raise ValueError("GitHub Actions supports at most 256 matrix jobs; shard discovery first.")
    for root in roots:
        for required in ("versions.tf", ".terraform.lock.hcl"):
            if f"{root}/{required}" not in tracked:
                raise ValueError(f"{root}: missing tracked {required}")
    return roots


if __name__ == "__main__":
    paths = subprocess.check_output(["git", "ls-files", "-z"], text=True).split("\0")
    print(json.dumps(discover(filter(None, paths)), separators=(",", ":")))
