#!/usr/bin/env python3

def print_inventory(user: str, inventory: dict):
    value = 0
    count = 0
    categories = {}

    print(f"=== {user}'s Inventory ===")
    for item, info in inventory[user].items():
        print(
            f"{item} ({info['class']}, {info['rarity']}) "
            f"{info['quantity']}x @ {info['value']} gold each = "
            f"{info['quantity'] * info['value']}"
            )

        value += info['quantity'] * info['value']
        count += info['quantity']
        if not categories.get(info['class']):
            categories.update({info['class']: 0})
        categories[info['class']] += info['quantity']

    print()
    print("Inventory value:", value, "gold")
    print("Item count:", count, "items")
    print("Categories:", end=' ')
    for item_class, quantity in categories.items():
        print(f"{item_class}({quantity})", end=' ')
    print()


def transaction(sender: str, receiver: str, item: str,
                quantity: int, inventory: dict):
    item_send = inventory[sender][item]

    if item_send['quantity'] < quantity:
        print("Transaction failed")
        return
    print("lol")


inventory = {
    'Alice': {
        'sword': {
            'class': 'weapon',
            'rarity': 'rare',
            'quantity': 1,
            'value': 500
            },
        'potion': {
            'class': 'consumable',
            'rarity': 'common',
            'quantity': 5,
            'value': 50
            },
        'shield': {
            'class': 'armor',
            'rarity': 'uncommon',
            'quantity': 1,
            'value': 200
            }
    },
    'Bob': {}
}

print_inventory("Bob", inventory)
transaction('Alice', 'Bob', 'potion', 8, inventory)
