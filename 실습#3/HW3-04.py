#3.4 clear
#다항식 추상구현
import math
class Polynominal:
    def __init__(self): #비어있는 다항식 생성
        print("다항식의 최고 차수를 입력하시오: ", end='')
        deg=float(input())
        coefArr=[]
        while(deg>=0):
            print("x^{}의 계수: ".format(deg), end='')
            coef=float(input())
            coefArr.append(coef)
            deg=deg-1
        coefArr.reverse()
        self.coefArr=coefArr
    def degree(self): #다항식의 차수 반환
        return (len(self.coefArr)-1)

    def evaluate(self,scalar): # 미지수에 scalar 넣어 계산한 결과 반환
        result=0
        for deg in range(len(self.coefArr)):
            result+=self.coefArr[deg]*math.pow(scalar,deg)
        return result

    def add(self,rhs): #현재 다항식과 다항식 rhs를 더한 새로운 다항식을 만들어 반환
        addCoefArr=[]
        resultArr=[]
        if self.degree()<=rhs.degree():
            for deg in range(self.degree()+1):
                addCoefArr.append(self.coefArr[deg]+rhs.coefArr[deg])
            for degLeft in range((self.degree())+1,rhs.degree()+1):
                addCoefArr.append(rhs.coefArr[degLeft])
        else:
            for deg in range(rhs.degree()+1):
                addCoefArr.append(self.coefArr[deg]+rhs.coefArr[deg])
            for degLeft in range((rhs.degree())+1,self.degree()+1):
                addCoefArr.append(self.coefArr[degLeft])
        for i in range(len(addCoefArr)-1,-1,-1):
            resultArr.append("{} x^{}".format(addCoefArr[i],i))
        print(" + ".join(resultArr)) 
        return addCoefArr

    def subtract(self,rhs): #현재 다항식에서 다항식 rhs를 뺀 새로운 다항식을 만들어 반환
        subCoefArr=[]
        resultArr=[]
        if self.degree()<=rhs.degree():
            for deg in range(self.degree()+1):
                subCoefArr.append(self.coefArr[deg]-rhs.coefArr[deg])
            for degLeft in range((self.degree())+1,rhs.degree()+1):
                subCoefArr.append(rhs.coefArr[degLeft])
        else:
            for deg in range(rhs.degree()+1):
                subCoefArr.append(self.coefArr[deg]-rhs.coefArr[deg])
            for degLeft in range((rhs.degree())+1,self.degree()+1):
                subCoefArr.append(self.coefArr[degLeft])
        for i in range(len(subCoefArr)-1,-1,-1):
            resultArr.append("{} x^{}".format(subCoefArr[i],i))
        print(" + ".join(resultArr))
        return subCoefArr

    def multiply(self,rhs): #현재 다항식과 다항식 rhs를 곱한 새로운 다항식 만들어 반환
        #self.coefArr=[a0,a1,a2,a3,a4] rhs.coefArr=[b0,b1,b2,b3]
        multiCoefArr=[0]*(len(self.coefArr)+len(rhs.coefArr)-1)
        resultArr=[] 
        
        for i in range(len(multiCoefArr)): #최적화 어떻게 가능?
            for a in range(len(self.coefArr)):
                for b in range(len(rhs.coefArr)):
                    if a+b==i:
                        multiCoefArr[i]=multiCoefArr[i]+self.coefArr[a]*rhs.coefArr[b]
        for i in range(len(multiCoefArr)-1,-1,-1):
            resultArr.append("{} x^{}".format(multiCoefArr[i],i))
        print(" + ".join(resultArr))
        return multiCoefArr

    def display(self,function): #현재 다항식을 화면에 보기 좋게 출력
        resultArr=[]
        print(function, end=' ')
        for i in range(len(self.coefArr)-1,-1,-1):
            resultArr.append("{}x^{}".format(self.coefArr[i],i))
        print(" + ".join(resultArr))

test1=Polynominal()
test2=Polynominal()
print(test1.coefArr)
print(test2.coefArr)
print(test1.add(test2))
print(test1.subtract(test2))
print(test1.multiply(test2))
test1.display("A(x)=")