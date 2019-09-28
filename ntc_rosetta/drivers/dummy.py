from ntc_rosetta.drivers.base import Driver
from ntc_rosetta.parsers.dummies.dummy import DummyParser as NSWDummyParser
from ntc_rosetta.translators.dummies.dummy import DummyTranslator as NSWDummyTranslator


class DummyDriverNapalmStarWars(Driver):
    parser = NSWDummyParser
    translator = NSWDummyTranslator
    datamodel_name = "napalm_star_wars"
