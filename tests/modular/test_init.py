from ecl.grid import EclGrid
from ecl.eclfile import EclInitFile

from preprocessing.modular.init import preprocess as preprocess_init


def test_init_preprocessing_module():
    test_grid_location = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.EGRID"
    test_init_location = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.INIT"

    grid = EclGrid(test_grid_location)
    init = EclInitFile(grid, test_init_location)
    init_props = preprocess_init(init)
    prop_keys = init_props.keys()
    goal = [
        "permx",
        "permy",
        "permz",
        "tranx",
        "trany",
        "tranz",
        "dx",
        "dy",
        "dz",
        "depth",
        "ntg",
        "poro",
        "porv",
        "satnum",
        "pvtnum",
        "eqlnum",
        "rocknum",
    ]
    assert all([x in goal for x in prop_keys])
