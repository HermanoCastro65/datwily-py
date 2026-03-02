import pandas as pd
from datwily import Dataset

def test_detect_outliers_iqr():
    df = pd.DataFrame({
        "age": [20, 22, 21, 23, 400]
    })

    data = Dataset(df)
    outliers = data.outliers.detect("age")

    assert 400 in outliers