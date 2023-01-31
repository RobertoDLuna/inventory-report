import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_data(self, file_path, string_type):
        inventory_list = []
        if "csv" in file_path:
            with open(file_path, encoding="utf-8") as file:
                # fonte sobre o quotechar: https://realpython.com/python-csv/
                file_reader = csv.DictReader(
                    file, delimiter=",", quotechar='"'
                )

                for item in file_reader:
                    inventory_list.append(item)

        if "json" in file_path:
            with open(file_path) as file:
                content = file.read()
                inventory_list = json.loads(content)

        if "xml" in file_path:
            with open(file_path) as file:
                file_reader = xmltodict.parse(file.read())
                inventory_list = file_reader["dataset"]["record"]

        if string_type == "simples":

            return SimpleReport.generate(inventory_list)

        else:

            return CompleteReport.generate(inventory_list)
