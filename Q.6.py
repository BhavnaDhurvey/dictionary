

# dic={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3}
# a={}
# for key in dic:
#     if dic not in a:
#         a[dic]=key
# print(a)


# Output :-
# {“ball”:”red”,”bat”:4,”wickets”:8}




# dic1={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3}
# result = {}

# for key,value in dic1.items():
#     if value not in result:
#         result[key] = value
# print(result)



dict1={'ball':'red','bat':4,'wickets':8,'ball':'green','bat':3}
temp = []
res = dict()
for key, val in dict1.items():
    if val not in temp:
        temp.append(val)
        res[key] = val

print(res)