class MissingHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def count(self):
        return self.dataset.df.isna().sum().sum()

    def drop_rows(self):
        self.dataset.df = self.dataset.df.dropna()

    def report(self):
        missing_counts = self.dataset.df.isna().sum()
        return missing_counts.to_dict()
    
    def fill_mean(self, column):
        mean_value = self.dataset.df[column].mean()
        self.dataset.df[column] = self.dataset.df[column].fillna(mean_value)

    def fill_value(self, column, value):
        self.dataset.df[column] = self.dataset.df[column].fillna(value)