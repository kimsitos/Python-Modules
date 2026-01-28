#!/usr/bin/env python3

import sys

print("=== Player Score Analytics ===")

scores = []
try:
    for argv in sys.argv[1:]:
        scores.append(int(argv))

    total_players = len(scores)
    if total_players <= 0:
        print("No scores. Usage: python3 ft_score_analytics.py <score1> ...")

    else:
        print(f"Scores processed: {scores}")

        print(f"Total players: {total_players}")

        total_score = sum(scores)
        print(f"Total score: {total_score}")

        print(f"Average score: {total_score / total_players}")

        high_score = max(scores)
        print(f"High score: {high_score}")

        low_score = min(scores)
        print(f"Low score: {low_score}")

        print(f"Score range: {high_score - low_score}")
except ValueError:
    print(f"Error: {argv} is not a valid score")
