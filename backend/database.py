import mysql.connector

# データベース接続
conn = mysql.connector.connect(
    host="リンク",
    port=3333,
    user="ユーザーネーム",
    password="パスワード",
    database="データベース名",
)
cursor = conn.cursor(dictionary=True)


# ---- 文房具テーブル ----
def getStationery():
    cursor.execute("SELECT * FROM stationery;")
    return cursor.fetchall()


def setStationery(val):
    sql = """
        INSERT INTO stationery
        (maker_name, name, product_code, price, stock, category)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, val)
    conn.commit()


def deleteStationery(item_id):
    sql = """
        UPDATE stationery
        SET deleted_at = NOW()
        WHERE id = %s
    """
    cursor.execute(sql, (item_id,))
    conn.commit()


# ---- ユーザーテーブル ----
def getUsers():
    cursor.execute("SELECT * FROM users;")
    return cursor.fetchall()


def setUser(val):
    sql = """
        INSERT INTO users
        (name, email, password, is_administrator)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, val)
    conn.commit()


def deleteUser(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    cursor.execute(sql, (user_id,))
    conn.commit()


# ---- 履歴テーブル ----
def getHistory():
    cursor.execute("SELECT * FROM history;")
    return cursor.fetchall()


def setHistory(val):
    sql = """
        INSERT INTO history
        (item_id, user_id, operation, quantity, created_at)
        VALUES (%s, %s, %s, %s, NOW())
    """
    cursor.execute(sql, val)
    conn.commit()


def deleteHistory(his_id):
    sql = "DELETE FROM history WHERE id = %s"
    cursor.execute(sql, (his_id,))
    conn.commit()


cursor.close()
conn.close()
