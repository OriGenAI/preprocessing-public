import numpy as np
from preprocessing.deck.runspec import (
    preprocess_phases,
    preprocess_start,
    preprocess_dimens,
    preprocess,
)
from ecl2df import EclFiles
from datetime import datetime


data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
data = EclFiles(data_file_loc)
ecldeck = data.get_ecldeck()

runspec_section = """

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

GRID    """


def test_phases():
    phases = preprocess_phases(ecldeck)
    assert phases["water"] == True
    assert phases["gas"] == False
    assert phases["oil"] == True


def test_start():
    start = preprocess_start(ecldeck)
    assert start == datetime(2015, 4, 9)


def test_dimens():
    dimens = preprocess_dimens(ecldeck)
    assert np.all([np.array([20, 20, 10]), dimens])


def test_all():
    data_file_loc = "tests/files/cases/training/SIMULATION_1/SIMULATION_1.DATA"
    contents = preprocess(data_file_loc)
    phases = contents["phases"]
    dimens = contents["dimens"]
    assert phases["water"] == True and phases["gas"] == False and phases["oil"] == True
    assert contents["start"] == datetime(2015, 4, 9)
    assert contents["endscale"] == True
    assert contents["multout"] == True
    assert np.all([np.array([20, 20, 10]), dimens])
