"""
작성자: 최용준
작성일:2021.10.04
1. 덱을 활용하는 방법에 대해 실습한다
2. 실습문제 5.4: 덱을 이용하여 팰린드롬 판별문 구현
3. 방법: deque 클래스를 활용
알고리즘:
1. collections 모듈에서 deque 클래스 import
2. 덱 생성
3. 덱에 문자열 삽입
4.덱의 앞뒤를 빼내서 소문자로 바꿈
5. 덱에서 꺼낸 문자들이 구두점이면 다음 순번 문자 빼냄
6.덱에서 빼낸 문자열이 다른 값이면 false 반환
7. 남은 덱이 없거나 남은 덱이 구두점이면 true 반환
"""
from collections import deque 

strList= list(input())
def isPalindrome(string):
    deq=deque()#덱 인스턴스 생성

    deq.extend(string) #덱에 문자열 삽입
    while(len(list(deq))>1):#덱의 길이가 1보다 크면 반복
        frontChar=deq.popleft().lower() #덱의 전면부 뺸 후 소문자 변환
        backChar=deq.pop().lower()#덱의 후면부 뺀 후 소문자 반환
        while(len(list(deq))>1):
            if frontChar in ".,' ":
                frontChar=deq.popleft().lower() #덱의 전면부에서 뺀 값이 구두점이면 다음 값으로 넘어감
            else: break
        while(len(list(deq))>1):
            if backChar in ".,' ":
                backChar=deq.pop().lower() #덱의 후면부에서 뺀 값이 구두점이면 다음값으로 넘어감
            else: break
        if (frontChar in ".,' ") or (backChar in ".,' "): #덱에 남아있는 값이 구두점이라면 참
            return True
        elif frontChar!=backChar:#덱에서 빼낸 앞과 뒤가 다르다면 팰린드롬이 아님
            return False
    return True

print(isPalindrome(strList))

