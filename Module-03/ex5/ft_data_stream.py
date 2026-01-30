
# -------------------
# NECESITA REVISION
# -------------------

def process_events(num_events):
    id_event = 1
    players = ['alice', 'frank', 'bob', 'eve', 'diana', 'charlie']
    events_type = ['found treasure', 'killed a monster',
                   'has died', 'leveled up']
    while id_event <= num_events:
        yield {
            'id': id_event,
            'player': players[id_event % len(players)],
            'event_type': events_type[id_event % (len(events_type))],
            'data': {
                'level': id_event + len(players) + (
                    id_event % len(events_type)),
                'score_delta': -25,
                'zone': 'pixel_zone_5'
            }
        }
        id_event += 1


def fibonacci(index):
    a = 0
    b = 1
    for _ in range(index):
        yield a
        a, b = b, a + b
        index -= 1


def prime_numbers(index):
    def is_prime(num):
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

    a = 2
    while index:
        if is_prime(a):
            yield a
            index -= 1
        a += 1


game_events = process_events(12)
fib = fibonacci(10)
prime = prime_numbers(5)

total_events = 0
treasures_found = 0
monsters_killed = 0
deaths = 0
level_ups = 0
print("=== Game Data Stream Processor ===\n")

print("Processing 100 game events\n")
for ev in game_events:
    print(f"Event {ev['id']}: Player {ev['player']} "
          f"(level {ev['data']['level']}) {ev['event_type']}")
    match ev['event_type']:
        case 'found treasure':
            treasures_found += 1
        case 'killed a monster':
            monsters_killed += 1
        case 'has died':
            deaths += 1
        case 'leveled up':
            level_ups += 1
    total_events += 1

print("\n=== Stream Analytics ===")
print("Total events processed:", total_events)
print("Treasures events:", treasures_found)
print("Monsters events:", monsters_killed)
print('Deaths events:', deaths)
print('Level-up events:', level_ups)

print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10):", end=' ')
for f in fib:
    print(f, end=' ')

print("\nPrime numbers (first 5):", end=' ')
for p in prime:
    print(p, end=' ')
