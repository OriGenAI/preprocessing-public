import cwrap

from preprocessing.modular.grdecl import preprocess as preprocess_grdecl


def test_grdecl_preprocessing_module():
    test_grdecl_location = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.GRDECL"
    mappings = [
        {"name": "ACTNUM", "source": "BOOLEAN"},
        {"name": "LITHO", "source": "LITHO"},
    ]
    with cwrap.open(test_grdecl_location, "r") as f:
        props = preprocess_grdecl(f, mappings)

    prop_keys = props.keys()
    goal = ["litho", "actnum"]
    assert all([x in goal for x in prop_keys])
