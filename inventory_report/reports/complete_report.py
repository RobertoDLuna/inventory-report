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
