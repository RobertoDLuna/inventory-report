from inventory_report.importer.importer import Importer
import json
from typing import List, Dict


class JsonImporter(Importer):
    def import_data(path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            try:
                data = json.loads(file.read())
            except Exception:
                raise ValueError("Arquivo inválido")

            return list(data)
