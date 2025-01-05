import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
class ExtractData:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self.load_csv()

    def load_csv(self) -> pd.DataFrame | None:
        try:
            df = pd.read_csv(self.file_path)
            logger.info('CSV successfully loaded into dataframe')
            return df
        except Exception as e:
            logger.error(f"Error reading from CSV file: {e}")
            return None