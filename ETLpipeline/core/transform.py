from ETLpipeline.config import config
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class TransformData:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.config = config.get_transform_config()
        self.transformed_data = self.bonus_increment()

    def bonus_increment(self) -> pd.DataFrame:
        try:
            multiplier = self.config['salary_multiplier']
            self.data['salary'] = self.data['salary'] * multiplier
            return self.data
        except Exception as e:
            logger.error('Error encountered while transforming data: {e}')