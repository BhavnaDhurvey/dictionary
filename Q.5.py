# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# res = {}
# for key in list1:
#     for value in list2:
#         res[key] = value
#         list2.remove(value)
#         break  
# print ("Resultant dictionary is : "+str(res))

# output=
# {'one':1,'two':2,'three':3,'four':4,'five':5}


# list1=['one','two','three','four','five']
# list2=[1,2,3,4,5,]
# n={}
# for i in range(list1):
#     c=list1[i]
#     n[c]=list2[i]  
# print(n)


list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]
n={}
i=0
while  i <len(list1):
    c=list1[i]
    n[c]=list2[i]  
    i=i+1
print(n)
