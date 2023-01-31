from collections import Counter


class SimpleReport:
    def get_oldest_date(self, stock):
        oldest_date = stock[0]["data_de_fabricacao"]

        for product in stock:
            if oldest_date > product["data_de_fabricacao"]:
                oldest_date = product["data_de_fabricacao"]

        return oldest_date

    def get_closest_date(self, stock):
        closest_date = stock[0]["data_de_validade"]

        for product in stock:
            if closest_date > product["data_de_validade"]:
                closest_date = product["data_de_validade"]

        return closest_date

    # Fonte : https://realpython.com/python-counter;
    def get_company(self, stock):
        count_companies = list()

        for product in stock:
            count_companies.append(product["nome_da_empresa"])

        counter = Counter(count_companies)
        # fonte: https://docs.python.org/3/library/functions.html
        find_company = max(counter, key=counter.get)

        return find_company

    @classmethod
    def generate(self, stock):
        oldest = self.get_oldest_date(self, stock)
        closest = self.get_closest_date(self, stock)
        company = self.get_company(self, stock)

        return (
            f"Data de fabricação mais antiga: {oldest}\n"
            f"Data de validade mais próxima: {closest}\n"
            f"Empresa com mais produtos: {company}"
        )
