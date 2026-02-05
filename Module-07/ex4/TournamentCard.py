from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        Card.__init__(self, name, cost, rarity)
        Rankable.__init__(self)
        self._attack = attack
        if health <= 0:
            raise ValueError("Health must be 1 or greater")
        self._health = health

    def play(self) -> dict:
        return {
            'card_played': self._name,
            'mana_used': self._cost,
            'effect': 'TournamentCard summoned to battlefield'
        }

    def defend(self, incoming_damage: int) -> dict:
        self._health -= incoming_damage - 3
        return {
            'defender': self._name,
            'damage_taken': incoming_damage - 3,
            'damage_blocked': 3,
            'still_alive': True if self._health > 0 else False,
        }

    def attack(self, target) -> dict:
        if not isinstance(target, TournamentCard):
            raise ValueError("The target must be a TournamentCard")
        target.defend(self._attack)
        return {
            'attacker': self._name,
            'target': target._name,
            'damage': self._attack,
            'combat_type': 'melee',
        }

    def get_combat_stats(self) -> dict:
        return {
            'damage_dealed': self.attack,
            'healt': self._health,
        }

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        if wins <= 0:
            raise ValueError("Wins cant be negative")
        self._wins += wins
        self._rating += 15 * wins

    def update_losses(self, losses: int) -> None:
        if losses <= 0:
            raise ValueError("Losses cant be negative")
        self._losses += losses
        self._rating -= 15 * losses

    def get_rank_info(self) -> dict:
        info = self.get_card_info()
        info['wins'] = self._wins
        info['losses'] = self._losses
        info['rating'] = self._rating
        return info
