import pytest
from datwily import Dataset

def test_dataset_raises_error_for_missing_file():
    with pytest.raises(FileNotFoundError, match="File not found"):
        Dataset("missing_file.csv")