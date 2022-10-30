from collections import Counter
from datetime import datetime


class SimpleReport:
    def __manufacturing_date(data):
        manufacturing_date_list = [dado["data_de_fabricacao"] for dado in data]

        return manufacturing_date_list

    def __expiration_date(data):
        today = datetime.today().date().isoformat()

        expiration_date_list = [
            dado["data_de_validade"]
            for dado in data
            if dado["data_de_validade"] >= today
        ]

        return expiration_date_list

    def __company_name(data):
        company_name_list = [dado["nome_da_empresa"] for dado in data]

        return company_name_list

    @staticmethod
    def generate(data: "list[dict]"):
        oldest_date = min(SimpleReport.__manufacturing_date(data))
        closest_date = min(SimpleReport.__expiration_date(data))
        most_common_company = Counter(
            SimpleReport.__company_name(data)
        ).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {closest_date}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
