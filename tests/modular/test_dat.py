from preprocessing.modular.dat import preprocess as preprocess_dat_files


def test_grdecl_preprocessing_module():
    dat_files_loc = [
        "tests/files/PORO.dat",
        "tests/files/permx.dat",
        "tests/files/VCL.dat",
    ]
    mappings = [
        {"name": "PORO", "source": "PORO"},
        {"name": "PERMX", "source": "permx"},
        {"name": "V-CLAI", "source": "VCL"},
    ]

    dat_files = {}

    for keyword in mappings:
        file = next(filter(lambda file: keyword["source"] in file, dat_files_loc), None)
        if file:
            dat_files[keyword["name"]] = file

    props = preprocess_dat_files(dat_files, mappings)

    prop_keys = props.keys()
    goal = ["PORO", "PERMX", "V-CLAI"]
    assert all([x in goal for x in prop_keys])

    assert props["PORO"].shape[0] > 0
    assert props["PORO"].shape[1] == 5
    # The input files are the same except for the keyword, so it should match if well read
    assert props["PORO"].loc[:, "PORO"].eq(props["PERMX"].loc[:, "PERMX"]).all()
    assert props["PORO"].loc[:, "PORO"].eq(props["V-CLAI"].loc[:, "V-CLAI"]).all()
