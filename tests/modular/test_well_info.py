from preprocessing.modular.data import WellSpecsProcessor
from datetime import date


def test_well_info_well_specification_data():
    # Read files
    processor = WellSpecsProcessor("tests/files/cases/training/SIMULATION_2/SIMULATION_2.DATA")
    result = processor.process()

    # Test perforation keys
    assert result.get("perforation_keys") == ["k", "i", "j", "global_index", "tran"]

    # Test dates
    assert result.get("dates")[0] == date(2015, 4, 9)
    assert result.get("dates")[1] == date(2016, 4, 8)
    assert result.get("dates")[2] == date(2017, 4, 8)

    # Test well perforations
    well_perforations = result.get("wells").get("I1").get("perforations")
    assert well_perforations[0][0] == 0
    assert well_perforations[0][1] == 1
    assert well_perforations[0][2] == 1
    assert well_perforations[0][3] == 442
    assert well_perforations[0][4] == 0

    # Test well schedule
    ## I1 should be Closed in timestep 1
    assert result.get("wells").get("I1").get("schedule")[0][0] == False
    assert result.get("wells").get("P1").get("schedule")[0][0] == True

    ## I2 should be the same in timestep 2 as in timestep 1
    I2_schedule_t1 = result.get("wells").get("I2").get("schedule")[0][0]
    assert result.get("wells").get("I2").get("schedule")[0][1] == I2_schedule_t1
    ## All others should be closed in timestep 2
    assert result.get("wells").get("P1").get("schedule")[0][1] == False

    ## All well should be opened in timestep 3
    assert result.get("wells").get("P1").get("schedule")[0][2] == True
    assert result.get("wells").get("I1").get("schedule")[0][2] == True


def test_well_info_well_connection_data():
    # Read files
    processor = WellSpecsProcessor("tests/files/cases/training/SIMULATION_3/SIMULATION_3.DATA")
    result = processor.process()

    # Test perforation keys
    assert result.get("perforation_keys") == ["k", "i", "j", "global_index", "tran"]

    # Test dates
    dates = result.get("dates")
    assert dates[0] == date(1981, 12, 1)
    assert dates[1] == date(1982, 1, 1)
    assert dates[2] == date(1982, 2, 1)
    assert dates[3] == date(1982, 3, 1)
    assert dates[4] == date(1982, 4, 1)

    # Test well perforations
    assert result.get("wells").get("RB-007").get("perforations")[0] == [
        0,
        70,
        62,
        1883,
        0.000954877,
    ]

    # Test well schedule
    schedule = result.get("wells").get("RB-007").get("schedule")
    ## RB-007 1 and 3-5 should be opened in timestep 1
    assert schedule[0][1] == True
    assert schedule[3][1] == True
    ## RB-007 41 should be closed in timestep 1
    assert schedule[4][1] == False

    ## RB-007 1 should be the same in timestep 2 as in timestep 1
    RB_007_schedule_t1 = schedule[0][1]
    assert schedule[0][2] == RB_007_schedule_t1
    ## RB-007 3 should closed but 4 and 5 should be opened in timestep 2
    assert schedule[1][2] == False
    assert schedule[2][2] == True

    ## All well should be opened in timestep 3
    assert schedule[0][3] == True
    assert schedule[1][3] == True


def test_well_info_type():
    # Read files
    processor = WellSpecsProcessor("tests/files/cases/training/SIMULATION_4/SIMULATION_4.DATA")
    result = processor.process()

    # Test well producers and injectors
    assert result.get("wells").get("RB-007").get("well_type") == "PRODUCER"
    assert result.get("wells").get("RB-008").get("well_type") == "INJECTOR"
    assert result.get("wells").get("RB-008").get("well_phase") == "WAT"

    # Well 007 should be opened in timestep 1 and closed in timestep 2
    assert result.get("wells").get("RB-007").get("well_schedule")[0] == False
    assert result.get("wells").get("RB-007").get("well_schedule")[1] == True


def test_well_info_closed_well():
    # Read files
    processor = WellSpecsProcessor("tests/files/cases/training/SIMULATION_5/SIMULATION_5.DATA")
    result = processor.process()

    # Test open closed wells
    well_schedule = result.get("wells").get("A1").get("well_schedule")
    assert well_schedule[0] == False
    assert well_schedule[1] == True
    assert well_schedule[2] == True
    assert well_schedule[3] == True


def test_well_info_reference_depth():
    # Read files
    processor = WellSpecsProcessor("tests/files/cases/training/SIMULATION_5/SIMULATION_5.DATA")
    result = processor.process()

    # Test open closed wells
    assert result.get("wells").get("A1").get("reference_depth") == 29823.8712343609
    assert result.get("wells").get("I2").get("reference_depth") == 28748.0290932156
