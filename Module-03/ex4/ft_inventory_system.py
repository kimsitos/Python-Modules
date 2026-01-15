#!/usr/bin/env python3

def print_inventory(user: str, inventory: dict):
    value = 0
    count = 0
    categories = {}

    print(f"\n=== {user}'s Inventory ===")
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

    print(f"\n=== {sender} gives {receiver} {quantity} {item} ===")
    item_send = inventory[sender].get(item)
    if item_send['quantity'] < quantity or not item_send:
        print("Transaction failed")
        return

    inventory[sender][item]['quantity'] -= quantity
    if item in inventory[receiver]:
        inventory[receiver][item]['quantity'] += quantity
    else:
        inventory[receiver][item] = {
            'class': item_send['class'],
            'rarity': item_send['rarity'],
            'quantity': quantity,
            'value': item_send['value']
        }
    print("Trasaction succesfully!")


def add_item(user: str, item: str, item_class: str, rarity: str,
             quantity: int, value: int, inventory: dict):
    inventory[user][item] = {
        'class': item_class,
        'rarity': rarity,
        'quantity': quantity,
        'value': value
    }


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
    'Bob': {

    }
}

print_inventory("Alice", inventory)
add_item('Bob', 'ring', 'armor', 'epic', 2, 6000, inventory)
transaction('Alice', 'Bob', 'potion', 2, inventory)
print_inventory('Bob', inventory)
