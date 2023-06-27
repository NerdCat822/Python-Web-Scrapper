from flask import Flask

app = Flask("JobScrapper")


@app.route("/") # 이 위치로 이동시, 아래 함수 실행
def home():
    return "<h1>hey there!</h1>"

@app.route("/hello")
def hello():
    return 'hello you!'

app.run("0.0.0.0")
