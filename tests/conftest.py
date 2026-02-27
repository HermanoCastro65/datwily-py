import pytest
import pandas as pd

@pytest.fixture
def sample_csv(tmp_path):
    df = pd.DataFrame({
        "nome": ["Ana", "Bruno", "Carlos"],
        "idade": [25, 30, 22]
    })

    file_path = tmp_path / "clientes.csv"
    df.to_csv(file_path, index=False)

    return file_path