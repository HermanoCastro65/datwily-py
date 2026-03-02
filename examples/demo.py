from datwily import Dataset, Pipeline
import pandas as pd
from pathlib import Path
import tempfile


def create_large_mock(path):
    df = pd.DataFrame({
        "Full Name": [
            "Ana Silva","Bruno Souza","Carlos Pereira","Daniel Costa","Eduardo Alves",
            "Fernanda Rocha","Gabriel Martins","Helena Barros","Igor Teixeira","Juliana Melo",
            "Karen Dias","Lucas Ribeiro","Marina Gomes","Nicolas Freitas","Olivia Farias"
        ],
        "Age": [22, None, 35, 28, 41, None, 19, 23, 120, 27, 31, None, 29, 33, 26],
        "City": [
            "Rio","SP","Rio","BH","Curitiba","SP","Rio","Rio","SP","Curitiba",
            "BH","Rio","Rio","SP","Curitiba"
        ],
        "Salary": [
            2500,3000,4500,None,7000,5200,1800,2300,999999,4100,3900,None,3600,4800,3200
        ],
        "System ID": [
            "A12","A13","A14","A15","A16","A17","A18","A19","A20","A21",
            "A22","A23","A24","A25","A26"
        ]
    })

    df.to_csv(path, index=False)


def main():
    tmp_dir = Path(tempfile.gettempdir())
    file_path = tmp_dir / "datwily_large_demo.csv"

    create_large_mock(file_path)

    print("Loading dataset...")
    data = Dataset(file_path)

    print("Initial shape:", data.shape)
    print("Initial missing:", data.missing.count())

    # --- Pipeline de preparação ---
    pipe = Pipeline()
    pipe.add(lambda d: d.columns.normalize())
    pipe.add(lambda d: d.missing.fill_mean("age"))
    pipe.add(lambda d: d.outliers.remove("age"))
    pipe.add(lambda d: d.missing.fill_value("salary", 0))
    pipe.add(lambda d: d.outliers.remove("salary"))
    pipe.add(lambda d: d.encode.one_hot("city"))
    pipe.add(lambda d: d.scale.minmax("salary"))

    pipe.run(data)

    print("After processing shape:", data.shape)
    print("Remaining missing:", data.missing.count())

    print("\nStatistics:")
    print(data.describe())

    # split treino/teste
    train, test = data.split(test_size=0.3, seed=42)

    print("\nTrain rows:", train.rows)
    print("Test rows:", test.rows)

    # export
    clean_csv = tmp_dir / "clean_output.csv"
    clean_json = tmp_dir / "clean_output.json"

    data.to_csv(clean_csv)
    data.to_json(clean_json)

    print("\nExported files:")
    print(clean_csv)
    print(clean_json)

    # cleanup
    if file_path.exists():
        file_path.unlink()


if __name__ == "__main__":
    main()