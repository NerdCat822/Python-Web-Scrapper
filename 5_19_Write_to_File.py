from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

# indeed, wwr: list 로 리턴
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

file = open(f"{keyword}.csv", "w") # csv 파일 생성
file.write("Position, Company, Location, URL\n") # Column 이름

for job in jobs: # 각 dict 불러와 csv에 작성
    file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")

file.close()
