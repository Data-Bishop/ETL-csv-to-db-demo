import pandas as pd

class ExtractData:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_csv()

    def load_csv(self) -> pd.DataFrame | None:
        try:
           return pd.read_csv(self.file_path)
        except Exception as e:
            print(f"Error loading CSV file: {e}")
            return None