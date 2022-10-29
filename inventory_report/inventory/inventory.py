import csv
import json
from pathlib import Path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __csv_reader(path):
        with open(path, "r") as file:
            companies_reader = csv.DictReader(file)
            csv_data = list(companies_reader)

            return csv_data

    def __json_reader(path):
        with open(path) as file:
            json_data = json.load(file)

            return json_data

    @staticmethod
    def import_data(path: str, type="completo"):
        file_ext = Path(path).suffix
        companies_data = []

        if file_ext == '.csv':
            companies_data = Inventory.__csv_reader(path)

        elif file_ext == '.json':
            companies_data = Inventory.__json_reader(path)

        if type == "simples":
            return SimpleReport.generate(companies_data)

        return CompleteReport.generate(companies_data)
