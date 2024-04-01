def bullcow(scno,gusno):
    b=[0,0]
    i=0
    for s in scno:
        if s in gusno:
            if scno[i]==gusno[i]:
                b[0]+=1
            else:
                b[1]+=1
        i+=1  
    return b
    
scno=input()
gusno=input()
ans=bullcow(scno,gusno)
print(ans)