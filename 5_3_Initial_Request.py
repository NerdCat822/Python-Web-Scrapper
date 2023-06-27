from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200: # 200 = 정상
    print("Can't request website")
else:
    print(response.text) # 웹 사이트 구성 HTML 코드

