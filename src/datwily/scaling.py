class ScalingHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def minmax(self, column):
        series = self.dataset.df[column]

        min_val = series.min()
        max_val = series.max()

        if max_val == min_val:
            self.dataset.df[column] = 0.0
            return

        scaled = (series - min_val) / (max_val - min_val)

        self.dataset.df[column] = scaled.astype(float)