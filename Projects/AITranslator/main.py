"""
Main entry point for the resource translation tool.

This script reads configuration from appconfig.ini, processes all supported resource files in the input directory,
translates their values into multiple languages using the OpenAI GPT API, and writes the translated files to the output directory.
"""

import sys
import os
# Ensure src directory is in sys.path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import argparse
from src.appconfig import AppConfig
from src.resource_loader import ResourceLoader
from src.resx_handler import ResxHandler
from src.translator import Translator
from src.logger import Logger

LANGUAGES = [
    ('English', 'en'),
    ('German', 'de'),
    ('French', 'fr'),
    ('Italian', 'it'),
]

EXTENSIONS = ['.json', '.csv', '.xml', '.resx']

def parse_languages(langs_str):
    """
    Parse a comma-separated string of languages or language codes into a list of (name, code) tuples.
    Accepts either language names (case-insensitive) or codes (en, de, etc).
    """
    supported = {
        'english': 'en', 'en': 'en',
        'german': 'de', 'de': 'de',
        'french': 'fr', 'fr': 'fr',
        'italian': 'it', 'it': 'it',
    }
    result = []
    for lang in langs_str.split(','):
        lang = lang.strip().lower()
        if lang in supported:
            # Use canonical name for output file naming
            name = lang.capitalize() if len(lang) > 2 else {
                'en': 'English', 'de': 'German', 'fr': 'French', 'it': 'Italian'
            }[lang]
            code = supported[lang]
            result.append((name, code))
    return result

def process_file(input_path, output_path, file_name, translator, logger, languages):
    """
    Process a single resource file: load, translate, and save translations for each language.

    Args:
        input_path (str): Directory containing the input file.
        output_path (str): Directory to save translated files.
        file_name (str): Name of the file to process.
        translator (Translator): Translator instance for API calls.
        logger (Logger): Logger instance for error logging.
        languages (list): List of (name, code) tuples for target languages.
    """
    ext = os.path.splitext(file_name)[1].lower()
    file_path = os.path.join(input_path, file_name)
    if ext == '.resx':
        data = ResxHandler.load(file_path)
    else:
        data = ResourceLoader.load(file_path)
    language_names = [lang[0] for lang in languages]
    results = translator.batch_translate(data, language_names, logger)
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    for lang, code in languages:
        out_file = os.path.join(output_path, f"{base_name}_{code}{ext}")
        if ext == '.resx':
            ResxHandler.save(results[lang], file_path, out_file)
        else:
            ResourceLoader.save(results[lang], out_file)
        print(f"Saved: {out_file}")

def main():
    """
    Main function to parse arguments, load configuration, and process all supported files in the input directory.
    """
    parser = argparse.ArgumentParser(description='Resource Translator using AI Agent')
    parser.add_argument('--appconfig', default='appconfig.ini', help='App config for input/output paths and settings')
    parser.add_argument('--languages', default='English,German,French,Italian', help='Comma-separated list of languages or codes to translate to (e.g. "en,de,fr,it")')
    args = parser.parse_args()

    user_languages = parse_languages(args.languages)
    if not user_languages:
        print('No valid languages specified.')
        return

    app_config = AppConfig(args.appconfig)
    input_path = app_config.input_path
    output_path = app_config.output_path
    api_key = app_config.api_key
    model = app_config.model
    log_file = app_config.log_file
    base_url = app_config.base_url
    if not input_path or not output_path:
        print('Input or output path not set in appconfig.ini')
        return

    if not os.path.isdir(input_path):
        print(f'Input path {input_path} is not a directory.')
        return

    translator = Translator(api_key, model, prompt_config_file='promptconfig.ini', base_url=base_url)

    for file_name in os.listdir(input_path):
        ext = os.path.splitext(file_name)[1].lower()
        if ext in EXTENSIONS:
            logger = Logger(log_file, file_name)
            process_file(input_path, output_path, file_name, translator, logger, user_languages)

if __name__ == '__main__':   
    main()
