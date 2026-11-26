import mysql.connector

conn = mysql.connector.connect(
    host="リンク",
    port=3333,
    user="ユーザーネーム",
    password="パスワード",
    database="データベース名",
)
cursor = conn.cursor(dictionary=True)


def print_data():
    # データ取得
    cursor.execute("SELECT id, name, email FROM user")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def getUsers():
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    return users


def getHistory():
    cursor.execute("SELECT * FROM users;")
    history = cursor.fetchall()
    return history


def getStationery():
    cursor.execute("SELECT * FROM users;")
    station = cursor.fetchall()
    return station


def setStationery(val):
    sql = (
        "INSERT INTO stationery "
        "(id, maker_name, name, product_code, price, stock, category, deleted_at) "
        "VALUES (%s, %s)"
    )
    cursor.execute()


cursor.close()
conn.close()
