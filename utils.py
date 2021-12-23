# def get(cur, id):
#     cur.execute(f"SELECT * FROM person WHERE id = {id}")
#     records = cur.fetchall()  # Its going to rerun a list of tuples
#     if len(records) != 0:
#         obj = {"id": records[0][0], "name": records[0]
#                [1], "username": records[0][2]}
#         return obj

#     return None


def get(cur, table, id):
    cur.execute(f"SELECT * FROM {table} WHERE id = {id}")
    records = cur.fetchone()  # Its going to rerun a list of tuples
    if records != None:
        if table == "person":
            obj = {"id": records[0], "name": records[1],
                   "username": records[2]}

        elif table == "activity":
            obj = {
                "id": records[0], "activity_details": records[1], "person_id": records[2]}

        return obj

    return None


# get(cur, "person", "1")
# get(cur, "activity", "1")
