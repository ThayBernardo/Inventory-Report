from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):

    def generate(list: list):
        simple_report = SimpleReport.generate(list)

        quantidade_empresa = Counter(
            [empresa["nome_da_empresa"] for empresa in list]
        )

        empresas = ""

        for key, value in quantidade_empresa.items():
            empresas += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{empresas}"
        )
