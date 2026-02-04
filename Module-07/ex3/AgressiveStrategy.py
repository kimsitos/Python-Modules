from ex3.GameStrategy import GameStrategy
import random


class AgresiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        targets_attacked = []
        enemy_health = 0
        for enemy in battlefield:
            enemy_stats = enemy.get_card_info()
            try:
                enemy_health += enemy_stats.get('health')
                targets_attacked.append(enemy_stats.get('name'))
            except TypeError:
                pass

        damage_dealt = 0
        mana_used = 0
        cards_played = []
        for card in hand:
            card_stats = card.get_card_info()
            try:
                damage_dealt += card_stats.get('attack')
                mana_used += card_stats.get('cost')
                cards_played.append(card_stats.get('name'))
                if damage_dealt >= enemy_health:
                    break
            except TypeError:
                pass

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt
        }

    def get_strategy_name(self) -> str:
        return 'AgresiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        return random.shuffle(available_targets)
