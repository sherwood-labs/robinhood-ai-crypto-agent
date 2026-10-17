"""Launcher. Implementation: rh_agent.storage.scorecard."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / "src"))

if __name__ == "__main__":
    import runpy

    runpy.run_module("rh_agent.storage.scorecard", run_name="__main__")
