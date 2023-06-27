def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w") # csv 파일 생성
    file.write("Position, Company, Location, URL\n") # Column 이름

    for job in jobs: # 각 dict 불러와 csv에 작성
        file.write(f"{job['position']}, {job['company']}, {job['location']}, {job['link']}\n")

    file.close()
