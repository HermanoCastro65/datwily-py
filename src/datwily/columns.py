import re
import unicodedata


class ColumnHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def _remove_accents(self, text):
        return ''.join(
            c for c in unicodedata.normalize('NFKD', text)
            if not unicodedata.combining(c)
        )

    def normalize(self):
        new_columns = []

        for col in self.dataset.df.columns:
            col = col.strip().lower()
            col = self._remove_accents(col)

            col = col.replace("-", "")
            col = col.replace("@", "_")
            col = col.replace("/", "_")
            col = col.replace(" ", "_")

            col = re.sub(r"[^a-z0-9_]", "", col)
            col = re.sub(r"_+", "_", col)
            col = col.strip("_")

            new_columns.append(col)

        self.dataset.df.columns = new_columns

    def __iter__(self):
        return iter(self.dataset.df.columns)

    def __len__(self):
        return len(self.dataset.df.columns)

    def __getitem__(self, item):
        return self.dataset.df.columns[item]

    def __repr__(self):
        return repr(list(self.dataset.df.columns))

    def __eq__(self, other):
        return list(self.dataset.df.columns) == list(other)