from ex2.EliteCard import EliteCard


print("=== DataDeck Ability System ===")

print("EliteCard capabilities:")
print("- Card: ['play', 'get_card_info', 'is_playable']")
print("- Combatable:  ['attack', 'defend', 'get_combat_stats']")
print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

print("\nPlaying Arcane Warrior (Elite Card)")
Arcane_Warrior = EliteCard('Arcane Warrior', 3, 'Legendary', 4, 9)

print("\nCombat phase:")
print("Attack result:", Arcane_Warrior.attack('Enemy'))
print("Defense result", Arcane_Warrior.defend(5))

print("\nMagit phase:")
print("Spell cast:", Arcane_Warrior.cast_spell('Fireball', ['Enemy1, Enemy2']))
print("Mana channel:", Arcane_Warrior.channel_mana(3))

print("Multiple interface implementation successful!")
