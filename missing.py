
# Python code to demonstrate Dictionary and
# missing value error
 
# # initializing Dictionary
# d = { 'a' : 1 , 'b' : 2 }
 
# trying to output value of absent key
# print ("The value associated with 'c' is : ")
# print (d['c'])

 
# initializing Dictionary
test_dict = {'gfg' : [1, 3, 4], 'is' : [7, 6], 'best' : [4, 5]}
  
# printing original dictionary
print("The original dictionary is : " + str(test_dict))
  
# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()
res = []
for key, val in test_dict.items():
    res.append([key]+[val])
  
# printing result 
print("The converted list is : " + str(res)) 