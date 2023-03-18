#3.2
import os
textList=[0]
def myLineEditor() :	
    while True :
        command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료 f-찾기=> ")
        if command == 'i' :		#리스트에 내용을 입력함
            pos = int( input("  입력행 번호: "))
            if pos>len(textList): #입력행이 리스트 길이보다 클 때, 늘려주고 뒤에 붙이기
                for i in range(len(textList),pos+1):
                    textList.append(0)
            string = input("  입력행 내용: ")	    
            textList.insert(pos, string)		
        elif command == 'd' :			#리스트에서 내용을 삭제함
            pos = int( input("  삭제행 번호: "))
            textList.pop(pos)			
        elif command == 'r' :			
            pos = int( input("  변경행 번호: "))
            string = input("  변경행 내용: ")	    
            textList.replace(pos, string)		        
        elif command == 'q' : return	        
        elif command == 'p' :		           #리스트 내용 모두 출력 
            print('Line Editor')
            for line in range (len(textList)) :
                if textList[line]==0:
                    continue   
                print('[%2d] '%line, end='')    
                print(textList[line])      #입력 되어있는 값만 나오도록 수정함
            print()			                    
        elif command == 'l' :			  #(1)사용자가 입력하는 파일을 읽도록 수정      
            filename=input()
            if os.path.isfile(filename):    
                infile = open(filename, "r")
                lines = infile.readlines()	        
                for line in lines:		            
                    textList.insert(len(textList), line.rstrip('\n'))
                    print(line)
                infile.close()
            else:
                print("파일이 존재하지 않습니다. 새파일을 만드세요")

        elif command == 's' :		#(2)사용자가 입력하는 파일에 현재 문서 저장하도록 수정
            filename = input()
            outfile = open(filename , "w")
            for i in range(len(textList)) :
                outfile.write(str(textList[i]))
            outfile.close()

        elif command =='f' : #(3)문자열을 입력하면 이 문자열을 포함하고 있는 라인들만을 찾아 출력할 수 있는 f 명령 추가
            print("찾을 문자열을 입력하세요 ", end='')
            string=input()
            for line in textList:
                if string in str(line):
                    print("[{}]: ".format(textList.index(line)),line)
myLineEditor()

