from flask import Flask, render_template, request
from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("JobScrapper")


@app.route("/") # 이 위치로 이동시, 아래 함수 실행
def home():
    return render_template("home.html", name="nico")

db = {} # 가짜 DB, Cache

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")