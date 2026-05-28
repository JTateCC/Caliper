import os
import hashlib
from datetime import datetime

import ezdxf
class CaliperDxfModel:

    def __init__(self, file_path):
        self.file_path = file_path
        self.document_id = hashlib.md5(file_path.encode()).hexdigest()
        self.file_name = os.path.basename(file_path)
        self.date_created = None  # filesystem
        self.date_modified = None  # filesystem
        self.file_size = None  # in bytes
        self.dxf_version = None  # e.g. AC1015 = AutoCAD 2000
        self.header_vars = None
        self.custom_vars = None

    def load(self):
        self._load_filesystem_metadata()
        self._load_dxf_header()

    def _load_filesystem_metadata(self):
        stats = os.stat(self.file_path)
        self.date_created = datetime.fromtimestamp(stats.st_ctime)
        self.date_modified = datetime.fromtimestamp(stats.st_mtime)
        self.file_size = stats.st_size

    def _load_dxf_header(self):
        doc = ezdxf.readfile(self.file_path)
        self.dxf_version = doc.dxfversion
        self.header_vars = dict(doc.header)
        self.custom_vars = {name: value for name, value in doc.header.custom_vars}

