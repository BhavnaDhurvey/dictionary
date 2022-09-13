# # a={101:"Ram",102:"Shan",103:"Mom"}
# # for x in a:
# #        print(x,':',a[x])





# # a={101:"Ram",102:"Shan"}
# # for x in a:
# #     print("key is ",x,"and the value is",a[x])


# # a=[[40,50,60],[70,80,90],[10,30,8]]
# # b={}
# # c=input("enter the number...")
# # for x in a:
# #     b[x]=a
# #     for k in c:
# #         print(x,':',a[x])

 
# # a=[[40,50,60],[70,80,90],[10,30,8]]

# # sum=0
# # b=[]
# # while i<len(a):
# #     j=0
# #     while j<len(a):
# #         sum=i,j
# #         b.append(sum)
# #         j=j+1
# #     i=i+1
# # print(b)

# # p={}
# # for x in a:
# #     p[b]=x
# # print(p)
# # for i in a:
# #     for j in a[i]:
# #         s=i,j
# # print(s)

# # b={}
# # for x in a:
# #     b[x]=a
# # print(b)


# a=[[40,50,60],[70,80,90],[10,30,8]]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==type([]):
#         j=0
#         while j<len(a[i]):
#             if type(a[i][j])==type([]):
#                 k=0
#                 while k<len(a[i][j]):
#                     b.append(a[i][j][k])
#                     k+=1
#             else:
#                 b.append(a[i][j])
#             j=j+1
#     else:
#         b.append(a[i])
#     i=i+1
# print(b)
# p={}
# i=0
# while i <len(b):
#     p[i]=b[i]
#     i=i+1 
# print(p)

c=int(input("enter the number..."))

for x in range(c):
    print(x,":",p[x])
    