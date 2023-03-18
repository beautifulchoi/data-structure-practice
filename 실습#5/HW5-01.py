"""
10/01 최용준
실습문제 5.1번 서큘러 큐대신 큐모듈을 사용하여 미로탐색 구현
"""
import queue

def isValidPos(x, y) :		
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False		
    else :			        
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS() :			    	
    que = queue.Queue()
    que.put((0,1))
    print('BFS: ')			

    while not que.empty(): 
        here = que.get()
        print(here, end='->')
        x,y = here
        if (map[y][x] == 'x') : return True
        else :
            map[y][x] = '.'
            if isValidPos(x, y - 1) : que.put((x, y - 1))	
            if isValidPos(x, y + 1) : que.put((x, y + 1))	
            if isValidPos(x - 1, y) : que.put((x - 1, y))	
            if isValidPos(x + 1, y) : que.put((x + 1, y))	
    return False

def DFS() :			   
    stack = queue.LifoQueue()		
    stack.put((0,1))
    print('DFS: ')

    while not stack.empty(): 	
        here = stack.get()	    
        print(here, end='->')
        x, y = here		     
        if (map[y][x] == 'x') :	
            return True
        else :
            map[y][x] = '.'	
            
            if isValidPos(x, y - 1): stack.put((x, y - 1)) 
            if isValidPos(x, y + 1): stack.put((x, y + 1)) 
            if isValidPos(x - 1, y): stack.put((x - 1, y)) 
            if isValidPos(x + 1, y): stack.put((x + 1, y)) 

    return False
map =  [[ '1', '1', '1', '1', '1', '1' ],
	    [ 'e', '0', '1', '0', '0', '1' ],
	    [ '1', '0', '0', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '0', 'x' ],
	    [ '1', '1', '1', '1', '1', '1' ]]
MAZE_SIZE = 6
result = BFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')

map =  [[ '1', '1', '1', '1', '1', '1' ],
	    [ 'e', '0', '1', '0', '0', '1' ],
	    [ '1', '0', '0', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '1', '1' ],
	    [ '1', '0', '1', '0', '0', 'x' ],
	    [ '1', '1', '1', '1', '1', '1' ]]
result = DFS()
if result : print(' --> 미로탐색 성공')
else : print(' --> 미로탐색 실패')
