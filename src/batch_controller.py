import os
from src.caliper_dxf_model import CaliperDxfModel


class BatchController:

    def __init__(self, directory):
        self.directory = directory
        self.caliper_dxf_list = []

    def build_dxf_models(self):
        for root, dirs, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.dxf'):
                    caliper_dxf =  CaliperDxfModel(os.path.join(root, file))
                    caliper_dxf.load()
                    self.caliper_dxf_list.append(caliper_dxf)

