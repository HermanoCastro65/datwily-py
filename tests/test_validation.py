import pandas as pd
from datwily import Dataset

def test_validation_detects_negative_values():
    df = pd.DataFrame({
        "age": [20, -5, 30]
    })

    data = Dataset(df)
    report = data.validate()

    assert "age" in report["negative_values"]


def test_validation_detects_non_numeric_column():
    df = pd.DataFrame({
        "salary": ["high", "low", "medium"]
    })

    data = Dataset(df)
    report = data.validate()

    assert "salary" in report["invalid_types"]