
import sys
import turtle

def _print(l:list)->str:
    print(*l)
    

if __name__=='__main__':
    i=c1=c2=0
    
    file=open(sys.argv[1])
    res=file.readlines()
    file.close()
    rng=iter(range(len(res)))
    while i<len(res):
        if ';' in res[i]:
            res[i]=res[i][:res[i].index(';')]
        wrd=res[i]
        l=res[i].split()
        if l !=[]:
            if l[0]=='REM':
                i+=1
            elif l[0]=='FD':
                turtle.forward(float(l[1]))
            
            elif l[0]=='LT':
                turtle.left(float(l[1]))
        
            elif l[0]=='RT':
                turtle.right(float(l[1]))
            
            elif l[0]=='BK':
                turtle.back(float(l[1]))
            
            elif l[0]=='PENDOWN':
                turtle.pendown()

            elif l[0]=='PENUP':
                turtle.penup()

            elif l[0]=='PRINT':
                _print(l[1:])

            elif l[0]=='JMP':
                if c1<int(l[2]):
                    i=int(l[1])-1
                    c1+=1
                    if c1==int(l[2]):
                        i=res.index(wrd)  
                        c1=0
                  
            elif l[0]=='END':
                break
            
            
        i+=1
        
turtle.exitonclick()