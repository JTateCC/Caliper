import os
class CaliperDxfModel:

    def __init__(self, document_id, file_path):
        self.document_id = document_id
        self.file_path = file_path
        self.file_name = os.path.basename(file_path)
        self.date_created = None  # filesystem
        self.date_modified = None  # filesystem
        self.file_size = None  # in bytes
        self.dxf_version = None  # e.g. AC1015 = AutoCAD 2000
        self.header_data = {}
