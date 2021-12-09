
import sys
import turtle
if __name__=='__main__':
    i=0
    c=0
    stack=[]
    file=open(sys.argv[1])
    res=file.readlines()
    file.close()
    rng=iter(range(len(res)))
    while i<len(res):

        if ';' in res[i]:
            res[i]=res[i][:res[i].index(';')]
        if type(res[i])==str:
            l=res[i].split()
            res[i]=res[i].split()
        else:
            l=res[i]
            
        if l !=[]:
            if l[0]=='REM':
                pass

            elif l[0]=='JMP':
                
                if int(l[2]):
                    c+=1
                    res[i][2]=int(res[i][2])-1
                    i=int(l[1])-1

                elif int(l[2])==0:
                        res[i][2]=c-1
                   
                        c=0
                                        
            elif l[0]=='END':
                break
            else:
                stack.append(l)     
        i+=1

for i in stack:
    if i[0]=='FD':
        turtle.forward(float(i[1]))
    elif i[0]=='BK':
        turtle.back(float(i[1]))
    elif i[0]=='RT':
        turtle.right(float(i[1]))
    elif i[0]=='LT':
        turtle.left(float(i[1]))
    elif i[0]=='PENUP':
        turtle.penup()
    elif i[0]=='PENDOWN':
        turtle.pendown()
    elif i[0]=='PRINT':
        print(*i[1:])
    
turtle.exitonclick()