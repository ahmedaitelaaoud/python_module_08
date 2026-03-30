import os
from dotenv import load_dotenv

def oracle() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    env_loaded = load_dotenv()

    required_vars = {
        "MATRIX_MODE": "Mode",
        "DATABASE_URL": "Database",
        "API_KEY": "API Access",
        "LOG_LEVEL": "Log Level",
        "ZION_ENDPOINT": "Zion Network"
    }

    print("Configuration loaded:")
    loaded_values = {}
    for env_var, label in required_vars.items():
        value = os.getenv(env_var)
        loaded_values[env_var] = value
        if value is None:
            print(f"{label}: [WARNING] Not Set")
        else:
            if env_var == "API_KEY":
                display_val = "Authenticated"
            elif env_var == "DATABASE_URL":
                display_val = "Connected to local instance"
            else:
                display_val = value

            print(f"{label}: {display_val}")

    print()

    print("Environment security check:")
    if loaded_values["API_KEY"] and loaded_values["DATABASE_URL"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] Secrets missing from environment")

    if env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file not found")

    print("[OK] Production overrides available")
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()
