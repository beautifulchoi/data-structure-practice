"""
작성자: 최용준
작성일:2021.9.24
1. 스택을 활용하는 방법에 대해 실습한다
2. 실습문제 4.3: 스택을 이용하여 괄호검사하는 프로그램을 확장제작
3. 방법: 4.2절에서 구현한 Stack 클라스 활용
알고리즘:
1. 사용자로부터 파일이름을 받아들임
2. 만들어 놓은 스택 모듈로부터 스택 클래스를 불러와서 생성
3. 예제에서 만들어 놓은 checkBrackets 함수를 이용하기 위해 각 줄들의 배열을 하나로 묶고 구분하기 위해
    줄의 마지막을 $로 놓음
4. checkBrackets 함수를 확장(각 조건에 위배될 때마다 print문으로 위배조건 출력, 줄을 검사하는 cnt,
    줄마다의 문자열을 체크하는 lineChar, 조건1 위배시 그줄에서의 괄호위배 문자위치를 알려주는 cntOfErr1 변수를 놓음
    줄이 바뀔때마다 cnt 를 증가시키고 lineChar를 0으로 초기화, 한 라인내에서는 lineChar 1씩증가)
5. 함수 출력
"""
import stackADT
import copy
def checkBrackets(statement):
    stack = stackADT.Stack() #스택 인스턴스 생성
    cnt=1 #줄바꿈을 체크하는 변수
    lineChar=0 #라인 내의 문자위치를 체크하는 변수
    cntOfErr1=0 #조건1위배시 문자위치를 체크하는 변수
    for ch in statement:
        if ch==' ': 
            continue #문자수를 제대로 세기 위해 띄어쓰기나오면 건너뜀
        lineChar+=1 #문자 지날떄 마다 변수 +1
        if ch=='$': 
            cnt+=1
            lineChar=0 #줄바뀜 체크, 줄 바뀔때마다 그줄의 문자수 체크변수 초기화		    
        if ch in ('{', '[', '('):	
            stack.push(ch)
            cntOfErr1=copy.copy(cnt)
            
        elif ch in ('}', ']', ')'):	
            if stack.isEmpty() :
                print("조건 2 위반, {}줄 {}번째 문자".format(cnt,lineChar))

                return False		
            else :
                left = stack.pop()
                if (ch == "}" and left != "{") or \
                   (ch == "]" and left != "[") or \
                   (ch == ")" and left != "(") :
                    print("조건 3 위반, {}줄 {}번째 문자".format(cnt,lineChar))
                    return False	
    if stack.isEmpty()==False:
        print("조건 1 위반,{}줄 {}번째 문자".format(cntOfErr1,lineChar))
    else:
        print(0)
    return stack.isEmpty()	

filename=input()# 파일이름 받아들임
file=open(filename, 'rt', encoding='UTF8')
lines=file.readlines()
totalCode='$'.join(lines) #줄마다 리스트로 묶은 lines 를 하나의 문자열로 합침
if stackADT.checkBrackets(totalCode):
    print("괄호 이상 없음")
else:
    print("괄호 오류")
    



