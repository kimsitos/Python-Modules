from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlataform import TournamentPlataform
import random

print("=== DataDeck Tournament Platform ===")

print("\nRegistering Tournament Cards...")

fire_dragon = TournamentCard('dragon_001', random.randint(1, 8), 'legendary',
                             random.randint(1, 8), random.randint(1, 8))
print(f"\nFire Dragon (ID: {fire_dragon._name}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating:", fire_dragon._rating)
print(f"- Record: {fire_dragon._wins}-{fire_dragon._losses}")

ice_wizard = TournamentCard('wizard_001', random.randint(1, 8), 'common',
                            random.randint(1, 8), random.randint(1, 8))
print(f"\nIce Wizard (ID: {ice_wizard._name}):")
print("- Interfaces: [Card, Combatable, Rankable]")
print("- Rating:", ice_wizard._rating)
print(f"- Record: {ice_wizard._wins}-{ice_wizard._losses}")

tournament = TournamentPlataform()

tournament.register_card(fire_dragon)
tournament.register_card(ice_wizard)

print("\nCreating tournament")
print("Match result:", tournament.create_match('dragon_001', 'wizard_001'))

print("\nTournament Leaderboard:")
position = 1
for card in tournament.get_leaderboard():
    print(f"{position}. {card._name} - Rating: {card._rating}"
          f"({card._wins} - {card._losses})")
    position += 1

print("\nPlataform Report:")
print(tournament.genetate_toutnament_report())

print("\n=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
