import os
from pathlib import Path
from importlib.util import find_spec
from git import Repo

try:
    import fake_records
except:
    pass

try:
    import pandas as pd
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
    } == set(df.columns)


def test_data_folder_ignored():
    r = Repo(".")
    if not os.path.exists("data"):
        os.mkdir("data")
    open("data/test", "wb").close()
    assert not r.untracked_files
    os.remove("data/test")
    os.rmdir("data")


def test_save():
    df = pd.DataFrame({"a": [1]})
    fake_records.save(df)
    assert os.path.exists("data/fake_records.csv")
    os.remove("data/fake_records.csv")
    os.rmdir("data")


def test_load(tmp_path):
    df = pd.DataFrame({"a": [1]})
    df.to_csv(tmp_path / "test.csv")
    assert fake_records.load("test.csv").loc["a"] == 1


def test_assign_salaries():
    df = pd.DataFrame({"a": [1]})
    df = fake_records.assign_salaries(df)
    df["Salary"].min() >= 20000
    df["Salary"].max() <= 100000
    assert len(df.columns) == 2
