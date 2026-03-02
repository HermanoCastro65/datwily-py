import pandas as pd
import tempfile
from pathlib import Path
from datwily import Dataset


def create_mock_dataset(file_path):
    df = pd.DataFrame({
        "Name": ["Ana", "Bruno", None, "Carla", "Daniel"],
        "Age": [25, None, 40, None, 30],
        "City": ["Rio", "Sao Paulo", "Rio", None, "Curitiba"],
        "Salary": [3000, 4500, None, 5000, None]
    })

    df.to_csv(file_path, index=False)


def main():
    temp_dir = tempfile.gettempdir()
    file_path = Path(temp_dir) / "datwily_demo_dataset.csv"

    try:
        print("Creating mock dataset...")
        create_mock_dataset(file_path)

        print(f"Dataset saved at: {file_path}")

        data = Dataset(file_path)

        print("\n=== BASIC INFO ===")
        print("Shape:", data.shape)
        print("Columns:", data.columns)
        print("Rows:", data.rows)

        print("\n=== MISSING VALUES ===")
        print("Total missing:", data.missing.count())
        print("Per-column report:", data.missing.report())

        print("\n=== FILL OPERATIONS ===")
        data.missing.fill_mean("Age")
        data.missing.fill_value("City", "Unknown")
        data.missing.fill_value("Salary", 0)

        print("After filling:")
        print("Missing count:", data.missing.count())
        print("Report:", data.missing.report())

        print("\n=== DROP ROWS (if any left) ===")
        data.missing.drop_rows()
        print("Rows after drop:", data.rows)

        print("\n=== FINAL DATAFRAME ===")
        print(data.df)

    finally:
        if file_path.exists():
            file_path.unlink()
            print("\nTemporary dataset removed.")


if __name__ == "__main__":
    main()