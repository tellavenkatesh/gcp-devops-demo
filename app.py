from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
        result = a + b + a
        print(a)
        return jsonify({"a": a, "b": b, "result": result})
    except:
        return jsonify({"error": "Please pass integers a and b"}), 400

@app.route('/')
def index():
    return "Welcome to GCP DevOps Demo and CI/CD automation - Add Two Numbers API"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
