# ----------------
# Matrix functions
# ----------------
def fetch_matrix_data():
    print("\nAnalyzing Matrix data...")

    matrix = rq.get("https://pokeapi.co/api/v2/pokemon?&limit=100").json()

    pokemon_name = []
    pokemon_weight = []
    for pokemon in matrix['results']:
        pokemon_name.append(pokemon.get('name'))
        pokemon_weight.append(rq.get(pokemon.get('url')).json().get('weight'))
    df = pd.DataFrame({"name": pokemon_name, "weight": pokemon_weight})
    return df


def generate_visualization(df):
    print("Generating visualization...")
    pyplot.figure(figsize=(20, 8))

    pyplot.bar(df.get('name'), df.get('weight'))
    pyplot.xlabel("Pokemon name")
    pyplot.ylabel("Wight(g)")
    pyplot.title("Pokemons weight")

    pyplot.xticks(rotation=60, fontsize=6)
    pyplot.tight_layout()
    output_file = "matrix_analysis.png"
    pyplot.savefig(output_file)
    pyplot.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


print("\nOPERATOR STATUS: Loading programs...")
print("\nChecking dependencies:")

if __name__ == '__main__':
    """Panadas imported for analyze data"""
    try:
        import pandas as pd
        print(f"[OK] {pd.__name__} ({pd.__version__}) - Data manipulation ready")
    except ModuleNotFoundError as e:
        pd = None
        print("[ERROR]", e)

    """request for request the api"""
    try:
        import requests as rq
        print(f"[OK] {rq.__name__} ({rq.__version__}) - Network access ready")
    except ModuleNotFoundError as e:
        rq = None
        print("[ERROR]", e)

    """matplotlib used for visualizationof data.
    In this case used to work with pandas"""
    try:
        import matplotlib
        import matplotlib.pyplot as pyplot
        print(f"[OK] {matplotlib.__name__} ({matplotlib.__version__})"
              f"- Visualization ready")
    except ModuleNotFoundError as e:
        pyplot = None
        print("[ERROR]", e)

    if pd and rq and pyplot:
        generate_visualization(fetch_matrix_data())
    else:
        print("\n-- With poetry --"
              "\npoetry install"
              "\npoetry run python3 operator"
              "\n\n-- With pip --"
              "\npip install -r requirements.txt"
              "\npython3 -m ex1.operator.py")
