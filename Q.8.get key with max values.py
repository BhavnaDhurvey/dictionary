dict={'A':2,'B':3,'C':8,'D':5}
max_key=None
max=0
for x in dict:
    if dict[x]>max:
        max_key=x
    s=dict.get(max_key)
print(max_key)
print(s)



dict={1:2,3:4,9:10,6:2}
maximum = 0
max_key = None
d={}
for k in dict:
    if dict[k] > maximum:
        maximum = dict[k]
        max_key = k
d[max_key]=maximum
print("max_key",max_key)
print("maximum",maximum)
print("max key and values",d)

