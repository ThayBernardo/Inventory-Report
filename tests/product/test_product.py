from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "nome_produto",
        "nome_empresa",
        "data_de_fabricacao",
        "data_de_validade",
        "numero_de_serie",
        "instrucoes_de_armazenamento"
    )
    assert product.id == 1
    assert product.nome_do_produto == "nome_produto"
    assert product.nome_da_empresa == "nome_empresa"
    assert product.data_de_fabricacao == "data_de_fabricacao"
    assert product.data_de_validade == "data_de_validade"
    assert product.numero_de_serie == "numero_de_serie"
    assert product.instrucoes_de_armazenamento == "instrucoes_de_armazenamento"
