from flask import Flask, request, jsonify, abort
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample API key
API_KEY = '1234567890abcdef1234567890abccxz'

def require_api_key(view_function):
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('api_key')
        if api_key and api_key == API_KEY:
            return view_function(*args, **kwargs)
        else:
            abort(401)  # Unauthorized
    return decorated_function

@app.route("/api/news")
@require_api_key
def get_news():
    news = {
        "id": 1,
        "title": "Demo",
    }

    return jsonify({"news": news})

if __name__ == "__main__":
    app.run(debug=True)
