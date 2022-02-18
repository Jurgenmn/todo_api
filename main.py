from flask import Flask, request, jsonify
import utils


conn = utils.init_env()

# Open a cursor to perform database operations
cur = conn.cursor()


app = Flask(__name__)


@app.route("/")
def index():
    query = "SELECT * FROM person;"
    cur.execute(query)
    users = cur.fetchall()
    print(users)
    users_lst = []
    for user in users:
        obj = {"id": user[0], "name": user[1], "user_name": user[2]}
        users_lst.append(obj)

    return jsonify(users_lst)


@app.route("/person/<int:id>", methods=["GET"])
def retrive_todo(id):
    user = utils.get(cur, "person", id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    return jsonify(user)


@app.route("/person/<int:id>", methods=["DELETE"])
def delete_car(id):
    user = utils.get(cur, "person", id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    cur.execute(f"DELETE FROM person WHERE id = {id}")
    conn.commit()  # Save the changes on databes
    return jsonify(user)


@app.route("/person/<int:id>/activities", methods=["GET"])
def get_person_activities(id):
    user = utils.get(cur, "person", id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    query = f"SELECT * FROM activity WHERE person_id = {id}"
    cur.execute(query)
    records = cur.fetchall()
    activities = []
    for row in records:
        activity = {
            "id": row[0], "activity_details": row[1], "person_id": row[2]}
        activities.append(activity)

    return jsonify(activities)


@app.route("/person/<int:user_id>/activity/<int:activity_id>", methods=["DELETE"])
def delete_activity_from_person(user_id, activity_id):
    user = utils.get(cur, "person", user_id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    activity = utils.get(cur, "activity", activity_id)
    if activity == None:
        return (jsonify({"error": "resource not found"}), 404)

    if user["id"] != activity["person_id"]:
        return (jsonify({"error": "resource not found"}), 404)

    cur.execute(f"DELETE FROM activity WHERE id = {activity_id}")
    conn.commit()
    return jsonify(activity)


@app.route("/person/<int:user_id>/activities", methods=["POST"])
def create_activity(user_id):
    print(user_id)
    print(request.json)
    user = utils.get(cur, "person", user_id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)
    
    cur.execute(f"INSERT INTO activity(activity_details, person_id) VALUES('{request.json['activity_details']}', {user_id})")
    conn.commit()
    return (jsonify({"status": "succes"}))


@app.route("/user", methods=["POST"])
def create_user():

    cur.execute(f"INSERT INTO person(name, user_name, password) VALUES('{request.json['name']}', '{request.json['username']}', '{request.json['password']}')")
    conn.commit()
    return (jsonify({"status": "succes"}))


#person and user are refered to the same table

@app.route("/user/<int:person_id>", methods=["DELETE"])
def del_person(person_id):
    user = utils.get(cur, "person", person_id)
    if user == None:
        return (jsonify({"error": "resource not found"}), 404)

    cur.execute(f"DELETE FROM person WHERE id = {person_id}")
    conn.commit()
    return jsonify(user)



app.run("localhost", 3000, debug=True)

