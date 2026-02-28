import requests

# We are asking python to "visit" a website
response = requests.get("https://google.com")

# Lets see if the website is healthy(200 means OK)

if response.status_code == 200:
    print("Success! I can reach the internet. ")
else:
    print("Something is wrong. Status code :", response.status_code)

