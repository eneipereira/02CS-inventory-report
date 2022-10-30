from inventory_report.reports.colored_report import ColoredReport
from inventory_report.inventory.inventory import SimpleReport
import pytest
from faker import Faker
from tests.factories.product_factory import ProductFactory
from datetime import datetime, timedelta

faker = Faker("pt-BR")

old_date = faker.past_date()
future_date = faker.future_date() + timedelta(days=20)

oldest_date = old_date - timedelta(days=30)
closest_date = datetime.today().date() + timedelta(days=10)
company_bigger_stock = faker.company()


@pytest.fixture
def stock():
    return [
        vars(
            ProductFactory(
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                nome_da_empresa=company_bigger_stock,
                data_de_fabricacao=str(old_date),
                data_de_validade=str(future_date),
            )
        ),
        vars(
            ProductFactory(
                data_de_fabricacao=str(oldest_date),
                data_de_validade=str(closest_date),
            )
        ),
    ]


GREEN = [
    "\033[32mData de fabricação mais antiga:\033[0m",
    "\033[32mData de validade mais próxima:\033[0m",
    "\033[32mEmpresa com mais produtos:\033[0m",
]

BLUE = [
    f"\033[36m{oldest_date}\033[0m",
    f"\033[36m{closest_date}\033[0m"
]

RED = f"\033[31m{company_bigger_stock}\033[0m"


def test_decorar_relatorio(stock):
    report = ColoredReport(SimpleReport).generate(stock)

    for each_green in GREEN:
        assert each_green in report

    for each_blue in BLUE:
        assert each_blue in report

    assert RED in report
