# k={'a':10,'b':20}
# l={'c':{'d':15,'e':17}}
# k.update(l)
# print(k)
# m=[]
# m.append(k)
# print(m)
# n={}
# n[1]=m  
# print(n)


# k={'a':10,'b':20}
# l={'d':15,'e':17}
# k["c"]=l



# m=[]
# m.append(k)
# n={}
# n[1]=m  
# print(n)




d={}
s="a"
p=10
d[s]=p 
d["b"]=20             
# print(d)
z={}
m="d"
n=15
z[m]=p
z["e"]=17
# print(z)
d["c"]=z
# print(d)

m=[]
m.append(d)
n={}
n[1]=m  
print(n)


