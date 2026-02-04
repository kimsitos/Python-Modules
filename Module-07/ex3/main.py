from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AgressiveStrategy import AgresiveStrategy
from ex3.GameEngine import GameEngine

print("=== DataDeck Game Engine ===")
cardfact = FantasyCardFactory()

print("\nConfigutring Fantasy Card Game...")
print("Factory: FantasyCardFactory")
print("Strategy: AggressiveStrategy")
print("Available types:", cardfact.get_supported_types())
game = GameEngine()
game.configure_engine(FantasyCardFactory(), AgresiveStrategy())

print("\nSimulating agresive turn...")
hand = [card.get_card_info().get('name') for card in game.hand_user]
print("Hand", hand)

print("\nTurn execution:")
print("Strategy: AgressiveStrategy")
print("Actions:", game.simulate_turn())

print("\nGame Report:")
print(game.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
