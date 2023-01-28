from pathlib import Path
from importlib.util import find_spec
from git import Repo
import os


def test_module_exists():
    assert Path("fake_records.py").exists()


def test_faker_installed():
    assert find_spec("faker")


def test_data_folder_ignored():
    r = Repo(".")
    os.mkdir("data")
    open("data/test", "wb").close()
    assert not r.untracked_files
