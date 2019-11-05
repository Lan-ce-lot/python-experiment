import sqlite3

#单词列表
regions=[
	(1, '我国古代称生什么为“弄瓦”？ ', 'A.男孩', 'B.女孩', 'C.第一个孩子', 'D.第二个孩子', 2),
	(2, '大雁塔在哪里？', 'A.苏州', 'B.杭州', 'C.南京', 'D.西安', 4),
	(3, '“落花时节又逢君”中的“君”指的是:', 'A.李白', 'B.杜甫', 'C.李商隐', 'D.李龟年', 4),
	(4, '“悄悄地挥一挥手，不带走一片云彩”的是诗人：', 'A.徐志摩', 'B.舒婷', 'C.席慕容', 'D.北岛', 1),
	(5, '“变脸”是哪个剧种的绝活？', 'A.京剧', 'B.豫剧', 'C.粤剧', 'D.川剧', 4),
	(6, '美国微软公司的总部设在 ', 'A.美国西部', 'B.美国东部', 'C.美国南部', 'D.美国北部', 1)
	]
 
#创建数据库，单词写入数据库
con = sqlite3.connect(r"F:\work\二上\py\SQL数据库\test0.db")
con.execute("create table region(id primary key, name, A, B, C, D, ans)")
con.executemany("insert into region(id, name, A, B, C, D, ans) values(?, ?, ?, ?, ?, ?, ?)", regions)
con.commit()
con.close()
