from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrap(*args, **kwargs) -> any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:2f} seconds")
        return result

    return wrap


def power_validator(min_power: int) -> callable:
    def validate(func: callable) -> callable:
        @wraps(func)
        def wrap(*args, **kwargs) -> any:
            if args[0] >= min_power:
                return func(*args, **kwargs)
            return 'Insufficient power for this spell'

        return wrap

    return validate


def retry_spell(max_attempts: int) -> callable:
    def try_spell(func: callable):
        total_trys = 0

        @wraps(func)
        def wrap(*args, **kwargs):
            nonlocal total_trys
            if total_trys >= max_attempts:
                return f"Spell casting failed after {max_attempts} attempts"
            try:
                return func(*args, **kwargs)
            except Exception:
                total_trys += 1
                print(f"Spell failed, retrying... "
                      f"({total_trys}/{max_attempts})")

        return wrap

    return try_spell


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        length_name = 0
        for c in name:
            if not ((c >= 'a' and c <= 'z') or
                    (c >= 'A' and c <= 'Z') or c == ' '):
                return False
            length_name += 1
        return True if length_name >= 3 else False

    def cast_spell(self, spell_name: str, power: int) -> str:
        @power_validator(10)
        def spell_cast(power: int, spell_name: str) -> str:
            return f"Successfully cast {spell_name} with {power} power"

        return spell_cast(power, spell_name)


if __name__ == '__main__':

    print("===Testing spell timer===")

    @spell_timer
    def cast_fireball(damage: int) -> str:
        """cast a fireball"""
        return f"Fireball does {damage} of damage"

    print('Name:', cast_fireball.__name__)
    print('Documentation:', cast_fireball.__doc__, '\n')
    print(cast_fireball(5))

    print("\n===Testing power_validator===")

    @power_validator(3)
    def cast_tetrakarn(damage: int) -> str:
        """cast tetrakarn spell"""
        return f"Tetrakarn does {damage} of damage"

    print('Name:', cast_tetrakarn.__name__)
    print('Documentation:', cast_tetrakarn.__doc__, '\n')
    print(cast_tetrakarn(2))
    print(cast_tetrakarn(8))

    print("\n===Testing retry_spells===")
    max_attempts = 3

    @retry_spell(max_attempts)
    def cast_ice(damage: int) -> str:
        if damage < 0:
            raise ValueError
        """cast ice spell"""
        return f"Icece does {damage} of damage"

    for _ in range(max_attempts + 1):
        print(f"{cast_ice.__name__}: {cast_ice(-2)}")
    print(f"{cast_ice.__name__}: {cast_ice(9)}")

    @retry_spell(max_attempts)
    def cast_helium(damage: int) -> str:
        if damage < 0:
            raise ValueError
        """cast helium spell"""
        return f"helium does {damage} of damage"

    print(f"\n{cast_helium(9)}")

    print("\nTesting MageGuild...")

    names = ['alb ert', 'pe', "\tmotomami"]
    for name in names:
        print(f"{name}:", MageGuild.validate_mage_name(name))

    mage = MageGuild()
    print(mage.cast_spell("iced", 15))
