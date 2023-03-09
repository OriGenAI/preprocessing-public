import os

from preprocessing.deck.section import scan_file, find_includes, find_section


def test_scan_file():
    data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    header = "RUNSPEC"
    with open(data_file_loc, "r") as f:
        content = f.read()
    result = scan_file(content, header)
    good_result = """

TITLE
 SIMPLE 2PH MODEL WITH SINGLE FAULT AND LGR

DIMENS
    20  20  10 / 

METRIC

OIL

WATER

TABDIMS
    2*    24 2*    20    20 1*     1 7* /
EQLDIMS
    2* 100 2* /
REGDIMS
    6* /
WELLDIMS
       12   100     4    12     0     0     0     0     0     0     0     0 /

TRACERS
-- NOTRAC NWTRAC NGTRAC NETRAC Diff/NODiff
      0      2     0     0      'DIFF' /

ENDSCALE
/

NSTACK
  25 /
START
9 APR 2015 /


MULTOUT

"""

    assert good_result == result.group("content")


def test_find_includes():
    data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    with open(data_file_loc, "r") as f:
        content = f.read()
    abs_path = os.path.abspath(data_file_loc)
    result = find_includes(content, abs_path)
    good_list = [f"{os.getcwd()}/tests/files/cases/include/SHIFTTOP.GRDECL"]
    assert good_list == result


def test_find_section():
    data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    section = find_section(data_file_loc, "RUNSPEC")
    good_result = """

TITLE
 SIMPLE 2PH MODEL WITH SINGLE FAULT AND LGR

DIMENS
    20  20  10 / 

METRIC

OIL

WATER

TABDIMS
    2*    24 2*    20    20 1*     1 7* /
EQLDIMS
    2* 100 2* /
REGDIMS
    6* /
WELLDIMS
       12   100     4    12     0     0     0     0     0     0     0     0 /

TRACERS
-- NOTRAC NWTRAC NGTRAC NETRAC Diff/NODiff
      0      2     0     0      'DIFF' /

ENDSCALE
/

NSTACK
  25 /
START
9 APR 2015 /


MULTOUT

"""
    assert section == good_result


def test_find_section_with_download_func():
    data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    section_header = "RUNSPEC"
    test_path = "tests/files/cases/training/SIMULATION_1/my_file"

    def download_func(relative_path, actual_path):
        open(test_path, "a").close()

    find_section(data_file_loc, section_header, download_func)

    assert os.path.exists(test_path)

    os.remove(test_path)
    assert not os.path.exists(test_path)
