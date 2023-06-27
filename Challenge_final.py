from flask import Flask, render_template, request, redirect
from extractors.wwr import extract_wwr_jobs
from extractors.ro import extract_ro_jobs

app = Flask("Challenge_Job_Scrapper")


@app.route("/") # 이 위치로 이동시, 아래 함수 실행
def home():
    return render_template("home.html", name="nico")

db = {} # 가짜 DB, Cache

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        ro = extract_ro_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = ro + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run("0.0.0.0")
