from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    # Для доступа к сайту из сети, указать
    # app.run(host='0.0.0.0')
    app.run(debug=True)