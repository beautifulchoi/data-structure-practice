"""
작성자: 최용준
작성일:2021.9.29
1. 스택을 활용하는 방법에 대해 실습한다
2. 실습문제 4.5: 사용자에게 중위표현식을 받아서 후위표현식으로 변경하기+이를 계산
3. 방법: 4.2절에서 구현한 Stack 클라스 활용
알고리즘:
1. 사용자로부터 중위표현식을 받음
2. 만들어 놓은 스택 모듈로부터 스택 클래스를 불러와서 생성
3. 피연산자는 스택에 넣지않고 출력
4. 연산자는 스택이 비었으면 push
5. 스택이 비지 않았다면 스택에 있는 연산자와 우선순위를 비교하여 스택에 있는 연산자의 우선순위가 같거나 크다면 
스택에 있는 연산자를 pop을 한 후 출력하고 현재 연산자는 스택에 push
6. 우선순위가 현재 연산자가 더 크면 현재 연산자를 push
7. 수식이 끝나면 스택이 빌 때 까지 pop을 한 후 출력
8. 왼쪽 괄호가 나오면 스택에 push
9. 왼쪽 괄호 다음 연산자는 무조건 push
10. 오른쪽 괄호 만나면 왼쪽 괄호 삭제될 때 까지 왼쪽 괄호 위에 쌓여있는 모든 스택 pop

"""
import stackADT
def precedence (op):			      #4.4절 연산자 우선순위 예제 인용  
    if   op=='(' or op==')' : return 0	
    elif op=='+' or op=='-' : return 1	
    elif op=='*' or op=='/' : return 2	
    else : return -1

def InfixToPostfix(expr): #후위표현식으로 변환
    compStack=stackADT.Stack()
    output=[]
    for term in expr:
        if term=="(":
            compStack.push(term) # 왼괄호면 스택에 푸쉬
        elif term==")":
            while not compStack.isEmpty(): #오른 괄호면 왼괄호 나올 때까지 스택에 쌓인 연산자를 모두 빼버림
                op=compStack.pop()
                if op=="(":
                    break
                else: output.append(op) #괄호 내의 연산자 스택에서 꺼내 출력 

        elif term in "+-*/": 
            while not compStack.isEmpty():
                op=compStack.peek()
                if (precedence(term)<=precedence(op)):
                    output.append(op)
                    compStack.pop()
                else: 
                    break
            compStack.push(term) #연산자 비교를 하여 우선순위가 높은 것들 스택에서 꺼내 출력

        else: output.append(term) # 피연산자 출력

    while not compStack.isEmpty():
        output.append(compStack.pop()) #나머지 연산자들 출력 

    return output

def evalPostfix(expr):
    s = stackADT.Stack()			       
    for token in expr :			
        if token in ('+','-','*', '/'):	
            val2 = s.pop()		
            val1 = s.pop()		
            if (token == '+'): s.push(val1 + val2)	
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :				        
            s.push( float(token) )	

    return s.pop()

n=input()
print(InfixToPostfix(n))
print(evalPostfix(InfixToPostfix(n)))
            



    

    