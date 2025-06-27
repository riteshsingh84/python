"""
Handles translation of resource values using the OpenAI GPT API (openai>=1.0.0).
"""

import openai
import time
from typing import Dict, List, Tuple
from prompt_config import PromptConfig

class Translator:
    """
    Handles translation of text using the OpenAI GPT API.

    Attributes:
        model (str): The OpenAI model to use for translation.
        prompt_template (str): The prompt template to use for translation.
    """

    def __init__(self, api_key: str, model: str = 'gpt-4.1-turbo', prompt_config_file: str = 'promptconfig.ini', base_url: str = None):
        """
        Initialize the Translator with API key, model, prompt template, and base_url.

        Args:
            api_key (str): OpenAI API key.
            model (str): Model name to use for translation.
            prompt_config_file (str): Path to the prompt config file.
            base_url (str): Base URL for the OpenAI API (for custom endpoints).
        """
        if base_url:
            self.client = openai.OpenAI(api_key=api_key, base_url=base_url)
        else:
            self.client = openai.OpenAI(api_key=api_key)
        self.model = model
        self.prompt_template = PromptConfig(prompt_config_file).prompt_template

    def translate(self, text: str, target_language: str) -> str:
        """
        Translate a single text string to the target language using GPT API.

        Args:
            text (str): The text to translate.
            target_language (str): The language to translate to.

        Returns:
            str: The translated text.

        Raises:
            RuntimeError: If the API call fails.
        """
        prompt = self.prompt_template.format(target_language=target_language, text=text)
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=512
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"API error: {e}")

    def batch_translate(self, data: Dict[str, str], languages: List[str], logger) -> Dict[str, Dict[str, str]]:
        """
        Translate all values in a dictionary to multiple languages.

        Args:
            data (Dict[str, str]): Key-value pairs to translate.
            languages (List[str]): List of language names to translate to.
            logger (Logger): Logger instance for error logging.

        Returns:
            Dict[str, Dict[str, str]]: Nested dict with language as key and translated key-value pairs as value.
        """
        results = {lang: {} for lang in languages}
        for key, value in data.items():
            for lang in languages:
                try:
                    translation = self.translate(value, lang)
                    results[lang][key] = translation
                except Exception as e:
                    logger.log_error(key, value, lang, str(e))
                    results[lang][key] = value  # fallback to original
                    time.sleep(2)  # avoid rate limit
        return results
