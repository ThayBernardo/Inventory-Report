import csv
import json
import xml.etree.ElementTree as xml
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path: str, type: str):
        if "csv" in path:
            return cls.read_csv(path, type)
        elif "json" in path:
            return cls.read_json(path, type)
        elif "xml" in path:
            return cls.read_xml(path, type)

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

    @classmethod
    def read_xml(cls, path, type):
        file = xml.parse(path).getroot()
        dicionario = []
        for i in file.findall('record'):
            dict = {item.tag: item.text for item in i}
            dicionario.append(dict)
        if (type == "simples"):
            return SimpleReport.generate(dicionario)
        elif (type == "completo"):
            return CompleteReport.generate(dicionario)
