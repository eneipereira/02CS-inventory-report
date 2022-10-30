import sys
from pathlib import Path
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def main():
    args = sys.argv

    if len(args) < 3:
        print("Verifique os argumentos", file=sys.stderr)
        return

    _, path, file_type = args

    file_ext = Path(path).suffix

    if file_ext == '.csv':
        importer = CsvImporter
    elif file_ext == '.json':
        importer = JsonImporter
    else:
        importer = XmlImporter

    inventory = InventoryRefactor(importer)
    report = inventory.import_data(path, file_type)

    return print(report, end="")
