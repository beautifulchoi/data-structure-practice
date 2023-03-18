#P2.2
from random import *
answer=randrange(1,100)
min=0
max=99
for i in range(1,11):
    print("숫자를 입력하세요(범위:{}~{})".format(min,max), end=' ')
    guess=int(input())
    if guess==answer:
        print("정답입니다! {}번 만에 맞추셨습니다".format(i))
        break
    elif guess<answer:
        print("아닙니다. 더 큰 숫자입니다.")
        min=guess
    elif guess>answer:
        print("아닙니다. 더 작은 숫자입니다.")
        max=guess
    if i==10:
        print("게임이 끝났습니다.")
