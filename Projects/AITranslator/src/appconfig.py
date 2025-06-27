"""
Handles application configuration loading from appconfig.ini.
Supports input/output paths, OpenAI API key/model, and log file path.
"""

import configparser
import os

class AppConfig:
    """
    Loads and stores application configuration from an INI file.
    Attributes:
        input_path (str): Directory containing input resource files.
        output_path (str): Directory to save translated files.
        api_key (str): OpenAI API key for translation.
        model (str): OpenAI model name.
        log_file (str): Path to the log file for errors.
    """
    def __init__(self, config_file='appconfig.ini'):
        """
        Initialize AppConfig and load settings from the given config file.
        Args:
            config_file (str): Path to the configuration file.
        """
        self.input_path = None
        self.output_path = None
        self.api_key = None
        self.model = 'gpt-4.1-turbo'
        self.log_file = 'translation_errors.log'
        self.base_url = None
        self._load(config_file)

    def _load(self, config_file):
        """
        Internal method to load configuration from the INI file.
        Args:
            config_file (str): Path to the configuration file.
        """
        config = configparser.ConfigParser()
        if os.path.exists(config_file):
            config.read(config_file)
            self.input_path = config.get('paths', 'input', fallback=None)
            self.output_path = config.get('paths', 'output', fallback=None)
            self.api_key = config.get('openai', 'api_key', fallback=None)
            self.model = config.get('openai', 'model', fallback='gpt-4.1-turbo')
            self.log_file = config.get('logging', 'log_file', fallback='translation_errors.log')
            self.base_url = config.get('openai', 'base_url', fallback=None)
