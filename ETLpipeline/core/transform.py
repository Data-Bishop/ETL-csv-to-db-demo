from ETLpipeline.config import config
import pandas as pd

class TransformData:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.config = config.get_transform_config()
        self.transformed_data = self.bonus_increment()

    def bonus_increment(self) -> pd.DataFrame:
        multiplier = self.config['salary_multiplier']
        self.data['salary'] = self.data['salary'] * multiplier
        return self.data
