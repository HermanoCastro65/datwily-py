import pandas as pd
from pathlib import Path
from .missing import MissingHandler
from .columns import ColumnHandler
from .outliers import OutlierHandler
from .encoding import EncodingHandler
from .scaling import ScalingHandler

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
        self.scale = ScalingHandler(self)

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

    def split(self, test_size=0.2, seed=None):
        if not 0 < test_size < 1:
            raise ValueError("test_size must be between 0 and 1")

        df_shuffled = self.df.sample(frac=1, random_state=seed).reset_index(drop=True)

        test_count = int(len(df_shuffled) * test_size)

        test_df = df_shuffled.iloc[:test_count].copy()
        train_df = df_shuffled.iloc[test_count:].copy()

        from .dataset import Dataset

        return Dataset(train_df), Dataset(test_df)

    def to_csv(self, path):
        from pathlib import Path
        path = Path(path)
        self.df.to_csv(path, index=False)

    def to_json(self, path):
        from pathlib import Path
        path = Path(path)
        self.df.to_json(path, orient="records", indent=2)

    def validate(self):
        report = {
            "negative_values": [],
            "invalid_types": []
        }

        for column in self.df.columns:
            series = self.df[column]

            if pd.api.types.is_numeric_dtype(series):
                if (series < 0).any():
                    report["negative_values"].append(column)
            else:
                try:
                    series.astype(float)
                except:
                    report["invalid_types"].append(column)

        return report