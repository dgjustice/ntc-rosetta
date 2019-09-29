from ntc_rosetta.parsers.dummies.dummy.napalm_star_wars.star_wars import (
    Universe,
    to_yaml,
)
from typing import Any, Dict
from yangify import parser


class DummyParser(parser.RootParser):
    """
    DummyParser expects as native data a dictionary where the `universe`
    key is reserved for the device configuration.
    """

    class Yangify(parser.ParserData):
        def init(self) -> None:
            self.root_native: Dict[str, Any] = to_yaml(self.root_native["dev_conf"])
            self.native: Dict[str, Any] = self.root_native["universe"]

    universe = Universe
