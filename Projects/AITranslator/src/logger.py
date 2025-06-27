"""
Handles error logging for the translation process.
"""

import logging
import os

class Logger:
    """
    Logger for translation errors and issues.

    Attributes:
        log_file (str): Path to the log file.
    """

    def __init__(self, log_file='translation_errors.log', original_file_name=None):
        """
        Initialize the Logger and configure logging.

        Args:
            log_file (str): Path to the log file.
            original_file_name (str, optional): Name of the original file to prefix to the log file name (without extension).
        """

        if original_file_name:
            base, ext = os.path.splitext(log_file)
            file_base, _ = os.path.splitext(original_file_name)
            # Ensure log directory exists
            log_dir = os.path.dirname(base)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
            log_file = f"{file_base}_{os.path.basename(base)}{ext}"
            if log_dir:
                log_file = os.path.join(log_dir, log_file)
        else:
            # Ensure log directory exists for default log_file
            log_dir = os.path.dirname(log_file)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
        logging.basicConfig(filename=log_file, level=logging.ERROR, 
                            format='%(asctime)s %(levelname)s:%(message)s')
        self.log_file = log_file

    def log_error(self, key, value, language, error):
        """
        Log an error that occurred during translation.

        Args:
            key (str): The resource key that failed.
            value (str): The original value (not logged).
            language (str): The language attempted.
            error (str): The error message.
        """

        msg = f"Failed to translate key '{key}' to {language}: {error}"
        logging.error(msg)
