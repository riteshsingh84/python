"""
Handles loading and saving of .resx resource files for translation.
"""

import xml.etree.ElementTree as ET
from typing import Dict

class ResxHandler:
    """
    Utility class for loading and saving .resx resource files.
    """
    @staticmethod
    def load(file_path: str) -> Dict[str, str]:
        """
        Load key-value pairs from a .resx file.
        Args:
            file_path (str): Path to the .resx file.
        Returns:
            Dict[str, str]: Dictionary of key-value pairs.
        """
        tree = ET.parse(file_path)
        root = tree.getroot()
        namespace = {'resx': 'http://www.w3.org/2005/05/xmlmime'}
        data = {}
        for data_elem in root.findall('data'):
            key = data_elem.get('name')
            value_elem = data_elem.find('value')
            if key and value_elem is not None:
                data[key] = value_elem.text or ''
        return data

    @staticmethod
    def save(data: Dict[str, str], template_path: str, file_path: str):
        """
        Save key-value pairs to a .resx file, preserving the original structure.
        Args:
            data (Dict[str, str]): Dictionary of key-value pairs.
            template_path (str): Path to the original .resx file (used as template).
            file_path (str): Path to the output .resx file.
        """
        tree = ET.parse(template_path)
        root = tree.getroot()
        for data_elem in root.findall('data'):
            key = data_elem.get('name')
            if key in data:
                value_elem = data_elem.find('value')
                if value_elem is not None:
                    value_elem.text = data[key]
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
