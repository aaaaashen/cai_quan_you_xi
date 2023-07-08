import random
import sys
while True:
    def cai_quan():
        a = int(input("请出拳,其中石头为1，剪刀为2，布为3"))
        bot = random.randint(1,3)
        print("你出的是%d,电脑出的是%d"%(a,bot))
        if a+1==bot or a-2==bot:
            print("赢麻麻！")
        elif a==bot:
            print("没赢也没输")
        else:
            print("输光光！")
    ask = input("想要来一把猜拳比赛么， y or n ").lower()
    if ask == "y":
        cai_quan()
    elif ask == "n":
        sys.exit()





