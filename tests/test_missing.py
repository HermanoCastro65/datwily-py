import pandas as pd
from datwily import Dataset

def test_missing_count():
    df = pd.DataFrame({
        "name": ["Ana", None, "Carlos"],
        "age": [20, 25, None]
    })

    data = Dataset(df)

    assert data.missing.count() == 2

def test_missing_drop_rows():
    df = pd.DataFrame({
        "name": ["Ana", None, "Carlos"],
        "age": [20, 25, None]
    })

    data = Dataset(df)
    data.missing.drop_rows()

    assert data.rows == 1