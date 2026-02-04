from abc import ABC, abstractclassmethod


class Magical(ABC):
    @abstractclassmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    @abstractclassmethod
    def channel_mana(self, amount: int) -> dict:
        pass

    @abstractclassmethod
    def get_magic_stats(self) -> dict:
        pass
