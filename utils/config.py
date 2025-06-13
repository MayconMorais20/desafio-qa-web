from dotenv import load_dotenv
import os

class Config:
    load_dotenv()  # Load environment variables from .env file

    @staticmethod
    def get_env_variable(var_name):
        """Get the environment variable or raise an exception."""
        try:
            return os.environ[var_name]
        except KeyError:
            raise Exception(f"Missing environment variable: {var_name}")

    @staticmethod
    def get_driver_path():
        """Get the path for the WebDriver."""
        return Config.get_env_variable('WEBDRIVER_PATH')

    @staticmethod
    def get_base_url():
        """Get the base URL for the application."""
        return Config.get_env_variable('BASE_URL')