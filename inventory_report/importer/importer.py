# fonte: https://docs.python.org/3/library/abc.html
from abc import ABC


class Importer(ABC):
    @staticmethod
    def import_data(path: str):
        pass
