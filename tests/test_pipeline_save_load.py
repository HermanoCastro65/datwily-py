import pandas as pd
from datwily import Dataset, Pipeline

def encode_city(dataset):
    dataset.encode.one_hot("city")

def test_pipeline_can_be_saved_and_loaded(tmp_path):
    df = pd.DataFrame({
        "city": ["Rio", "SP", "Rio"]
    })

    data = Dataset(df)

    pipe = Pipeline()
    pipe.add(encode_city)

    file_path = tmp_path / "pipe.dtw"
    pipe.save(file_path)

    loaded = Pipeline.load(file_path)
    loaded.add(encode_city)
    loaded.run(data)

    assert "city_Rio" in data.df.columns