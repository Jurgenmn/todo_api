from dotenv import load_dotenv
import os
import psycopg2

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
    record = cur.fetchone()  # Its going to rerun a list of tuples
    print("record is gonna be below this line $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(record)
    if record != None:
        if table == "person":
            obj = {"id": record[0], "name": record[1],
                   "username": record[2]}

        elif table == "activity":
            obj = {
                "id": record[0], "activity_details": record[1], "person_id": record[2]}

        return obj

    return None


# get(cur, "person", "1")
# get(cur, "activity", "1")


def init_env():
    load_dotenv()

    DBURL= os.getenv("DBURL")
    USER = os.getenv("DB_USER")
    DBNAME = os.getenv("DBNAME")
    PASSWORD = os.getenv("PASSWORD")
    PORT = os.getenv("PORT")

    # Connect to your postgres DB
    conn = psycopg2.connect(host=DBURL, dbname=DBNAME, user=USER, password=PASSWORD, port=PORT, sslmode="require")

    return conn