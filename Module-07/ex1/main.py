from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard


print("=== DataDeck Deck Builder ===")

print("Building deck with different card types...")
decky = Deck()
decky.add_card(CreatureCard('Joseph', 5, 'common', 3, 7))
decky.add_card(ArtifactCard('Mana-ntial', 6, 'legendary', 4,
                            'adds +1 mana during 4 turns'))
decky.add_card(SpellCard('Storm', 2, 'uncommon', 'deals 2 of damage'))
decky.shuffle()
print('Deck stats:', decky.get_deck_stats())

print("\nDrawing and playing cards:")

while decky._cards:
    card = decky.draw_card()
    print("\nDrew:", card._name)
    print("Play result:", card.play('anything'))

print("\nPolymorphism in action: Same interface, different card behaviors")
