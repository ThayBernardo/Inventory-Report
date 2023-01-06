import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, type: str):
        if "csv" in path:
            with open(path, encoding="utf-8") as file:
                reader = list(csv.DictReader(file))
            if (type == "simples"):
                return SimpleReport.generate(reader)
            elif (type == "completo"):
                return CompleteReport.generate(reader)
