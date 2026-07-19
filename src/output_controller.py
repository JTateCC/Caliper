import openpyxl

class OutputController:

    def __init__(self, dxf_list):
        self.dxf_list = dxf_list

    def to_excel(self, output_path):
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.append(
            ["document_id", "file_name", "file_path", "file_size", "date_created", "date_modified", "dxf_version"])
        for dxf in self.dxf_list:
            sheet.append([
                dxf.document_id,
                dxf.file_name,
                dxf.file_path,
                dxf.file_size,
                dxf.date_created,
                dxf.date_modified,
                dxf.dxf_version
            ])
        workbook.save(output_path)