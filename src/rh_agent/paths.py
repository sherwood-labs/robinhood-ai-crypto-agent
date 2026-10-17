"""Repository root.

Logs, .env, and .mcp.json stay at the root. Package modules live under src/.
"""

from pathlib import Path


def _repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "pyproject.toml").is_file() and (parent / ".mcp.json").is_file():
            return parent
    raise RuntimeError("Could not find the repository root (expected pyproject.toml and .mcp.json).")


ROOT = _repo_root()
