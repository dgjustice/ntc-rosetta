from ntc_rosetta.translators.dummies.dummy.napalm_star_wars.star_wars import Universe
from yangify import translator
from yangify.translator.config_tree import ConfigTree


class DummyTranslator(translator.RootTranslator):
    class Yangify(translator.TranslatorData):
        def init(self) -> None:
            self.root_result = ConfigTree()
            self.root_result.add_command("---")
            self.result = self.root_result

        def pre_process(self) -> None:
            self.root_result.new_section("universe:")

        def post(self) -> None:
            self.root_result = self.root_result.to_string()

    universe = Universe
