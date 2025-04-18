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

def set_environment_variable(variable_name: str, value: str, persist: bool = False, env_file: str = ".env"):
    """
    Set a new environment variable or update an existing one.
    Optionally persist the variable to a .env file.
    
    :param variable_name: The name of the environment variable
    :param value: The value to set for the environment variable
    :param persist: Whether to save the variable to a .env file
    :param env_file: The .env file path
    """
    if not variable_name.isidentifier():
        raise ValueError("Invalid environment variable name.")

    # Check if variable already exists
    if variable_name in os.environ:
        print(f"Overwriting existing variable: {variable_name}")

    os.environ[variable_name] = value
    print(f"{variable_name} set to {value}")

    if persist:
        lines = []
        # Load existing .env content
        if os.path.exists(env_file):
            with open(env_file, "r") as f:
                lines = f.readlines()

        # Update or append the variable
        updated = False
        for i, line in enumerate(lines):
            if line.startswith(f"{variable_name}="):
                lines[i] = f"{variable_name}={value}\n"
                updated = True
                break

        if not updated:
            lines.append(f"{variable_name}={value}\n")

        # Write back to file
        with open(env_file, "w") as f:
            f.writelines(lines)
        print(f"{variable_name} persisted to {env_file}")

def delete_environment_variable(variable_name: str):
    """
    Delete an environment variable if it exists.
    :param variable_name: The name of the environment variable to delete
    """
    if variable_name in os.environ:
        del os.environ[variable_name]
        print(f"{variable_name} has been deleted.")
    else:
        print(f"Warning: {variable_name} not found in environment variables.")

def save_environment_variables_to_file(file_path: str):
    """
    Save the current environment variables to a .env file.
    :param file_path: The path where the .env file will be saved
    """
    with open(file_path, 'w') as file:
        for key, value in os.environ.items():
            file.write(f"{key}={value}\n")
    print(f"Environment variables have been saved to {file_path}")

def update_environment_variable(variable_name: str, new_value: str):
    """
    Update the value of an environment variable by appending or modifying it.
    :param variable_name: The name of the environment variable to update
    :param new_value: The new value to append or set for the environment variable
    """
    current_value = os.getenv(variable_name, "")
    updated_value = current_value + new_value  # Append the new value
    os.environ[variable_name] = updated_value
    print(f"{variable_name} updated to {updated_value}")

# Example usage
print_all_environment_variables()

# Set a new environment variable
set_environment_variable('NEW_VARIABLE', 'SomeValue')

# Update an existing environment variable by appending a value
update_environment_variable('VBT_PRO_SECRET_URL', '/new_path')

# Save current environment variables to a file
save_environment_variables_to_file("../new_env_file.env")

# Delete an environment variable
delete_environment_variable('NEW_VARIABLE')
