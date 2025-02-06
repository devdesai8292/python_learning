#tuples are immutable, meaning that you can't change the values in a tuple once it's been created.
#this can be useful when you want to enforce the data integrity of your data
#tuples are faster than lists, because they are immutable   



#in any programming language, memory to store the data is very important and you should use the data structure which is faster. 

#tuples are faster than lists, because they are immutable and need no memory management 
#interpreter can allocate the fix memory for it and don't need to worry about future changes. 
#This lists are slower than tuples because they are mutable 




#Tuples are immutable and have a fixed size, so tuples use less memory. Overall, tuples are faster to create
#and access, resulting in better performance that can be noticeable with large amounts of data.


x = (1,2,3)
print(x)
print(type(x))

#x[2] = 4   This operation is not allowed in the tuple as tuple is immutable