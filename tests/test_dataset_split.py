import pandas as pd
from datwily import Dataset

def test_dataset_split_returns_two_datasets():
    df = pd.DataFrame({
        "age": [20,21,22,23,24,25,26,27,28,29]
    })

    data = Dataset(df)

    train, test = data.split(test_size=0.2, seed=42)

    assert isinstance(train, Dataset)
    assert isinstance(test, Dataset)
    assert train.rows + test.rows == data.rows
    assert test.rows == 2