from preprocessing.modular.s import WellSummaryProcessor

from ecl.summary import EclSum


def test_well_info_well_specification_data():
    # Read files
    processor = WellSummaryProcessor("tests/files/cases/training/SIMULATION_4/SIMULATION_4")
    preprocessed, raw = processor.process()

    # Test summary raw
    assert ((raw.index >= "1981-12-01") & (raw.index <= "1982-04-01")).sum() == 10
    assert "WOPR:RB-007" in raw.columns

    # Test summary parsed
    assert preprocessed.iloc[0].at["WELL"] == "RB-007"
    assert preprocessed.iloc[5].at["WELL"] == "RB-008"

    assert preprocessed.iloc[0].at["WOPR"] == 0.0
    assert preprocessed.iloc[0].at["WWPR"] == 0.0
    assert preprocessed.iloc[0].at["WGPR"] == 0.0

    # Test wcon merge
    assert preprocessed.iloc[0].at["STATUS"] == "SHUT"
    assert preprocessed.iloc[1].at["STATUS"] == "OPEN"
    assert preprocessed.iloc[6].at["STATUS"] == "OPEN"
