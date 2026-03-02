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

            try:
                df = pd.read_csv(path, encoding="utf-8")
                if df.shape[1] == 1:
                    df = pd.read_csv(path, encoding="utf-8", sep=";")
            except UnicodeDecodeError:
                df = pd.read_csv(path, encoding="latin-1")
                if df.shape[1] == 1:
                    df = pd.read_csv(path, encoding="latin-1", sep=";")

            self.df = df

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

        return Dataset(train_df), Dataset(test_df)

    def to_csv(self, path):
        path = Path(path)
        self.df.to_csv(path, index=False)

    def to_json(self, path):
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

    def profile(self):
        profile = {}

        for column in self.df.columns:
            series = self.df[column]

            col_profile = {}
            col_profile["missing"] = int(series.isna().sum())
            col_profile["unique"] = int(series.nunique(dropna=True))

            if pd.api.types.is_numeric_dtype(series):
                col_profile["type"] = "numeric"
                col_profile["mean"] = float(series.mean()) if series.count() > 0 else None
                col_profile["min"] = float(series.min()) if series.count() > 0 else None
                col_profile["max"] = float(series.max()) if series.count() > 0 else None
            else:
                col_profile["type"] = "categorical"
                mode = series.mode(dropna=True)
                col_profile["top"] = mode.iloc[0] if not mode.empty else None

            profile[column] = col_profile

        return profile