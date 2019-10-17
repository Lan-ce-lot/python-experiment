
import sqlite3
import random

con = sqlite3.connect(r"F:\work\二上\py\SQL数据库\test.db")         #单词从数据库中取出
cur = con.execute("select id, name from region")
word = []
for i in cur: word.append(i[1])
#print(word)
cur.close()
con.close()

while True:                                                          #随机取词
    get_word = ''
    temp = random.randint(0, len(word) - 1)
    temp_word = word[temp]
    
    while (len(temp_word)):                                          #打乱字母
        position = random.randint(0, len(temp_word) - 1)
        get_word += temp_word[position]
        temp_word = temp_word[:position] + temp_word[(position + 1):]#切片操作
        
    print('乱序后单词:',get_word)
    if(input('请你猜:') != word[temp]):
        print('对不起不正确.')
        while(input('继续猜:') != word[temp]):print('对不起不正确.') 
    print('真棒，你猜对了!\n')
    
    while True:                                                      #是否继续
        judge_w = input('是否继续(Y/N):')
        if (judge_w == 'Y' or judge_w == 'y'):break
        elif (judge_w == 'N' or judge_w == 'n'):exit()
