l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for x in l:
    for k in l:
        if l[x]<l[k]:
            l[x],l[k]=l[k],l[x]  
        else: #l[x]>l[k]:
            l[k],l[x]=l[x],l[k]  

print(l)



# l={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# d={}
# for value in l.values():
#     a.append(value)
#     a.sort()
# i=0
# while i <len(a):
#     for key ,value in l.items():
#         if value==a[i]:
#             d.update({key:value})
#     i=i+1
# print(d)
# e={}
# i=-1
# while i>=-len(a):
#     for key,value in l.items():
#         if value ==a[i]:
#             e.update({key:value})
#     i-=1
# print(e)



# # for x in l:
# #     for k in l:
# #         if l[x]<l[k]:
# #             l[x],l[k]=l[k],l[x]  
# # print(l)