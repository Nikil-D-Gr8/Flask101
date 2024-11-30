from dotenv import load_dotenv

# This is used to load all the .env file variables as 
# environment variables
load_dotenv()

import os
print(os.getenv("API_KEY"))

# when we want the dot_env varaible to overwrite system env one
load_dotenv(override =True)