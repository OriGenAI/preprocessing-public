import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False

    LOG_LOC = "logs"

    WELL_SETTINGS = "configs/group_well_info.yml"
    
    HM_WATER_INJ_CONTROLS = ["WWIRH"]
    HM_GAS_INJ_CONTROLS = ["WBHPH"]
    HM_PROD_CONTROLS = ["WBHPH", "WPRH", "WOPRH", "WGPRH"]

    FDP_GAS_INJ_CONTROLS = ["WBHP"]
    FDP_WATER_INJ_CONTROLS = ["WWIR"]
    FDP_PROD_CONTROLS = ["WBHP", "WOPR", "WWPR", "WGPR"]

    PREPROCESSING_VERSION = 0.1
    ## Well related elements (in INTEHEAD keyword)
    INTHEAD_KEYWORD_ELEMENTS = {
        # Number of wells
        "NWELLS": 16,
        # Maximum number of grid blocks connections per well
        "NCWMAX": 17,
        # Maximum number of wells belonging to a group in the model
        "NWGMAX": 19,
        # Number of values per well in the IWEL array
        "NIWELZ": 24,
        # Number of values per well in the SWEL array
        "NSWELZ": 25,
        # Number of values per well in the XWEL array
        "NXWELZ": 26,
        # Number of eight character words per well in the ZWEL array
        "NZWELZ": 27,
        # Maximum number of wells in the mdoel
        "NWMAXZ": 163,
        # Number of multi-segmented wells defined with the WELSEG keyword in the SCHEDULE section
        # for when multi-segment wells have been activated, or zero otherwise
        "NSEGWL": 174,
        # Maximum number of segments per multi-segment well,
        # for when multi-segment wells have been activated, or zero otherwise
        "NSWLMX": 175,
        # Maximum number of branches per multi-segment well, including the main branch groups for the model
        # for when multi-segment wells have been activated, or zero otherwise
        "NSEGMX": 176,
        # Number of entries per segment in the multi-segment well ISEG array,
        # for when multi-segment wells have been activated, or zero otherwise
        "NLBRMX": 177,
        # Number of entries per segment in the multi-segment well ISEG array,
        # for when multi-segment wells have been activated, or zero otherwise
        "NISEGZ": 178,
        # Number of entries per segment in the multi-segment well RSEG array,
        # for when multi-segment wells have been activated, or zero otherwise
        "NRSEGZ": 179,
        # Number of entries per segment in the multi-segment well ILBR array,
        # for when multi-segment wells have been activated, or zero otherwise
        "NILBRZ": 180
    }

    ## Keywords related to groups and wells
    GROUP_WELL_KEYWORDS = ["IGRP", "SGRP", "XGRP", "ZGRP", "IWEL", "SWEL", "XWEL", "ZWEL"]

class ProductionConfig(Config):
    pass


class StagingConfig(Config):
    pass


class DevelopmentConfig(Config):
    pass


configs = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "staging": StagingConfig,
    "default": ProductionConfig,
}

config_name = os.getenv("DEPLOYMENT") or "default"

config = configs[config_name]
