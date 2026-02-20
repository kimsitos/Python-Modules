def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact.get('power'),
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return [mage for mage in filter(
        lambda mage: mage['power'] >= min_power, mages)]


def spell_transformer(spells: list[str]) -> list[str]:
    return [spell for spell in map(lambda spell: f"* {spell} *", spells)]


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda mage: mage['power'])['power'],
        'min_power': min(mages, key=lambda mage: mage['power'])['power'],
        'avg_power': round(sum(
            map(lambda mage: mage['power'], mages)) / len(mages), 2)
    }


if __name__ == '__main__':
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'armor'},
        {'name': 'Light Prism', 'power': 74, 'type': 'relic'},
        {'name': 'Fire Staff', 'power': 94, 'type': 'accessory'},
        {'name': 'Crystal Orb', 'power': 82, 'type': 'accessory'}]

    mages = [
        {'name': 'Morgan', 'power': 42, 'element': 'shadow'},
        {'name': 'Luna', 'power': 23, 'element': 'ice'},
        {'name': 'Zara', 'power': 80, 'element': 'water'},
        {'name': 'Kai', 'power': 77, 'element': 'lightning'},
        {'name': 'Phoenix', 'power': 76, 'element': 'lightning'}]

    spells = ['meteor', 'blizzard', 'freeze', 'tsunami']

    print("\nTesting artifact sorter...")
    artifacts_filtered = artifact_sorter(artifacts)
    print(f"{artifacts_filtered[0]['name']} "
          f"({artifacts_filtered[0]['power']} power)", end='')
    for art in artifacts_filtered[1::]:
        print(f" comes before {art['name']} ({art['power']} power)", end='')

    print("\n\nTesting power_filter...")
    print(power_filter(mages, 80))

    print("\nTesting spell_transformer...")
    for spell in spell_transformer(spells):
        print(spell, end=' ')

    print("\n\nTesting mage_stats")
    print(mage_stats(mages))
