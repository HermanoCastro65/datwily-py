import pandas as pd
from datwily import Dataset

def test_describe_returns_statistics_for_numeric_columns():
    df = pd.DataFrame({
        "age": [20, 30, 40],
        "salary": [2000, 3000, 4000]
    })

    data = Dataset(df)
    report = data.describe()

    assert report["age"]["mean"] == 30
    assert report["salary"]["max"] == 4000