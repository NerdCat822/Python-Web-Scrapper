from flask import Flask

app = Flask("JobScrapper")


@app.route("/") # 이 위치로 이동시, 아래 함수 실행
def home():
    return "hey there!"


app.run("0.0.0.0")
