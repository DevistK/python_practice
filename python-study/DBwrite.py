import sqlite3

con = sqlite3.connect("D:/Python-Study/data.db", isolation_level=None)
c = con.cursor()

# c.execute("CREATE TABLE user(num INTGER PRYMARY KEY , name text , age text, phone text, job text)")

# insert = "INSERT INTO userInfo(num, name, age, phone, job)  VALUES(?,?,?,?,?)"
# dbValue = (
#   (1, 'Seo', '25', '010-1234-5678', 'back-enb-Developer'),
#   (2, 'Park', '25', '010-4321-5678', 'front-enb-Developer'),
#   (3, 'Kim', '24', '010-0000-5678', 'UX Desinger'),
#   (4, 'Lee', '25', '010-3124-5678', 'UI Designer'),
#   (5, 'Jun', '25', '010-4231-5678', 'MMA Fighter'),
#   (6, 'Baek', '28', '010-1342-5678', 'CEO'),
#   (7, 'Jo', '25', '010-2341-5678', 'CTO'),
# )
# c.executemany(insert, dbValue)

con.close()

# 소문자로 작성해도 정상임