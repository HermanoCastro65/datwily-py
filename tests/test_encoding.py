import pandas as pd
from datwily import Dataset

def test_one_hot_encoding_creates_binary_columns():
    df = pd.DataFrame({
        "city": ["Rio", "SP", "Rio"]
    })

    data = Dataset(df)
    data.encode.one_hot("city")

    assert "city_Rio" in data.df.columns
    assert "city_SP" in data.df.columns
    assert "city" not in data.df.columns