from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/news")
def get_news():
    news = {
        "id": 1,
        "title": "Demo",
    }

    return jsonify({"news": news})


if __name__ == "__main__":
    app.run(debug=True)