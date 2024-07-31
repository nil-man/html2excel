from openpyxl import Workbook


class BaseWorkbookParser:
    def __init__(self, file_path):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.file_path = file_path

