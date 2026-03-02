import pandas as pd
from datwily import Dataset

def test_normalize_column_names_basic():
    df = pd.DataFrame({
        "Full Name": ["Ana", "Bruno"],
        "Age": [20, 30]
    })

    data = Dataset(df)
    data.columns.normalize()

    assert "full_name" in data.df.columns
    assert "age" in data.df.columns


def test_normalize_column_names_special_chars():
    df = pd.DataFrame({
        "E-mail@Cliente": ["a@mail.com", "b@mail.com"],
        "Cidade/Estado": ["RJ", "SP"]
    })

    data = Dataset(df)
    data.columns.normalize()

    assert "email_cliente" in data.df.columns
    assert "cidade_estado" in data.df.columns