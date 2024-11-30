from dotenv import load_dotenv
import os

# This is used to load all the .env file variables as
# environment variables.
load_dotenv()

# Access environment variables using `os.getenv`.
print(os.getenv("Name"))  # Prints the value of the variable `Name`.
print(os.getenv("degree"))  # Prints the value of the variable `degree`.

# The `designation` variable will likely not work as expected because
# environment variable interpolation (like ${Name}) is not automatically resolved
# when using dotenv in Python. You'll need to manually combine them.

designation = os.getenv("designation")


# Print the `designation` value.
print(designation)

# When we want the .env variables to overwrite system environment ones,
# set `override=True`.
load_dotenv(override=True)
