players = {
    'alice': {
        'total_score': 2824,
        'favorite_mode': 'ranked',
        'achievements': set((
            "first kill", "treasure_hunter",
            "level_10", "treasure_hunter", "speed_demon"
            ))
        },
    'bob': {
        'total_score': 465,
        'favorite_mode': 'ranked',
        'achievements': set((
            "first kill",
            "boss_slayer", "collector"
            ))
        },
    'charlie': {
        'total_score': 9935,
        'favorite_mode': 'casual',
        'achievements': set((
            "first kill",
            ))
        }
}

print("\n=== List Comprehension Examples ===")
high_scores = list(set(
    user for user in players.keys() if players[user]['total_score'] > 2000))
print("High scores (>20000):", high_scores)

duplicated_scores = list(user['total_score'] * 2 for user in players.values())
print("Duplicated scores:", duplicated_scores)


print("\n=== Dictionary Comprehension Examples ===")
player_scores = dict((user, data['total_score'])
                     for user, data in players.items())
print("Player scores:", player_scores)

number_achievements = dict((user, len(data['achievements']))
                           for user, data in players.items())
print("Number of achievements:", number_achievements)


print("\n=== Set Comprehension Examples ===")
unique_players = set(player for player in players.keys())
print("Unique players:", unique_players)

all_achievements = {achievements for data in players.values()
                    for achievements in data.get('achievements')}
print("All achievements:", all_achievements)


print("\n=== Combinated Analysis ===")
total_players = len(players.keys())
print("Total players:", total_players)

total_achievements = sum(len(user['achievements'])
                         for user in players.values())
print("Total achievements:", total_achievements)

average_score = sum(data['total_score']
                    for data in players.values()) / total_players
print("average:", average_score)
