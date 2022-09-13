dict = { 'Name' : 'Nandini', 'Age' : 19 }
  
# using setdefault() to print a key value
print ("The value associated with Age is : ",end="")
print (dict.setdefault('ID', "No ID"))
print (dict.setdefault('Age'))
# printing dictionary values
print ("The dictionary values are : ")
print (str(dict))


# Output:
# The value associated with Age is : No ID
# The dictionary values are : 
# {'Name': 'Nandini', 'Age': 19, 'ID': 'No ID'}
