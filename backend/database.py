import mysql.connector

conn = mysql.connector.connect(
    host="リンク",
    port=3333,
    user="ユーザーネーム",
    password="パスワード",
    database="データベース名",
)
cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT VERSION();")
print(cursor.fetchone())

# データ取得
cursor.execute("SELECT id, name, email FROM user")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
