import sqlite3

con = sqlite3.connect("Data/users_info.db")
cur =  con.cursor()

query_info = """
                    SELECT firstname, lastname, fathername
                    FROM users
                    """
cur.execute(query_info)

usInfo = cur.fetchall()


con.close()
