from importlib import import_module


# ----------------
# Matrix functions
# ----------------
def fetch_matrix_data():
    print("\nAnalyzing Matrix data...")

    matrix = {
        "month":
            ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
             "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "leaving": np.random.randint(100, size=12)
    }
    df = pd.DataFrame(matrix)
    return df


def generate_visualization(df):
    print("Generating visualization...")
    month = df.get('month')
    leaving = df.get('leaving')
    if month is None or leaving is None:
        print("Error. Please insert values for month and leaving")
        exit(1)

    pyplot.plot(month, leaving, marker='o')
    pyplot.xlabel("Months")
    pyplot.ylabel("People leaving")
    pyplot.title("People living Madrid in 20XX")

    output_file = "matrix_analysis.png"
    pyplot.savefig(output_file)
    pyplot.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


print("\nOPERATOR STATUS: Loading programs...")
print("\nChecking dependencies:")

# ------------
# Get librarys
# ------------

"""Panadas imported for analyze data"""
try:
    pd = import_module('pandas')
    print(f"[OK] {pd.__name__} ({pd.__version__}) - Data manipulation ready")
except ModuleNotFoundError as e:
    pd = None
    print("[ERROR]", e)


try:
    np = import_module('numpy')
    print(f"[OK] {np.__name__} ({np.__version__}) - Network access ready")
except ModuleNotFoundError as e:
    np = None
    print("[ERROR]", e)


"""matplotlib used for visualizationof data.
In this case used to work with pandas"""
try:
    pyplot = import_module('matplotlib')
    print(f"[OK] {pyplot.__name__} ({pyplot.__version__})"
          f"- Visualization ready")
    pyplot = import_module('matplotlib.pyplot')
except ModuleNotFoundError as e:
    pyplot = None
    print("[ERROR]", e)

if pd and np and pyplot:
    generate_visualization(fetch_matrix_data())
else:
    print("\n-- With poetry --"
          "\npoetry install"
          "\npoetry run python3 operator"
          "\n\n-- With pip --"
          "\npip install -r requirements.txt"
          "\npython3 operator.py")
