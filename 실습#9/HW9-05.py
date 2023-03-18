
"""
작성자: 최용준
작성일:2021.11.9
1. 이진탐색트리를 이해하고 이를 응용해본다
2. 실습문제 9.5: 연락처를 저장하고 탐색하는 프로그램 작성
3. 구현 방법: 예제에서 만들어 놓은 이진탐색트리 함수들을 이용한다
"""
#이름 : 연락처 매칭 - 맵으로 구현 -> 연락처를 키로, 이름 value
#삽입 키i 를 누르면 친구의 이름과 전화번호를 인풋으로 받아서 넣어줌
#탐색 키s 를 누르면 친구의 이름을 검색하여 전화번호를 찾아줌
#삭젳 키d 를 누르면 친구의 이름을 입력하여 전화번호를 삭제시킴
#맵을 이용하여 구현

from bstADT import *

phoneDic=BSTMap()

while(True):
    print("삽입(i), 탐색(s), 삭제(d): ")
    orderChar=input()
    if orderChar=='i':
        print("친구이름: ", end='')
        nameOfFriend=input()
        print("전화번호: ", end='')
        phoneNumber=int(input())
        phoneDic.insert(phoneNumber,nameOfFriend)
        print("저장되었습니다")
    
    elif orderChar=='s':
        print("찾을 친구의 이름: ", end='')
        deleteName=input()
        findNode=phoneDic.search_value(deleteName)
        if findNode==None:
            print("없는 번호입니다")
        else:
            print("전화번호: ", findNode.key)
    
    elif orderChar=='d':
        print("삭제할 친구의 이름: ", end='')
        deleteName=input()
        deleteNode=phoneDic.search_value(deleteName)
        if deleteNode==None:
            print("없는 번호 입니다")
        else:
            phoneDic.delete(deleteNode.key)
        print("삭제되었습니다")

    elif orderChar=='q':
        break
    else:
        print("다시입력하세요")
