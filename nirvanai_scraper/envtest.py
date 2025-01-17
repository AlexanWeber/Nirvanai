import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv("../.env"), override=True)

print(f"hello {os.getenv('VBT_PRO_SECRET_URL')}")

def get_environment_variable(variable_name: str):
    """
    Retrieve the value of a specific environment variable.
    :param variable_name: The name of the environment variable to retrieve
    :return: The value of the environment variable, or None if not found
    """
    value = os.getenv(variable_name)
    if value is None:
        print(f"Warning: {variable_name} not found in environment variables.")
    return value

def set_environment_variable(variable_name: str, value: str):
    """
    Set a new environment variable or update an existing one.
    :param variable_name: The name of the environment variable
    :param value: The value to set for the environment variable
    """
    os.environ[variable_name] = value
    print(f"{variable_name} set to {value}")

def print_all_environment_variables():
    """
    Print all the environment variables loaded from the .env file.
    """
    for key, value in os.environ.items():
        print(f"{key}: {value}")

# Example usage
print_all_environment_variables()
