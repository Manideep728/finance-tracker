from flask import Flask
from database import init_db

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return "Finance Tracker is alive"

@app.route("/transactions")
def transactions():
    return "Transactions will live here"

if __name__ == "__main__":
    app.run(debug=True)


