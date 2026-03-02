class Pipeline:
    def __init__(self):
        self.steps = []

    def add(self, func):
        if not callable(func):
            raise TypeError("Pipeline step must be callable")
        self.steps.append(func)

    def run(self, dataset):
        for step in self.steps:
            step(dataset)

        return dataset