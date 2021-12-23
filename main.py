from flask import Flask, request, jsonify
import psycopg2
import utils

# Connect to your postgres DB
conn = psycopg2.connect(host="localhost", dbname="to_do_api",
                        user="jay", password="password")

# Open a cursor to perform database operations
cur = conn.cursor()

app = Flask(__name__)


@app.route("/")
def index():
    query = "SELECT * FROM person;"
    cur.execute(query)
    users = cur.fetchall()
    users_lst = []
    for user in users:
        obj = {"id": user[0], "name": user[1], "user_name": user[2]}
        users_lst.append(obj)

    return jsonify(users_lst)


@app.route("/person/<int:id>", methods=["GET"])
def retrive_todo(id):
    user = utils.get(cur, id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    return jsonify(user)


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_car(id):
    user = utils.get(cur, id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    cur.execute(f"DELETE FROM person WHERE id = {id}")
    conn.commit()
    return jsonify(user)


# # create 2 end endponts
# # get 2 specific users  get request
# # / users/2
# # delete request to the same route on top
# debug=True make the server reload on changes
app.run("localhost", 3000, debug=True)
