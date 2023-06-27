from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?term="

    response = get(f"{base_url}{keyword}")
    if response.status_code != 200: # 200 = 정상
        print("Can't request website")
    else:
        results = []
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all('section', class_="jobs") # <section> tag 확인
        for job_section in jobs:
            # job_posts 는 <li> list
            job_posts = job_section.find_all('li') # <section> 내 <li> 태그 확인
            job_posts.pop(-1) # 마지막 <li, class='view-all'> 제거, 필요 없음
            for post in job_posts:
                anchors = post.find_all('a')
                anchor = anchors[1] # anchor는 2번째꺼가 필요
                link = anchor['href']
                # <a> 안에 <span> 정보 추출: company, kind, region
                company, kind, region = anchor.find_all('span', class_="company")
                title = anchor.find('span', class_='title')
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string.replace(",", " "),
                    'location': region.string.replace(",", " "),
                    'position': title.string.replace(",", " ")
                }
                results.append(job_data)
        return results