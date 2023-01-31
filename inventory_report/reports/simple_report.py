import datetime
from typing import List, Dict


class SimpleReport:
    @staticmethod
    def generate(products_list: List[Dict]) -> str:
        now = datetime.datetime.now()

        manufacturing_dates = [
            product["data_de_fabricacao"] for product in products_list
        ]

        expiration_dates = [
            product["data_de_validade"]
            for product in products_list
            if product["data_de_validade"] > now.strftime("%Y-%m-%d")
        ]

        product_companies = [
            product["nome_da_empresa"] for product in products_list
        ]

        product_count_by_company = {
            f"{company}": product_companies.count(company)
            for company in product_companies
        }

        older_manufacturing_date = min(manufacturing_dates)
        closest_expiration_date = min(expiration_dates)
        most_products_company = max(
            product_count_by_company, key=product_count_by_company.get
        )

        return (
            f"Data de fabricação mais antiga: {older_manufacturing_date}\n"
            f"Data de validade mais próxima: {closest_expiration_date}\n"
            f"Empresa com mais produtos: {most_products_company}"
        )
