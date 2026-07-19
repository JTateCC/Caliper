from src.batch_controller import BatchController
from src.output_controller import OutputController

def main():
    batch_controller = BatchController('tests\\testFiles')
    batch_controller.build_dxf_models()
    output_controller = OutputController(batch_controller.caliper_dxf_list)
    output_controller.to_excel('tests\\myoutput.xlsx')

if __name__ == "__main__":
    main()