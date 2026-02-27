import pandas as pd
from pathlib import Path

class Dataset:
    def __init__(self, source):
        if isinstance(source, pd.DataFrame):
            self.df = source
        elif isinstance(source, (str, Path)):
            self.df = pd.read_csv(source)
        else:
            raise TypeError("Unsupported data source")