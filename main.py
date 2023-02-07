from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

open("yash.txt","w").write("Hello")

@app.route("/")
def index():
    return "Hello Yash its working"


if __name__=="__main__":
    app.run(host="0.0.0.0",port= 5000)
