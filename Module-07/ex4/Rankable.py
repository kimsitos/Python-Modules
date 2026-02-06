from abc import ABC, abstractclassmethod
import random


class Rankable(ABC):
    def __init__(self):
        self._rating = random.randint(600, 1000)
        self._wins = 0
        self._losses = 0

    @abstractclassmethod
    def calculate_rating(self) -> int:
        pass

    @abstractclassmethod
    def update_wins(self, wins: int) -> None:
        if wins <= 0:
            raise ValueError("Wins cant be negative")
        self._wins += wins
        self._rating += 15 * wins

    @abstractclassmethod
    def update_losses(self, losses: int) -> None:
        if losses <= 0:
            raise ValueError("Losses cant be negative")
        self._losses += losses
        self._rating -= 15 * losses

    @abstractclassmethod
    def get_rank_info(self) -> dict:
        pass
