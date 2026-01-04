alice = set((
    "first kill", "treasure_hunter",
    "level_10", "treasure_hunter", "speed_demon"
    ))
bob = set((
    "first kill", "level_10",
    "boss_slayer", "collector"
    ))
charlie = set((
    "level_10", "treasure_hunter",
    "boss_slayer", "speed_demon", "perfectionist"
    ))

print("=== Achivement Tracker System ===\n")
print("Player alice achivements:", alice)
print("Player bob achivements:", bob)
print("Player charlie achivements:", charlie)

print("\n=== Achievement Analytics ===")

achievements_unique = alice.union(bob, charlie)
print("All unique achivements:", achievements_unique)
print("Total unique achievements:", len(achievements_unique))
print()

print("Common to all players:", alice.intersection(bob, charlie))
rare_achievemnts = set(
    alice.difference(bob, charlie)
    | bob.difference(alice, charlie)
    | charlie.difference(alice, bob)
    )
print("Rare achievemnts (1 player) =", rare_achievemnts)
print()

print("Alice vs Bob common:", alice.intersection(bob))
print("Alice unique:", alice.difference(bob))
print("Bob unique:", bob.difference(alice))
