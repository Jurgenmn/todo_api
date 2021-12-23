def get(cur, id):
    cur.execute(f"SELECT * FROM person WHERE id = {id}")
    records = cur.fetchall()
    if len(records) != 0:
        obj = {"id": records[0][0], "name": records[0]
               [1], "username": records[0][2]}
        return obj

    return None
