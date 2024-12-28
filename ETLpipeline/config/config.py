from pathlib import Path
from typing import Dict, Any
import os
import yaml

class Config:
    _instance = None
    def __new__(cls) -> 'Config':
        if cls._instance is None:
            cls._instance = super().__new__(cls) # Create new class object
            cls._instance._load_config() # Set up the created object
        return cls
    
    def _load_config(self) -> None:
        config_path = Path(__file__).parent / 'config.yaml' # Construct patht to config file
        with open(config_path, 'r', encoding='utf-8') as file:
            self._config = yaml.safe_load(file)
        self._resolve_env_vars()
            
    def _resolve_env_vars(self) -> None:
        def resolve(value: Any) -> Any:
            if isinstance(value, str) and value.startswith('${') and value.endswith('}'):
                env_var = value[2:-1]
                return os.getenv(env_var)
            return value
        
        def traverse(obj: Dict) -> None:
            for key, value in obj.items():
                if isinstance(value, dict):
                    traverse(value)
                else:
                    obj[key] = resolve(value)
                    
        traverse(self._config)
        
    @property
    def database(self) -> Dict:
        return self._config['database']
    
    def paths(self) -> Dict:
        return self._config['paths']
    
    def transform(self) -> Dict:
        return self._config['transform']