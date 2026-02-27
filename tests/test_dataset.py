import pandas as pd
from datwily import Dataset

def test_dataset_accepts_dataframe():
    df = pd.DataFrame({"idade":[10,20,30]})
    data = Dataset(df)
    assert data.df is not None