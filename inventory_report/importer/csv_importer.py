import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path, "r") as file:
            companies_reader = csv.DictReader(file)
            csv_data = list(companies_reader)

            return csv_data
