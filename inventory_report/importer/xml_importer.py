from xml.etree import ElementTree as ET
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        tree = ET.parse(path)

        root = tree.getroot()

        xml_data = [
            {subtag.tag: subtag.text for subtag in tag}
            for tag in root
        ]

        return xml_data
