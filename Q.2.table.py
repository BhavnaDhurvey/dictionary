# Q2. Write a Python program to print the dictionary in a table format?

dict1 = {}
# insert data into dictionary
dict1 = {(0, 0): 'Samuel', (0, 1): 21, (0, 2): 'Data structures',
         (1, 0): 'Richie', (1, 1): 20, (1, 2): 'Machine Learning',
         (2, 0): 'Lauren', (2, 1):21, (2, 2): 'OOPS with Java'
}
print(" NAME ", " AGE ", "  COURSE " )
for i in range(3):
    for j in range(3):
        print(dict1[(i, j)], end ='   ')   
    print()

# Output:

# NAME   AGE    COURSE 
# Samuel   21   Data structures   
# Richie   20   Machine Learning   
# Lauren   21   OOPS with Java 