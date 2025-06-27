"""
Handles loading of translation prompt from a config file.
"""
import configparser
import os

class PromptConfig:
    """
    Loads and stores the translation prompt template from an INI file.
    Attributes:
        prompt_template (str): The prompt template string with placeholders.
    """
    def __init__(self, config_file='promptconfig.ini'):
        """
        Initialize PromptConfig and load the prompt template from the given config file.
        Args:
            config_file (str): Path to the prompt configuration file.
        """
        self.prompt_template = None
        self._load(config_file)

    def _load(self, config_file):
        """
        Internal method to load the prompt template from the INI file.
        Args:
            config_file (str): Path to the prompt configuration file.
        """
        config = configparser.ConfigParser()
        if os.path.exists(config_file):
            config.read(config_file)
            self.prompt_template = config.get('prompt', 'translation', fallback=None)
