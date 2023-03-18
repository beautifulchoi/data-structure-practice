#1 연결 스택 이용하여 팰린드롬 구현 
"""
작성자: 최용준
작성일:2021.10.13
1. 연결 리스트를 활용하는 실습을 한다
2. 실습문제 5.1: 연결 스택 이용하여 팰린드롬 구현 
3. 방법: 
알고리즘:
1. 구현된 연결 스택 호출
2. 
"""
from linkedList import Node
from linkedList import LinkedStack

string = input()
checkStack=LinkedStack()
for ch in string: 
    if ch in ",'. ":
        continue #구두점, 스페이스 대소문자 나오면 제낌
    ch.lower() #소문자 변환
    checkStack.push(ch) #스택에 집어넣음

for idx in range(len(string)): #스택에 들어있는 문자 하나씩 꺼내며 문자열과 비교
    if string[idx] in ",'.":
        continue#구두점 스페이스 등 나오면 제낌
    ch=string[idx].lower() #소문자 변환
    check=checkStack.pop() # 스택에서 문자 하나꺼냄
    if ch!=check: #스택에서꺼낸 문자열(문자열 거꾸로)와 문자열의 문자가 같지 않을 경우 
        print("팰린드롬이 아닙니다")
        break
    if checkStack.size()<=1: #스택에서 비교할 대상 다 꺼내면(문자열이 홀수면 스택에 하나 남아있어야함)
        print("팰린드롬입니다")
        break
    



