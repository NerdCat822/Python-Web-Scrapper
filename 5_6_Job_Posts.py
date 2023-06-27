from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200: # 200 = 정상
    print("Can't request website")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = soup.find_all('section', class_="jobs") # <section> tag 확인
    for job_section in jobs:
        # job_posts 는 <li> list
        job_posts = job_section.find_all('li') # <section> 내 <li> 태그 확인
        job_posts.pop(-1) # 마지막 <li, class='view-all'> 제거, 필요 없음
        for post in job_posts:
            print(post)
            print("//////////////")