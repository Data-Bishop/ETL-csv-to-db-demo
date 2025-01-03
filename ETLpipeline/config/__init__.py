from .config import Config

# Create a default Config instance with the standard configurations
config = Config()

# Expose the Config class and the default instance
__all__ = ["Config", "config"]