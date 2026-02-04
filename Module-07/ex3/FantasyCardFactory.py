from ex0 import Card, CreatureCard
from ex3.CardFactory import CardFactory
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
import random


class FantasyCardFactory(CardFactory):
    def __init__(self):
        super().__init__()
        self._creatures = ['dragon', 'goblin']
        self._spells = ['fireball', 'congelation', 'shock']
        self._artifacts = ['mana_ring', 'void_orb', 'arcane_mirror']

    def create_creature(self, name_or_power) -> Card:
        return CreatureCard(name_or_power, random.randint(1, 6),
                            random.choice(self.raritys),
                            random.randint(1, 5), random.randint(1, 7))

    def create_spell(self, name_or_power) -> Card:
        return SpellCard(name_or_power, random.randint(1, 6),
                         random.choice(self.raritys), name_or_power)

    def create_artifact(self, name_or_power) -> Card:
        return ArtifactCard(name_or_power, random.randint(1, 6),
                            random.choice(self.raritys),
                            random.randint(1, 5), name_or_power)

    def create_themed_deck(self, size: int) -> dict:
        if size < 0:
            raise ValueError("Can't support negative size")
        deck = []
        num_creatures = int(size / 2)
        num_spells = int((size - num_creatures) / 2)
        num_artifacts = int(size - (num_creatures + num_spells))
        for _ in range(num_creatures):
            deck.append(self.create_creature(
                random.choice(self._creatures)))
        for _ in range(num_spells):
            deck.append(self.create_spell(random.choice(self._spells)))
        for _ in range(num_artifacts):
            deck.append(self.create_artifact(
                random.choice(self._artifacts)))
        return deck

    def get_supported_types(self) -> dict:
        return {
            'creatures':  self._creatures,
            'spells': self._spells,
            'artifacts': self._artifacts,
        }
