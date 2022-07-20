from ecl.eclfile import EclFile

from preprocessing.modular.x import preprocess as preprocess_x


def test_x_preprocessing_module():
    test_x_location = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.X0000"

    rst = EclFile(test_x_location)
    init_props = preprocess_x(rst)
    prop_keys = init_props.keys()
    goal = ["pressure", "swat"]
    assert all([x in goal for x in prop_keys])
