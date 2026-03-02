import pandas as pd
from datwily import Dataset
from datwily.pipeline import Pipeline

def test_pipeline_executes_transformations():
    df = pd.DataFrame({
        "Full Name": ["Ana", "Bruno", "Carlos"],
        "Age": [20, None, 40],
        "City": ["Rio", "SP", "Rio"],
        "Salary": [2000, 3000, 4000]
    })

    data = Dataset(df)

    pipe = Pipeline()
    pipe.add(lambda d: d.columns.normalize())
    pipe.add(lambda d: d.missing.fill_mean("age"))
    pipe.add(lambda d: d.encode.one_hot("city"))
    pipe.add(lambda d: d.scale.minmax("salary"))

    pipe.run(data)

    assert "full_name" in data.df.columns
    assert "city_Rio" in data.df.columns
    assert data.df["age"].isna().sum() == 0
    assert data.df["salary"].max() == 1.0