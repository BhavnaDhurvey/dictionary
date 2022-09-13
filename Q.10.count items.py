# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# total = 0
# for value in dict1:
#     value_list = dict1[value]
#     count = len(value_list)
#     total += count
# print("totalcount:",total)

# # Output :-
# total count:5



h=[10,20,30,10,20,50,30,40,10]
count=0
for i in len(h):
    for j in len(h):
        if h[i]==h[j]:
            count+=1
print(count)





