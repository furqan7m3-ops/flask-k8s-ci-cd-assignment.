from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({"message": "App is running successfully!"})

@app.route("/add")
def add():
    try:
        a = int(request.args.get("a", 0))
        b = int(request.args.get("b", 0))
        return jsonify({"result": a + b})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
