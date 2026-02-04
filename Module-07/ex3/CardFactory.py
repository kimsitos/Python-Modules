from abc import ABC, abstractclassmethod
from ex0.Card import Card


class CardFactory(ABC):
    def __init__(self):
        self.raritys = ['Common', 'Rare', 'Legendary']
    @abstractclassmethod
    def create_creature(self, name_or_power) -> Card:
        pass

    @abstractclassmethod
    def create_spell(self, name_or_power) -> Card:
        pass

    @abstractclassmethod
    def create_artifact(self, name_or_power) -> Card:
        pass

    @abstractclassmethod
    def create_themed_deck(self, size: int) -> dict:
        pass

    @abstractclassmethod
    def get_supported_types(self) -> dict:
        pass
