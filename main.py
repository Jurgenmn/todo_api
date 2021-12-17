from flask import Flask, request, jsonify
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(host="localhost", dbname="todos",
                        user="jay", password="password")

# Open a cursor to perform database operations
cur = conn.cursor()

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({})


# debug=True make the server reload on changes
app.run("localhost", 3000, debug=True)
