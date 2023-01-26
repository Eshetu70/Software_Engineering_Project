from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World thiss my first program i was write down"
if __name__ == "__main__":
    app.run(host ='127.0.0.1', port =8098) 
