import sqlite3


conn = sqlite3.connect("db.db", check_same_thread=False)
conn.execute("PRAGMA foreign_keys = 1")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def last5_users() -> sqlite3.Row:
    cursor.execute("SELECT  users.id, fio, datar, roles.name FROM users JOIN roles ON users.id_role = roles.id ORDER BY users.id DESC LIMIT 0, 5")
    return cursor.fetchmany(5)

def get_all_roles_id():
    cursor.execute("SELECT id from roles")
    result = cursor.fetchall()
    return result

