from inventory_report.importer.importer import Importer
from typing import List, Dict
import xmltodict


class XmlImporter(Importer):
    def import_data(path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            try:
                data = xmltodict.parse(file.read())["dataset"]["record"]
            except Exception:
                raise ValueError("Arquivo inválido")

            return list(data)
