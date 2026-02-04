from ex0 import Card, CreatureCard
from ex3.CardFactory import CardFactory
from ex1 import ArtifactCard, SpellCard
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power) -> Card:
        return CreatureCard(name_or_power, random.randint(1, 6),
                            random.choice(self.raritys),
                            random.randint(1, 5), random.randint(1, 7))

# self.creatures = ['dragon', 'goblin', 'elf', 'kraken']
# self.spells = ['fireball', 'storm', 'healing', 'health_drain']
# self.artifacts = ['mana_ring', 'void_orb', 'arcane_mirror']
