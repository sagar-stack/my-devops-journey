import os
import requests
import time

# Instead of hardcoding the url, we "ask" the computer for it.
# If the computer doesn't have one,we use "https://google.com" as a backup.
target_url = os.getenv("TARGET_URL","https://google.com")

print(f"Now i am monitring {target_url}")

while True:
    try:
        r = requests.get(target_url)
        print(f"Status code: {r.status_code}")
    except:
        print("Failed to reach site.")
    time.sleep(5)
    