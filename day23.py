import os
from dotenv import load_dotenv

# This line looks for a .env file and loads the variables
load_dotenv()

password = os.getenv("DBPASSWORD")
url = os.getenv("TARGET_URL")

print(f"Connecting to {url} using password: {password}")



