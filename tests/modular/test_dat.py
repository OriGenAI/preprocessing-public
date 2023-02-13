from preprocessing.modular.dat import preprocess as preprocess_dat_files


def test_grdecl_preprocessing_module():
    dat_files_loc = [
        "tests/files/poro.dat",
        "tests/files/vcl.dat",
        "tests/files/perm.dat",
    ]
    mappings = [
        {"name": "PORO", "source": "PORO"},
        {"name": "PERMX", "source": "PERM"},
        {"name": "V-CLAI", "source": "VCL"},
    ]

    dat_files = {}

    for keyword in mappings:
        file = next(filter(lambda file: keyword["source"].lower() in file, dat_files_loc), None)
        if file:
            dat_files[keyword["name"].lower()] = file

    props = preprocess_dat_files(dat_files, mappings)

    prop_keys = props.keys()
    goal = ["poro", "permx", "v-clai"]
    assert all([x in goal for x in prop_keys])

    assert props["poro"].shape[0] > 0
    assert props["poro"].shape[1] == 5
    # The input files are the same except for the keyword, so it should match if well read
    assert props["poro"].loc[:, "poro"].eq(props["permx"].loc[:, "permx"]).all()
    assert props["poro"].loc[:, "poro"].eq(props["v-clai"].loc[:, "v-clai"]).all()
