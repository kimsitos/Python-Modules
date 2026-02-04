from ex0.Card import Card
import random


class Deck:
    def __init__(self):
        self._cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise ValueError("Please, insert a valid card")
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self._cards:
            if card.name == card_name:
                self._cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Card:
        card = self._cards[0]
        self._cards.remove(card)
        return card

    def get_deck_stats(self) -> dict:
        creature = 0
        artifact = 0
        spell = 0
        total_mana = 0
        for card in self._cards:
            total_mana += card.cost
            match type(card).__name__:
                case 'CreatureCard':
                    creature += 1
                case 'ArtifactCard':
                    artifact += 1
                case 'SpellCard':
                    spell += 1
        return {
            'total_cards': creature + artifact + spell,
            'creatures': creature,
            'spells': spell,
            'artifacts': artifact,
            'avg_cost': total_mana/(creature + artifact + spell)
        }
