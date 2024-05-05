import sqlite3

con = sqlite3.connect('Data/info_users.db')
cur = con.cursor()
query = """
                    SELECT login, password
                    FROM users
                    """
cur.execute(query)

user_info = {login: password for login, password in cur.fetchall()}
login = input('name: ')
password = int(input('pass: '))
default_role = 'user'
query_id = """
                    SELECT id
                    FROM users
                    """
cur.execute(query_id)
ids = [id[0] for id in cur.fetchall()]
insert = f"""
                INSERT INTO users(id, login, password, role)
                VALUES({len(ids) + 1}, '{login}', {password}, 'user')
            """

cur.execute(insert)


con.close()