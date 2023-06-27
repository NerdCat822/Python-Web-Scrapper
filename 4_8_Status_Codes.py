from random import randint
import requests

websites = (
    "google.com",
    "airbnb.com",
    "https://twitter.com",
    "facebook.com",
    "https://tiktok.com"
)

result = {}

for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = requests.get(website)
    if response.status_code == 200: # response 정상인지 검사
        print(f"{website} is OK")
        result[website] = "OK"
    else:
        print(f"{website} not OK")
        result[website] = "FAILED"

print(result)