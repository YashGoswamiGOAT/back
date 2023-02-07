from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    open("yash.txt","w").write("Hello")
    return "Hello Yash its working"

@app.route("/file")
def index():
    return str(open("yash.txt","r").read())

if __name__=="__main__":
    app.run(host="0.0.0.0",port= 5000)
