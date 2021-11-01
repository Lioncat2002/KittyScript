'''
Condition exprs
'''
def equal(l:list):
    e1=l[0]
    for i in l:
        if e1!=i:
            return 0
            
    return 1

def greater(a,b):
    return 1 if a>b else 0

def less(a,b):
    return 1 if a<b else 0

'''
Mathematical exprs
'''
def add(l:list)->float:
    sl=[float(i) for i in l]
    print(sum(sl))

def mul(l:list)->float:
    sl=[float(i) for i in l]
    f=1
    for i in sl:
        f*=sl
    print(f)

def _min(l:list)->float:
    print(min(l))

def _max(l:list)->float:
    print(max(l))

def avg(l:list)->float:
    print(sum(l)/len(l))


def _print(l:list)->str:
    print(*l)

if __name__=='__main__':
    i=c1=c2=0
    
    file=open('hello.ks')
    res=file.readlines()
    rng=iter(range(len(res)))
    while i<len(res):
        if ';' in res[i]:
            res[i]=res[i][:res[i].index(';')]
        wrd=res[i]
        l=res[i].split()
        if l !=[]:
            if l[0]=='ADD':
                add(l[1:])
            
            elif l[0]=='MUL':

                mul(l[1:])
        
            elif l[0]=='MIN':

                _min(l[1:])
            
            elif l[0]=='MAX':

                _min(l[1:])
            
            elif l[0]=='AVG':

                avg(l[1:])

            elif l[0]=='PRINT':
                _print(l[1:])
            
            elif l[0]=='EQL':

                r=equal(l[1:])
                if r==0 and i !=len(res)-2:
                    i+=2
                    
             
            elif l[0]=='GREATER':

                r=greater(l[1],l[2])
                if r==0 and i !=len(res)-2:
                    i+=2
               

            elif l[0]=='LESS':

                r=less(l[1],l[2])
                if r==0 and i !=len(res)-2:
                    i+=2

            elif l[0]=='JMP':
                if c1<int(l[2]):
                    i=int(l[1])
                    c1+=1
                    if c1==int(l[2]):
                        i=res.index(wrd)+1  
                        c1=0
                  
            elif l[0]=='END':
                break
        i+=1
        
