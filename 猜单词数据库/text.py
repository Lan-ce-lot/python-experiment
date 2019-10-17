#单词写入数据库
import sqlite3
regions = [(1, "anwser"), (2, "password"), (3, "python"), (4, "learn")]

'''cur = con.execute("select id from region")
for i in cur:
    print(i)'''



'''con.commit()'''
con = sqlite3.connect(r"F:\work\二上\py\SQL数据库\test.db")
con.execute("create table region(id primary key, name)")

con.executemany("insert into region(id, name) values(?, ?)", regions)
con.commit()
con.close()


