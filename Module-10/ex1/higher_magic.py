def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combiner():
        if callable(spell1) and callable(spell2):
            return (spell1(), spell2())

    return combiner


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplifier():
        if callable(base_spell):
            try:
                return base_spell() * multiplier
            except TypeError:
                return None

    return amplifier


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster():
        if callable(condition) and callable(spell):
            if condition(spell):
                return spell()
            return 'Spell fizzled'

    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence():
        results = []
        for spell in spells:
            if callable(spell):
                results.append(spell())
        return results

    return sequence


test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
mages = [
    {'name': 'Morgan', 'power': 90, 'element': 'shadow'},
    {'name': 'Luna', 'power': 95, 'element': 'ice'},
    {'name': 'Zara', 'power': 80, 'element': 'water'},
    {'name': 'Kai', 'power': 77, 'element': 'lightning'},
    {'name': 'Phoenix', 'power': 76, 'element': 'lightning'}]


if __name__ == '__main__':
    print("\nTesting spell combiner...")
    def fireball(): return 'Fireball casted'
    def heal(): return 'heal casted'
    healfireball = spell_combiner(fireball, heal)
    print(healfireball())

    print("\nTesting power aplifier...")
    def fireball_damage(): return 10
    mega_fireball = power_amplifier(fireball_damage, 'o')
    print(f"Original: {fireball_damage()}, "
          f"Amplified: {mega_fireball()}")

    print("\nTesting conditional_caster...")

    def spell_condition(spell: callable):
        try:
            return True if spell() > 5 else None
        except TypeError:
            pass

    tester_conditional = conditional_caster(spell_condition, fireball_damage)
    print("Condition Result:", tester_conditional())

    print("\nTesting spell sequence")
    seq = spell_sequence([fireball, heal, fireball_damage])
    print(seq())
