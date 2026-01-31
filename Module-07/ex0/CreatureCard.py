from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.attack = attack
        if health <= 0:
            raise ValueError("Health must be 1 or greater")
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Creature summoned to battlefield'
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['attack'] = self.attack
        info['health'] = self.health
        return info

    def attack_target(self, target) -> dict:
        if isinstance(target, CreatureCard):
            target.health -= self.attack
            return {
                'attacker': self.name,
                'target': target.name,
                'damage_dealt': self.attack,
                'combat_resolve': True if target.health <= 0 else False,
            }
        else:
            return
