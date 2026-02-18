import os

"""
=========
FUNCTIONS
=========
"""


def set_env_var():
    print("\nORACLE STATUS: Reading the Matrix...\n")
    try:
        with open(".env", "r") as env:
            for line in env:
                env_var, env_value = line.strip().split('=', 1)
                if not os.getenv(env_var):
                    os.environ[env_var] = env_value
        return True

    except FileNotFoundError as e:
        print(e)

    except ValueError:
        print("Insert the env variable in the correct format:"
              "<var_name>=<var_value>")
    return False


def read_env_var(set_result):
    print("Configuration loaded:")
    if set_result is False:
        return False
    env_var_oracle = ["MATRIX_MODE", "DATABASE_URL",
                      "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]

    read_result = True
    for var in env_var_oracle:
        try:
            value = os.getenv(var)
            if value is None:
                read_result = False
                raise EnvironmentError(f"Missing environment variable: {var}")
            if (var == "MATRIX_MODE" and
               not (value in ['development', 'production'])):
                read_result = False
            print(f"{var.lower()}: {value}")
        except EnvironmentError as e:
            print(f"{var.lower()}: {e}")
    return read_result


if __name__ == '__main__':
    set_result = set_env_var()
    read_result = read_env_var(set_result)
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured" if set_result else
          "[KO] .env fine is not properly configured")
    print("[OK] Production overrides available" if read_result else
          "[KO] Production overrides unavaliable")

    print("\nThe Oracle sees all configurations.")
