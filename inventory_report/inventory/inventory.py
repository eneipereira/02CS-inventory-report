from pathlib import Path
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type="completo"):
        file_ext = Path(path).suffix
        inventory = []

        if file_ext == ".csv":
            inventory = CsvImporter.import_data(path)

        elif file_ext == ".json":
            inventory = JsonImporter.import_data(path)

        elif file_ext == ".xml":
            inventory = XmlImporter.import_data(path)

        if type == "simples":
            return SimpleReport.generate(inventory)

        return CompleteReport.generate(inventory)
