from inventory_report.inventory.product import Product


PARAMS = [
    1,
    "Teste",
    "Empresa Fictícia",
    "2022-10-28",
    "2024-12-25",
    "123456789",
    "corretamente"
    ]

REPORT_PHRASE = (
    "O produto Teste fabricado em 2022-10-28 por Empresa Fictícia "
    "com validade até 2024-12-25 precisa ser armazenado corretamente."
    )


def test_relatorio_produto():
    new_product = Product(*PARAMS)

    assert str(new_product) == REPORT_PHRASE
