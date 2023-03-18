"""
작성자: 최용준
작성일:2021.9.27
1. 스택을 활용하는 방법에 대해 실습한다
2. 실습문제 4.4: 실습 4.3에서 확장구현한 괄호검사프로그램을 주석과 따옴표 내부도 무시하도록 확장구현
3. 방법: 4.2절에서 구현한 Stack 클라스 활용
알고리즘:
1. 사용자로부터 파일이름을 받아들임
2. 만들어 놓은 스택 모듈로부터 스택 클래스를 불러와서 생성
3. 예제에서 만들어 놓은 checkBrackets 함수를 이용하기 위해 각 줄들의 배열을 하나로 묶고 구분하기 위해
    줄의 마지막을 $로 놓음
4. checkBrackets 함수를 확장
    -각 조건에 위배될 때마다 print문으로 위배조건 출력
    -줄을 검사하는 cnt,줄마다의 문자열을 체크하는 lineChar, 조건1 위배시 그줄에서의 괄호위배 문자위치를 알려주는 cntOfErr1 변수를 놓음
    -줄이 바뀔때마다 cnt 를 증가시키고 lineChar를 0으로 초기화, 한 라인내에서는 lineChar 1씩증가
    -주석인지 아닌지 판단하는 변수인 cntQuote 추가
    -# 기호를 만나면 cntQuote를 증가시켜서 그동안은 루프내에서 문자열을 건너뜀
    -줄이 바뀌면 cntQuote를 초기화 시켜서 다시 루프 가동
    -따옴표문인지 아닌지 판단하는 cntEx1, cntEx2(각각 큰따옴표, 작은따옴표 체크)추가
    -따옴표를 만나면 cntEx 변수 1로 변함, cntEx가 1일때는 루프 건너뜀/따옴표 끝나면 cntEx 2로 바뀌고 이떄 0으로 초기화

5. 함수 출력
"""
import stackADT
def checkBrackets(statement):
    stack = stackADT.Stack()
    cnt=1#몇번쨰 줄인지 세는 변수(줄 바뀔떄 마다 +1)
    lineChar=0 #줄에서의 문자수를 세는 변수(줄 바뀌면 0으로 초기화)
    cntOfErr1=0 #에러1이 발생할 때 몇번째 문자열인지 세주는 변수
    cntQuote=0 # 주석인지 아닌지 판단하는 변수 (주석문에서는 1, 아니면 0)
    cntEx1=0; cntEx2=0#따옴표인지 아닌지 판단하는 변수
    for ch in statement:
        if ch==' ': #띄어쓰기를 만나면 문자수를 세지 않도록 제낌
            continue
        else:
            lineChar+=1

        if ch=='#':   
            cntQuote+=1
        if cntQuote!=0:
            continue     # 주석문을 만나게 되면 cntQuote를 증가시켜 주석문에 있는 동안 제낌

        if ch=='"':
            cntEx1+=1
        elif ch=="'":
            cntEx2+=1
        if cntEx1==1: #따옴표를 한번 만나면 cntEx가 1이 되어 괄호안에 있는동안은 제껴짐
            continue
        elif cntEx1==2: # 따옴표 한번 더 만나면 cntEx가 2가 되고 이 경우 괄호탈출이기에 cntEx를 0으로 초기화
            cntEx1=0
        if cntEx2==1:# 위와 마찬가지
            continue
        elif cntEx2==2:
            cntEx2=0 

        if ch=='$':
            cnt+=1  #줄 바뀌면 cnt를 하나씩 늘림
            lineChar=0 #줄바뀌면 라인내에 있는 문자수를 세는 변수 초기화
            cntQuote=0 #줄이 바뀌기에 주석문 탈출하므로 0으로 초기화
            cntEx1=0 # 줄 바뀌므로 괄호 탈출하므로 0으로 초기화
            cntEx2=0		    #줄 바뀌므로 초기화
        if ch in ('{', '[', '('):	
            stack.push(ch)
            cntOfErr1=cnt
            
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
if checkBrackets(totalCode):
    print("괄호 이상 없음")
else:
    print("괄호 오류")
    



