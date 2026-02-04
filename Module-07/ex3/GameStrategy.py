from abc import ABC, abstractclassmethod


class GameStrategy(ABC):
    @abstractclassmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractclassmethod
    def get_strategy_name(self) -> str:
        return ''

    @abstractclassmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
