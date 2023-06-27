from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver

# from selenium.webdriver.chrome.options import Options 
# >>VSC환경에서는 옵션 변경 필요없음

# options = Options()
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")

# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()

browser.get("https://kr.indeed.com/jobs?q=python")

print(browser.page_source)

# 코드 무한대기: 크롬 드라이버 버전 안맞아서 생기는 문제!!
while(True):
    pass
