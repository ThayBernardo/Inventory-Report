from typing import List, Dict
from datetime import date, datetime
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(products: List[dict]) -> List[Dict]:

        frab_antiga = date.fromisoformat(products[0]["data_de_fabricacao"])
        datas = []
        empresas = []
        for product in products:
            empresas.append(product["nome_da_empresa"])

            date_today = datetime.today().strftime('%Y-%m-%d')

            if (
                frab_antiga > date.fromisoformat(product["data_de_fabricacao"])
            ):
                frab_antiga = date.fromisoformat(product["data_de_fabricacao"])

            if (
                date.fromisoformat(date_today)
                <= date.fromisoformat(product["data_de_validade"])
            ):
                datas.append(date.fromisoformat(product["data_de_validade"]))

        min_data = min(datas)
        contagem = Counter(empresas).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {date.isoformat(frab_antiga)}\n"
            f"Data de validade mais próxima: {date.isoformat(min_data)}\n"
            f"Empresa com mais produtos: {contagem}"
            )

# MIN / today
# def remove_repetidos(lista):
#     emp = []
#     for i in lista:
#         if i not in emp:
#             emp.append(i)
#     emp.sort()
#     return emp
# empresas_unicas = remove_repetidos(empresas)

# valor = 0
# for unic in empresas_unicas:
#     conta_empresa = empresas.count(unic)
#     if conta_empresa > valor:
#         valor = conta_empresa