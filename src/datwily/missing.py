class MissingHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def count(self):
        return self.dataset.df.isna().sum().sum()

    def drop_rows(self):
        self.dataset.df = self.dataset.df.dropna()