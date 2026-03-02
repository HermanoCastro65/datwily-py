import pandas as pd
from datwily import Dataset

def test_select_keeps_only_specified_columns():
    df = pd.DataFrame({
        "name": ["Ana", "Bruno"],
        "age": [20, 30],
        "salary": [2000, 3000]
    })

    data = Dataset(df)
    data.select(["name", "age"])

    assert list(data.df.columns) == ["name", "age"]


def test_drop_removes_specified_columns():
    df = pd.DataFrame({
        "name": ["Ana", "Bruno"],
        "age": [20, 30],
        "salary": [2000, 3000]
    })

    data = Dataset(df)
    data.drop(["salary"])

    assert "salary" not in data.df.columns