
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
                'level': id_event + len(players) + (id_event % len(events_type)),
                'score_delta': -25,
                'zone': 'pixel_zone_5'
            }
        }
        id_event += 1


def fibonacci(index):
    a = 0
    b = 1
    i = 0
    while i <= index:
        yield a
        a, b = b, a + b
        i += 1


game_events = process_events(138)
fib = fibonacci(27)

treasures_found = 0
monsters_killed = 0
deaths = 0
level_ups = 0

print("Processing 100 game events")
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

print(treasures_found, monsters_killed, deaths, level_ups)

print("Fibonacci")
count = 0
for f in fib:
    if f % 2 == 0:
        print(f, end=' ')


print("\n\nPower cube")
powercube = iter([x * x for x in range(10)])
for x in range(10):
    print(next(powercube), end=' ')
