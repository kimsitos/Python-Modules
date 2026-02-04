from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self._attack = attack
        if health <= 0:
            raise ValueError("Health must be 1 or greater")
        self._health = health

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['attack'] = self._attack
        info['health'] = self._health
        return info

    def attack_target(self, target) -> dict:
        if isinstance(target, CreatureCard):
            target._health -= self._attack
            return {
                'attacker': self._name,
                'target': target._name,
                'damage_dealt': self._attack,
                'combat_resolve': True if target._health <= 0 else False,
            }
        else:
            return
