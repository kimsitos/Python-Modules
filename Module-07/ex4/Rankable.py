from abc import ABC, abstractmethod
import random


class Rankable(ABC):
    def __init__(self):
        self._rating = random.randint(600, 1000)
        self._wins = 0
        self._losses = 0

    @abstractmethod
    def calculate_rating(self) -> int:
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        if wins <= 0:
            raise ValueError("Wins cant be negative")
        self._wins += wins
        self._rating += 15 * wins

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        if losses <= 0:
            raise ValueError("Losses cant be negative")
        self._losses += losses
        self._rating -= 15 * losses

    @abstractmethod
    def get_rank_info(self) -> dict:
        pass
