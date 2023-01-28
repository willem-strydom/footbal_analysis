import os
from pathlib import Path
from importlib.util import find_spec
from git import Repo

try:
    import fake_records
except:
    pass


def test_module_exists():
    assert Path("fake_records.py").exists()


def test_faker_installed():
    assert find_spec("faker")


def test_generate():
    df = fake_records.generate()
    assert len(df) == 1000
    assert {
        "First Name",
        "Last Name",
        "Birthday",
        "Email",
        "Phone Number",
    } == df.columns()


def test_data_folder_ignored():
    r = Repo(".")
    os.mkdir("data")
    open("data/test", "wb").close()
    assert not r.untracked_files
