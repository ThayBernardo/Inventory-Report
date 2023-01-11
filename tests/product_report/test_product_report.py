from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = [
        2,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "A6B7C8",
        "ao abrigo de luz"
    ]

    instance_product = Product(
        id=product[0],
        nome_do_produto=product[1],
        nome_da_empresa=product[2],
        data_de_fabricacao=product[3],
        data_de_validade=product[4],
        numero_de_serie=product[5],
        instrucoes_de_armazenamento=product[6]
    )

    assert instance_product.__repr__() == (
        f"O produto {product[1]}"
        f" fabricado em {product[3]}"
        f" por {product[2]} com validade"
        f" até {product[4]}"
        f" precisa ser armazenado {product[6]}."
    )
