"""
Handles loading and saving of resource files in JSON, CSV, XML, and RESX formats.
"""

import json
import csv
import xml.etree.ElementTree as ET
from typing import Dict

class ResourceLoader:
    """
    Utility class for loading and saving resource files in various formats.
    Supported formats: .json, .csv, .xml, .resx (load only).
    """
    @staticmethod
    def load(file_path: str) -> Dict[str, str]:
        """
        Load key-value pairs from a resource file.
        Args:
            file_path (str): Path to the resource file.
        Returns:
            Dict[str, str]: Dictionary of key-value pairs.
        Raises:
            ValueError: If the file format is unsupported.
        """
        if file_path.endswith('.json'):
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        elif file_path.endswith('.csv'):
            data = {}
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if len(row) >= 2:
                        data[row[0]] = row[1]
            return data
        elif file_path.endswith('.xml'):
            tree = ET.parse(file_path)
            root = tree.getroot()
            data = {}
            for child in root:
                data[child.tag] = child.text or ''
            return data
        elif file_path.endswith('.resx'):
            from src.resx_handler import ResxHandler
            return ResxHandler.load(file_path)
        else:
            raise ValueError('Unsupported file format.')

    @staticmethod
    def save(data: Dict[str, str], file_path: str):
        """
        Save key-value pairs to a resource file.
        Args:
            data (Dict[str, str]): Dictionary of key-value pairs.
            file_path (str): Path to the output file.
        Raises:
            ValueError: If the file format is unsupported.
            NotImplementedError: If trying to save .resx (should use ResxHandler.save).
        """
        if file_path.endswith('.json'):
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        elif file_path.endswith('.csv'):
            with open(file_path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                for k, v in data.items():
                    writer.writerow([k, v])
        elif file_path.endswith('.xml'):
            root = ET.Element('resources')
            for k, v in data.items():
                child = ET.SubElement(root, k)
                child.text = v
            tree = ET.ElementTree(root)
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
        elif file_path.endswith('.resx'):
            from src.resx_handler import ResxHandler
            # For .resx, need template path, so this should be handled in main
            raise NotImplementedError('Use ResxHandler.save for .resx files.')
        else:
            raise ValueError('Unsupported file format.')
