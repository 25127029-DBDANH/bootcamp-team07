"""Pytest configuration for w2 tests."""

import sys
from pathlib import Path

BOOTCAMP_DIR = Path(__file__).resolve().parents[3]
if str(BOOTCAMP_DIR) not in sys.path:
    sys.path.insert(0, str(BOOTCAMP_DIR))
