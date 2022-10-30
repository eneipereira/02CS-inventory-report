from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __quantity_by_company(data):
        companies = dict()

        for dado in data:
            company = dado["nome_da_empresa"]

            if company not in companies:
                companies[company] = 1
            else:
                companies[company] += 1

        return companies

    @staticmethod
    def generate(data: "list[dict]"):
        simple_report = SimpleReport.generate(data)

        companies_dict = CompleteReport.__quantity_by_company(data)

        remaining_report = "Produtos estocados por empresa:\n"

        for (company, quantity) in companies_dict.items():
            remaining_report += f"- {company}: {quantity}\n"

        return f"{simple_report}\n" f"{remaining_report}"
