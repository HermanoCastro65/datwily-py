import pandas as pd
from pathlib import Path
from .missing import MissingHandler
from .columns import ColumnHandler
from .outliers import OutlierHandler
from .encoding import EncodingHandler

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
        
        self.missing = MissingHandler(self)
        self.columns = ColumnHandler(self)
        self.outliers = OutlierHandler(self)
        self.encode = EncodingHandler(self)

    @property
    def shape(self):
        return self.df.shape

    @property
    def rows(self):
        return len(self.df)
    
    def select(self, columns):
        self.df = self.df.loc[:, columns].copy()

    def drop(self, columns):
        self.df = self.df.drop(columns=columns).copy()

    def describe(self):
        numeric_df = self.df.select_dtypes(include="number")

        report = {}

        for column in numeric_df.columns:
            series = numeric_df[column]

            report[column] = {
                "count": int(series.count()),
                "mean": float(series.mean()),
                "std": float(series.std()),
                "min": float(series.min()),
                "max": float(series.max())
            }

        return report