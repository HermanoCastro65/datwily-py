import pandas as pd
from datwily import Dataset

def test_dataset_shape():
    df = pd.DataFrame({"a":[1,2,3],"b":[4,5,6]})
    data = Dataset(df)
    assert data.shape == (3, 2)

def test_dataset_columns():
    df = pd.DataFrame({"name":["Ana","Bruno"],"age":[20,30]})
    data = Dataset(df)
    assert data.columns == ["name", "age"]

def test_dataset_rows():
    df = pd.DataFrame({"a":[1,2,3,4]})
    data = Dataset(df)
    assert data.rows == 4