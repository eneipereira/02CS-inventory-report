import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def __csv_reader(path):
        with open(path, "r") as file:
            companies_reader = csv.DictReader(file)
            csv_data = list(companies_reader)

            return csv_data

    @staticmethod
    def import_data(path: str, type="completo"):
        companies_data = Inventory.__csv_reader(path)

        if type == "simples":
            return SimpleReport.generate(companies_data)

        return CompleteReport.generate(companies_data)
