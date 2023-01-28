from pathlib import Path
from importlib.util import find_spec


def test_module_exists():
    assert Path("fake_records.py").exists()


def test_faker_installed():
    assert find_spec("faker")
