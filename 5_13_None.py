from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options=options)

browser = webdriver.Chrome()
browser.get("https://kr.indeed.com/jobs?q=python")

soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")


jobs = job_list.find_all('li', recursive=False)

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None: # mosaic-zone을 찾지 못하면, None 리턴
        print("job li")
    else:
        print("mosaic li")

# 코드 무한대기: 크롬 드라이버 버전 안맞아서 생기는 문제!!
while (True):
    pass
