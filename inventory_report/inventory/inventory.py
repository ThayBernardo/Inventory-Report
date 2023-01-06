import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, type: str):
        if "csv" in path:
            return cls.read_csv(path, type)
        elif "json" in path:
            return cls.read_json(path, type)

    @classmethod
    def read_csv(cls, path, type):
        with open(path, encoding="utf-8") as file:
            reader = list(csv.DictReader(file))
            if (type == "simples"):
                return SimpleReport.generate(reader)
            elif (type == "completo"):
                return CompleteReport.generate(reader)

    @classmethod
    def read_json(cls, path, type):
        with open(path, encoding='utf-8') as file:
            reader = list(json.load(file))
            if (type == "simples"):
                return SimpleReport.generate(reader)
            elif (type == "completo"):
                return CompleteReport.generate(reader)
