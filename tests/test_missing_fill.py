import pandas as pd
from datwily import Dataset

def test_fill_mean_replaces_missing_numeric_values():
    df = pd.DataFrame({
        "age": [20, None, 40]
    })

    data = Dataset(df)
    data.missing.fill_mean("age")

    assert data.df["age"].isna().sum() == 0

def test_fill_value_replaces_missing_with_constant():
    df = pd.DataFrame({
        "city": ["Rio", None, "Sao Paulo"]
    })

    data = Dataset(df)
    data.missing.fill_value("city", "Unknown")

    assert "Unknown" in data.df["city"].values