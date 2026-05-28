from src.caliper_dxf_model import CaliperDxfModel

model = CaliperDxfModel(r"C:\Programming\Projects\Caliper\tests\testFiles\diamond.dxf")
model.load()
print(model.__dict__)