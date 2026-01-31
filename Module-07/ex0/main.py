from ex0.CreatureCard import CreatureCard


print("=== DataDeck Card Foundation ===")

print("\nTesting Abstract Base Class Design:")
Fire_Dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)
print("\nCreatureCard Info:")
print(Fire_Dragon.get_card_info())

mana_available = 6
print(f"\nPlaying {Fire_Dragon.name} with {mana_available} mana available:")
playable = Fire_Dragon.is_playable(mana_available)
print("Playable:", playable)
if playable:
    print("Play result:", Fire_Dragon.play(Fire_Dragon.get_card_info()))

Goblin_Warrior = CreatureCard('Goblin Warrior', 2, 'Common', 1, 2)
print(f"\n{Fire_Dragon.name} atttacks {Goblin_Warrior.name}")
print("Attack result:", Fire_Dragon.attack_target(Goblin_Warrior))

mana_available = 2
print(f"\nTesting insufficient mana ({mana_available} available):")
playable = Fire_Dragon.is_playable(mana_available)
print("Playable:", playable)
if playable:
    print("Play result:", Fire_Dragon.play(Fire_Dragon.get_card_info()))

print("\nAbstract pattern succesfully demonstrated!")
