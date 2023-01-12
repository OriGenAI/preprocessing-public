from ecl.grid import EclGrid

from preprocessing.modular.egrid import preprocess as preprocess_egrid


def test_egrid_preprocessing_module():
    test_file_location = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.EGRID"
    grid = EclGrid(test_file_location)
    egrid_props = preprocess_egrid(grid)
    logic = egrid_props["actnum"]
    assert len(logic) == 4000 and len(logic[logic == 0]) == 0
