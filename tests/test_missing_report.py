import pandas as pd
from datwily import Dataset

def test_missing_report_counts_per_column():
    df = pd.DataFrame({
        "name": ["Ana", None, "Carlos"],
        "age": [20, 25, None]
    })

    data = Dataset(df)
    report = data.missing.report()

    assert report["name"] == 1
    assert report["age"] == 1