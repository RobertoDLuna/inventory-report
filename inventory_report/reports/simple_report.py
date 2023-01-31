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


# from collections import Counter


# class SimpleReport:
#     def get_oldest_date(self, stock):
#         oldest_date = stock[0]["data_de_fabricacao"]

#         for product in stock:
#             if oldest_date > product["data_de_fabricacao"]:
#                 oldest_date = product["data_de_fabricacao"]

#         return oldest_date

#     def get_closest_date(self, stock):
#         closest_date = stock[0]["data_de_validade"]

#         for product in stock:
#             if closest_date > product["data_de_validade"]:
#                 closest_date = product["data_de_validade"]

#         return closest_date

#     # Fonte : https://realpython.com/python-counter;
#     def get_company(self, stock):
#         count_companies = list()

#         for product in stock:
#             count_companies.append(product["nome_da_empresa"])

#         counter = Counter(count_companies)
#         # fonte: https://docs.python.org/3/library/functions.html
#         find_company = max(counter, key=counter.get)

#         return find_company

#     @classmethod
#     def generate(self, stock):
#         oldest = self.get_oldest_date(self, stock)
#         closest = self.get_closest_date(self, stock)
#         company = self.get_company(self, stock)

#         return (
#             f"Data de fabricação mais antiga: {oldest}\n"
#             f"Data de validade mais próxima: {closest}\n"
#             f"Empresa com mais produtos: {company}"
#         )
