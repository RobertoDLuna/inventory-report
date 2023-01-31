from inventory_report.reports.simple_report import SimpleReport
from typing import List, Dict


class CompleteReport:
    @classmethod
    def generate(cls, products_list: List[Dict]) -> str:
        simple_report = SimpleReport.generate(products_list)
        company_inventory = cls.generate_company_inventory(products_list)

        return simple_report + company_inventory

    @classmethod
    def generate_company_inventory(cls, products_list: List[Dict]) -> str:
        product_companies = [
            product["nome_da_empresa"] for product in products_list
        ]

        inventory_by_company = {
            f"{company}": product_companies.count(company)
            for company in product_companies
        }

        return cls.generate_inventory_string(inventory_by_company)

    @staticmethod
    def generate_inventory_string(inventory_by_company_dict: Dict) -> str:
        string = "\nProdutos estocados por empresa:\n"

        for company, product_count in inventory_by_company_dict.items():
            string += f"- {company}: {product_count}\n"

        return string


# from collections import Counter
# from inventory_report.reports.simple_report import SimpleReport


# class CompleteReport:
#     def get_products_quantity_by_company(self, stock):
#         count_companies = list()
#         final_string = ""

#         for product in stock:
#             count_companies.append(product["nome_da_empresa"])

#         # Fontes: https://note.nkmk.me/en/python-collections-counter/
#         # https://www.delftstack.com/howto/python/python-counter-most-common/
#         most_common_company = Counter(count_companies).most_common()

#         for product, quantity in most_common_company:
#             final_string += f"- {product}: {quantity}\n"

#         return final_string

#     @classmethod
#     def generate(self, stock):
#         report = SimpleReport.generate(stock)
#         products_list = self.get_products_quantity_by_company(self, stock)

#         return (
#             f"{report}\n"
#             f"Produtos estocados por empresa:\n"
#             f"{products_list}"
#         )
