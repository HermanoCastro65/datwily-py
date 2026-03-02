import pandas as pd
from datwily import Dataset

def test_profile_numeric_column():
    df = pd.DataFrame({
        "age": [20, 30, 40, None]
    })

    data = Dataset(df)
    profile = data.profile()

    assert profile["age"]["type"] == "numeric"
    assert profile["age"]["missing"] == 1


def test_profile_categorical_column():
    df = pd.DataFrame({
        "city": ["Rio", "SP", "Rio", "BH"]
    })

    data = Dataset(df)
    profile = data.profile()

    assert profile["city"]["type"] == "categorical"
    assert profile["city"]["unique"] == 3