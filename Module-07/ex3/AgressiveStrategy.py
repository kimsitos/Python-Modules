from ex3.GameStrategy import GameStrategy


class AgresiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
       