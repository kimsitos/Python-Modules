def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    def accumulate(power_acumulate: int) -> int:
        nonlocal initial_power
        initial_power += power_acumulate
        return initial_power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict[str, callable]:
    vault = {}

    def store(key: str, value: int):
        nonlocal vault
        vault.update({key: value})

    def recall(key: str):
        nonlocal vault
        return vault.get(key)

    return {'store': store, 'recall': recall}


if __name__ == '__main__':

    print("\nTesting mmage_counter...")
    mage = mage_counter()
    for _ in range(1, 4):
        print(f"Call {_}:", mage())

    print("\nTesting spell_acumulator...")
    damage = spell_accumulator(5)
    for _ in range(1, 4):
        print(f"Call {_}:", damage(6))

    print("\nTesting enchantment_factory")
    freeze = enchantment_factory('Frozen')
    print(freeze('Sword'))

    print("\nTesting memory vault")
    mem_vault = memory_vault()
    mem_vault['store']('chips', 10)
    mem_vault['store']('coins', 30)
    print('Chips value:', mem_vault['recall']('chips'))
    print('Coins value:', mem_vault['recall']('coins'))
