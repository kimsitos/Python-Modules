from ex4.TournamentCard import TournamentCard


class TournamentPlataform:
    def __init__(self):
        self._cards = {}
        self._total_cards = 0
        self._matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise ValueError("Please, insert a TournamentCard")
        if self._cards.get(card._name):
            return f"Error: {card._name} is already registered"
        self._cards[card._name] = card
        self._total_cards += 1
        return f"Card {card._name} registered correctly!"

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self._cards.get(card1_id)
        if card1 is None:
            raise FileNotFoundError("Can't find Card1")

        card2 = self._cards.get(card2_id)
        if card2 is None:
            raise FileNotFoundError("Can't find Card2")

        while card1._health > 0:
            card2._health -= card1._attack
            if card2._health < 0:
                break
            card1._health -= card2._attack

        self._matches_played += 1

        if card1._health > 0:
            card1.update_wins(1)
            self._cards[card1_id] = card1
            card2.update_losses(1)
            self._cards[card2_id] = card2
            return {
                'winner': card1._name,
                'loser': card2._name,
                'winner_rating': card1._rating,
                'loser_rating': card2._rating,
            }
        card1.update_losses(1)
        self._cards[card1_id] = card1
        card2.update_wins(1)
        self._cards[card2_id] = card2
        return {
                'winner': card2._name,
                'loser': card1._name,
                'winner_rating': card2._rating,
                'loser_rating': card1._rating,
            }

    def get_leaderboard(self) -> list:
        def criteria(r):
            return r._rating
        leaderboard = [card for card in self._cards.values()]
        leaderboard.sort(key=criteria, reverse=True)
        return leaderboard

    def genetate_toutnament_report(self) -> dict:
        avg_rating = 0
        for card in self._cards.values():
            avg_rating += card._rating
        avg_rating /= self._total_cards
        return {
            'total_cards': self._total_cards,
            'matches_played': self._matches_played,
            'avg_rating': avg_rating,
            'plataform_status': 'active'
        }
