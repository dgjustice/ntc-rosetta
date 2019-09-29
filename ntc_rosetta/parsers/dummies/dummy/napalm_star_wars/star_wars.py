from typing import Any, Dict, Iterator, Tuple, cast

from ruamel.yaml import YAML

from ntc_rosetta.helpers import json_helpers as jh
from yangify.parser import Parser, ParserData


def to_yaml(config: str) -> Dict[str, Any]:
    yaml = YAML()
    config_data: Dict[str, Any] = dict(yaml.load(config))
    return config_data


class IndividualData(Parser):
    class Yangify(ParserData):
        path = "/napalm-star-wars:universe/individual"

        def extract_elements(self) -> Iterator[Tuple[str, Dict[str, Any]]]:
            for person in jh.query("individuals", self.native, default=[]):
                yield "individual", cast(Dict[str, Any], person)

    def name(self) -> Any:
        return jh.query("name", self.yy.native)

    def age(self) -> Any:
        return jh.query("age", self.yy.native)

    def affiliation(self) -> Any:
        return jh.query("affiliation", self.yy.native)


class Universe(Parser):
    class Yangify(ParserData):
        path = "/napalm-star-wars:universe"

    individual = IndividualData
