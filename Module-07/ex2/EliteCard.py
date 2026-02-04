from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self._attack = attack
        if health <= 0:
            raise ValueError("Health must be 1 or greater")
        self._health = health
        self._mana = 10
        self._spells_casted = []

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'EliteCard summoned to battlefield'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self._name,
            'target': target,
            'damage': self._attack,
            'combat_type': 'melee',
        }

    def defend(self, incoming_damage: int) -> dict:
        self._health -= incoming_damage - 3
        return {
            'defender': self._name,
            'damage_taken': incoming_damage - 3,
            'damage_blocked': 3,
            'still_alive': True if self._health > 0 else False,
        }

    def get_combat_stats(self) -> dict:
        return {

        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        if self._mana > 0:
            self._mana -= 3
        self._spells_casted.append(spell_name)
        return {
            'caster': self._name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': 3,
            'result': True if self._mana > 0 else False
        }

    def channel_mana(self, amount: int) -> dict:
        self._mana += amount
        return {
            'channeled': amount,
            'total_mana': self._mana
        }

    def get_magic_stats(self):
        return {
            'total_mana': self._mana,
            'spells casted': self._spells_casted
        }
