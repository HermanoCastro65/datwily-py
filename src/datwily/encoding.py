import pandas as pd

class EncodingHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def one_hot(self, column):
        df = self.dataset.df

        dummies = pd.get_dummies(df[column], prefix=column)

        df = df.drop(columns=[column])
        df = pd.concat([df, dummies], axis=1)

        self.dataset.df = df.copy()