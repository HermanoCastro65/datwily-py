import pandas as pd
from datwily import Dataset

def test_dataset_to_csv_creates_file(tmp_path):
    df = pd.DataFrame({
        "name": ["Ana", "Bruno"],
        "age": [20, 30]
    })

    data = Dataset(df)

    file_path = tmp_path / "output.csv"
    data.to_csv(file_path)

    assert file_path.exists()

def test_dataset_to_json_creates_file(tmp_path):
    df = pd.DataFrame({
        "name": ["Ana", "Bruno"],
        "age": [20, 30]
    })

    data = Dataset(df)

    file_path = tmp_path / "output.json"
    data.to_json(file_path)

    assert file_path.exists()