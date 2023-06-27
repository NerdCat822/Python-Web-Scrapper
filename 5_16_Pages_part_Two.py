from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
    browser = webdriver.Chrome()
    browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("ul", class_="pagination-list") # 첫 페이지 확인
    if pagination == None: # pagination = None이면 스크래핑할 페이지 1개
        return 1
    pages = pagination.find_all("li", recursive=False) # 페이지 1, 2, 3, 4, 5, 다음 -> len = 6
    count = len(pages)
    if count >= 5:
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    for page in range(pages):
        browser = webdriver.Chrome()
        browser.get(f"https://kr.indeed.com/jobs?q={keyword}")
        results = []
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")

        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None: # mosaic-zone을 찾지 못하면, None 리턴
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company.string,
                    'location': location.string,
                    'position': title
                }
                results.append(job_data)
   
# 코드 무한대기: 크롬 드라이버 버전 안맞아서 생기는 문제!!
while (True):
    pass
