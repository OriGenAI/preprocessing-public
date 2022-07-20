from preprocessing.deck.ecl_deck import extract_pvt, extract_relperm, preprocess

def test_pvt():
    test_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    
    pvt = extract_pvt(test_loc)
    # test oil and water density as an example
    assert 900 == pvt["OILDENSITY"][0]
    assert 1000 == pvt["WATERDENSITY"][0]

def test_relperm():
    test_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    
    relperm = extract_relperm(test_loc)
    sw_example = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9]
    krw_example = [0, 0.002, 0.0078, 0.0176, 0.0313, 0.0488, 0.0703, 0.0957, 0.125, 0.1582, 0.1953, 0.2363, 0.2813, 0.3301, 0.3828, 0.4395, 0.5]
    assert sw_example == relperm["SW"].tolist()
    assert krw_example == relperm["KRW"].tolist()
