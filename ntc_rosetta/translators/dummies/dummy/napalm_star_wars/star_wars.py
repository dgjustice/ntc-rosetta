from typing import Optional

from yangify import translator
from yangify.translator import Translator


class Individual(Translator):
    """
    Implements /napalm-star-wars:universe
    """

    class Yangify(translator.TranslatorData):
        def pre_process(self) -> None:
            self.result = self.result.new_section("")

    def name(self, value: Optional[str]) -> None:
        self.yy.result.add_command(f"  - {value}")

    def age(self, value: Optional[int]) -> None:
        self.yy.result.add_command(f"    {value}")

    def affiliation(self, value: Optional[str]) -> None:
        self.yy.result.add_command(f"    {value[0]}")


class Universe(Translator):
    class Yangify(translator.TranslatorData):
        def pre_process(self) -> None:
            self.result.new_section("individuals:")

    individual = Individual
