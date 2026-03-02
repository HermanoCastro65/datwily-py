import pandas as pd
from datwily import Dataset

def test_minmax_scaling_normalizes_values_between_0_and_1():
    df = pd.DataFrame({
        "salary": [2000, 3000, 4000]
    })

    data = Dataset(df)
    data.scale.minmax("salary")

    assert data.df["salary"].min() == 0.0
    assert data.df["salary"].max() == 1.0