"""
작성자: 최용준
작성일:2021.10.04
1. 큐을 활용하는 방법에 대해 실습한다
2. 실습문제 5.3: 피보나치 수열 계산 큐를 이용하여 계산
3. 방법: queue 모듈을 활용하여 계산 한 피보나치 수열을 넣고, 이전 계산한 수열은 뺄 것
알고리즘:
1. 큐 클래스 생성
2. 큐에 n=0 일 때와 n=1일 때의 값 삽입
3. 큐에 들어있는 두 개의 수를 빼서 합쳐 f(n)계산
4. f(n-1)과 f(n)값 다시 큐에 삽입
5. f(n)값 반환
"""
from queue import Queue

def fibo_queue(n):
    que=Queue()#큐 인스턴스 생성
    for i in range(n+1):
        if i==0:
            que.put(0) 
        elif i==1:
            que.put(1) #큐에 0과 1 삽입
        else:
            cnt1=que.get()
            cnt2=que.get()
            enque=cnt1+cnt2 #큐에서 두개 넣은 값 빼 낸후 더해서 다음 값 구함
            que.put(cnt2) 
            que.put(enque) #f(n-1)과 f(n) 값 다시 삽입
    que.get()
    return que.get()

print(fibo_queue(10))