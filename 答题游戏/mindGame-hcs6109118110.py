import sqlite3
from tkinter import *
from tkinter.messagebox import *

# 调用数据库
con = sqlite3.connect(r"F:\work\二上\py\SQL数据库\test0.db")
cur = con.execute("select id, name, A, B, C, D, ans from region")
word = []
qid = 1
score = 0
for row in cur:
    word.append(row)
cur.close()
con.close()

# 下一题函数
def Movenext():
    global qid
    global score
    if qid > len(word):  # 判断是否做完
        return showinfo('做完了', '题目做完了\n得分:' + str(score))
    if v.get() == word[qid - 1][6]:
        showinfo('答对了', '嘻嘻！答对了耶!!')
        score += 10
        result["text"] = "得分:" + str(score)
    else:
        showinfo('答错了', '诶呀！答错了诶...')
    qid += 1
    if qid <= len(word):  # 切换下一题
        group["text"] = str(qid) + '.' + word[qid - 1][1]
        for i in range(4):
            options[i]["text"] = word[qid - 1][2 + i]
        v.set(5)

# 查看得分函数
def Results():
    showinfo('得分', '现在得分:' + str(score))

# 窗口
root = Tk()
root.title('答题游戏')
root.geometry("500x309")

# 题干
group = LabelFrame(root, text=str(qid) + '.' + word[qid - 1][1], padx=0, pady=10, font=("楷体", 14))
group.pack(padx=10, pady=30)

# 分数框
result = Label(root, text = "得分:" + str(score), font=("楷体", 14))
result.pack()

# 选项
v = IntVar()
v.set(5)
options = []
for i in range(4):  # 创建四个选项
    options.append(Radiobutton(group, text=word[qid - 1][2 + i], value=1 + i, variable=v, font=("楷体", 12)))
    options[i].pack(anchor=W)

# 按钮
f1 = Frame(group)
f1.pack()
B1 = Button(f1, text="下一题", command=Movenext, font=("楷体", 13)).pack(side=LEFT)
B2 = Button(f1, text="得  分", command=Results, font=("楷体", 13)).pack()
root.mainloop()
