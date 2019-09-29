from typing import Optional

from yangify.translator import Translator, TranslatorData, unneeded


class Individual(Translator):
    """
    Implements /napalm-star-wars:universe
    """

    class Yangify(TranslatorData):
        path = "/napalm-star-wars:universe/individual"

        def pre_process(self) -> None:
            self.result = self.result.new_section(f"  - name: {self.key}")

        def pre_process_list(self) -> None:
            self.result = self.root_result.new_section("  individuals:")
            if self.to_remove and not self.replace:
                for element in self.to_remove:
                    self.result.add_command(f"#   - name: {element['name'].value}")
                    self.result.add_command(f"#     age: {element['age'].value}")
                    aff = element["affiliation"].value[0]
                    model = element["affiliation"].value[1]
                    self.result.add_command(f"#     affiliation: {model}: {aff}")

    def age(self, value: Optional[int]) -> None:
        if value:
            self.yy.result.add_command(f"    age: {value}")
        else:
            self.yy.result.add_command(f"#     age: {value}")

    def affiliation(self, value: Optional[str]) -> None:
        if value:
            self.yy.result.add_command(f"    affiliation: {value[1]}: {value[0]}")
        else:
            self.yy.result.add_command(f"#     affiliation: {value[1]}: {value[0]}")

    name = unneeded


class Universe(Translator):
    class Yangify(TranslatorData):
        path = "/napalm-star-wars:universe"

        def pre_process(self):
            pass

    individual = Individual
