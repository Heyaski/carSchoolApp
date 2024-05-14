import sqlite3

con = sqlite3.connect('Data/users_info.db')
cur = con.cursor()
query = "SELECT role FROM users WHERE login='egor'"
cur.execute(query)
current_role = cur.fetchall()
print(str(current_role[0]))
con.close()