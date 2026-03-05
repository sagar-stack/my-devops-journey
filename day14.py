import time
import requests

url = "https://www.google.com"
print("Starting continuous Monitoring...(Press Ctrl+C to stop)")

while True: # This means repeat forever
   try:
      status = requests.get(url, timeout=5).status_code
      if status == 200:
         print(f"[{time.ctime()}] {url} is healthy. ")
      else:
         print(f"[{time.ctime()}] {url} is having issues!")
   except requests.exceptions.RequestException as e:
      print(f"[{time.ctime()}] Connection failed! Error: {e}")


# This is the most important part
# It tells your script to "sleep" for 10 seconds so it doesn't melt your CPU
time.sleep(10)


