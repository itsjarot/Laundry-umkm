from flask import Flask

app = Flask(__name__)

@app.route("/")
def dashboard():
    return "Laundry System — Jalan! 🧺"

if __name__ == "__main__":
    app.run(debug=True)
