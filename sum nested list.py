list=[[4],[5],[1]]
i=0
p=[]
while i<len(list):
    if type(list[i])==type([]):
        j=0
        while j<len(list[i]):
            if type([i][j])==type([]):
                k=0
                while k<len(list[i][j]):
                    p.append(list[i][j][k])
                    k=k+1
            else:
                p.append(list[i][j])
            j=j+1
    else:
        p.append(j)
    i=i+1
print(p)
sum=0
i=0
while i <len(p):
    sum=sum+p[i]
    i=i+1
print(sum)
