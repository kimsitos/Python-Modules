from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
            'add': operator.add,
            'multiply': operator.mul,
            'max': max,
            'min': min
    }
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': partial(base_enchantment, power=50, element='fire'),
        'ice_enchant': partial(base_enchantment, power=50, element='ice'),
        'lightning_enchant': partial(
                            base_enchantment, power=50, element='lightning'),
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable


if __name__ == '__main__':
    spell_powers = [27, 38, 28, 12, 43, 20]

    print("\nTesting spell_reducer...")
    print('Sum:', spell_reducer(spell_powers, 'add'))
    print('Product:', spell_reducer(spell_powers, 'multiply'))
    print('Max:', spell_reducer(spell_powers, 'max'))
    print('Min:', spell_reducer(spell_powers, 'min'))

    print("\nTesting partial_enchanter...")

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{target} atacked with element {element} ({power} power)"

    elements = ['fire_enchant', 'ice_enchant', 'lightning_enchant']
    enchant = partial_enchanter(base_enchantment)
    for element in elements:
        print(enchant[element](target='Bunny'))
    
    print("\nTesting memoized fibonacci...")
    fibonacci_tests = [20, 20, 11, 76, 57]
    for fib in fibonacci_tests:
        print(f"Fib({fib}):", memoized_fibonacci(fib))
