import sqlite3


def create_connection():
    return sqlite3.connect("users.db")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    sql = "CREATE TABLE IF NOT EXISTS users (id text, fullname text, email text)"
    cursor.execute(sql)
    connection.commit()
    connection.close()


def get_users():
    connection = create_connection()
    cursor = connection.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    users = cursor.fetchall()
    connection.close()
    return users


def add_user(user_id: str, fullname: str, email: str) -> None:
    connection = create_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO users VALUES (?, ?, ?)"
    cursor.execute(sql, (user_id, fullname, email))
    connection.commit()
    connection.close()


def update_user(user_id: str, fullname: str, email: str) -> None:
    connection = create_connection()
    cursor = connection.cursor()
    sql = "UPDATE users SET fullname=?, email=? WHERE id=?"
    cursor.execute(sql, (fullname, email, user_id))
    connection.commit()
    connection.close()


def delete_user(user_id: str) -> None:
    connection = create_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM users WHERE id=?"
    cursor.execute(sql, (user_id,))
    connection.commit()
    connection.close()
