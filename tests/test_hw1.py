from pathlib import Path


def test_module_exists():
    assert Path("fake_records.py").exists()
