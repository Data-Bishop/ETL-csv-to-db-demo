from pathlib import Path
from typing import Dict, Any
import yaml

class Config:
    def __init__(self):
        self.config_file = Path(__file__).parent / 'config.yaml' # Construct patht to config file
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        if not self.config_file.exists():
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        with open(self.config_file, 'r') as file:
            return yaml.safe_load(file)
    
    def get_database_config(self) -> Dict[str, Any]:
        return self.config.get('database', {})
    
    def get_paths(self) -> Dict[str, Any]:
        return self.config.get('paths', {})
    
    def get_transform_config(self) -> Dict[str, Any]:
        return self.config.get('transform', {})