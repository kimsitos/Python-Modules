from abc import ABC, abstractclassmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str):
        if not name:
            raise ValueError("Error. a name must be provided")
        self._name = name
        if cost < 0:
            raise ValueError("Error. Card cost can't be negative")
        self._cost = cost
        if not cost:
            raise ValueError("Error. Every card must have rarity")
        self._rarity = rarity

    @abstractclassmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity
        }

    def is_playable(self, available_mana: int) -> bool:
        if available_mana >= self._cost:
            return True
        return False
