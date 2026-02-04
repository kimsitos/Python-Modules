from abc import ABC, abstractclassmethod


class Combatable(ABC):
    @abstractclassmethod
    def attack(self, target) -> dict:
        pass

    @abstractclassmethod
    def defend(self, incoming_damage: int) -> dict:
        pass

    @abstractclassmethod
    def get_combat_stats(self) -> dict:
        pass
