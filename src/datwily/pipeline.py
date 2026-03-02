import pickle
from pathlib import Path

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

    def save(self, path):
        path = Path(path)

        serializable_steps = []
        for step in self.steps:
            if step.__name__ == "<lambda>":
                raise ValueError(
                    "Lambda functions cannot be saved. "
                    "Use Pipeline.add_step(handler, method, *args) instead."
                )
            serializable_steps.append(step.__name__)

        with open(path, "wb") as f:
            pickle.dump(serializable_steps, f)

    @classmethod
    def load(cls, path):
        path = Path(path)
        with open(path, "rb") as f:
            _ = pickle.load(f)

        return cls()