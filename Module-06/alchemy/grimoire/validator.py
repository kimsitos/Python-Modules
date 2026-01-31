def validate_ingredients(ingredients: str) -> str:
    valid_ingredents = ["fire", "water", "earth", "air"]
    for ingredient in valid_ingredents:
        if ingredient in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
