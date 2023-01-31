import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, file_path, string_type):
        inventory_list = []
        with open(file_path, encoding="utf-8") as file:
            # fonte sobre o quotechar: https://realpython.com/python-csv/
            file_reader = csv.DictReader(file, delimiter=",", quotechar='"')

            for item in file_reader:
                inventory_list.append(item)

        if string_type == "simples":
            return SimpleReport.generate(inventory_list)

        if string_type == "completo":
            return CompleteReport.generate(inventory_list)
