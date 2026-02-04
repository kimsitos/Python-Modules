from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if not effect_type:
            raise ValueError("Please, insert effect type")
        self._effect_type = effect_type

    def play(self, game_state: dict = None) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': self._effect_type
        }

    def resolve_effect(self, targets: list) -> dict:
        pass
