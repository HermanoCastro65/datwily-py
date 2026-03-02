import pandas as pd
from pathlib import Path

class Dataset:
    def __init__(self, source):
        if isinstance(source, pd.DataFrame):
            self.df = source

        elif isinstance(source, (str, Path)):
            path = Path(source)

            if not path.exists():
                raise FileNotFoundError(f"File not found: {path}")

            self.df = pd.read_csv(path)

        else:
            raise TypeError("Unsupported data source")

    @property
    def shape(self):
        return self.df.shape

    @property
    def columns(self):
        return list(self.df.columns)

    @property
    def rows(self):
        return len(self.df)