from inventory_report.inventory.product import Product

PARAMS = [
    1,
    "Teste",
    "Empresa Fictícia",
    "2022-10-28",
    "2024-12-25",
    "123456789",
    "Guardar direitinho",
]


def test_cria_produto():
    new_product = Product(*PARAMS)

    assert new_product.id == PARAMS[0]
    assert new_product.nome_do_produto == PARAMS[1]
    assert new_product.nome_da_empresa == PARAMS[2]
    assert new_product.data_de_fabricacao == PARAMS[3]
    assert new_product.data_de_validade == PARAMS[4]
    assert new_product.numero_de_serie == PARAMS[5]
    assert new_product.instrucoes_de_armazenamento == PARAMS[6]
