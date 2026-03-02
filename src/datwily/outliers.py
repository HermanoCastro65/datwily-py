class OutlierHandler:
    def __init__(self, dataset):
        self.dataset = dataset

    def detect(self, column):
        series = self.dataset.df[column]

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outliers = series[(series < lower_bound) | (series > upper_bound)]

        return list(outliers.values)

    def remove(self, column):
        series = self.dataset.df[column]

        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        self.dataset.df = self.dataset.df[
            (series >= lower_bound) & (series <= upper_bound)
        ].copy()