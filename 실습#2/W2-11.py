#P2.4
import math
def draw_tree(row, left, right):
       check=math.pow(2,row+1)
       check=(right-left)//check
       if check==0:
              return 
       index=0
       for i in range(left,right):
              if i%check==0:
                     if index%2==1:
                            print("X", end='')
                     else:
                            print("-", end='')
                     index+=1
              else:
                     print("-",end='')
       print()
       draw_tree(row+1,left,right)
draw_tree(0,0,65)
              
              