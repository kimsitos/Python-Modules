from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(self, facotry: CardFactory,
                         strategy: GameStrategy) -> None:
        if not isinstance(facotry, CardFactory):
            raise ValueError("Factory must be from class CardFactory")
        self._factory = facotry

        if not isinstance(strategy, GameStrategy):
            raise ValueError("Strategy must be from class GameStrategy")
        self._strategy = strategy

        self.hand_user = facotry.create_themed_deck(5)
        self.battlefield = [facotry.create_creature('goblin'),
                            facotry.create_creature('dragon')]

        self._turns_simulated = 0
        self._total_damage = 0

    def simulate_turn(self) -> dict:
        turn_result = self._strategy.execute_turn(
            self.hand_user, self.battlefield)

        self._total_damage = turn_result.get('damage_dealt')
        self._turns_simulated += 1
        return turn_result

    def get_engine_status(self) -> dict:
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': self._strategy.get_strategy_name(),
            'total_damage': self._total_damage,
            'cards_created': len(self.hand_user) + len(self.battlefield)
        }
