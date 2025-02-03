


#list in python is very important
#it serves the purpose of an array in other languages
#List is a collection of items
#List is mutable
#List is ordered
#List can have duplicate items
#List can have different data types
#List can have nested list
#List can have tuple
#List can have dictionary
#List can have set


#How can i use the list in any efficient way?


names = ["Dev","Pooja","Divam"]
ages = [32,31,10]


#The list in the python is similar to the queue in the system verilog 
#you can do multiple operations on the list like append, insert, remove, pop, clear, index, count, sort, reverse, copy, extend


names.append("Dhupsa")
ages.append(38)




print(names)
print(ages)



names.pop()
print(names)

names_temp = names.copy()
names_temp[0] = "Atith"  #This will change the value of the first element in the list

print(sum(ages))




#Nested List
#what is the use case of the nested list?
#probably a matrix can be the best example of the nested list
#matrix is a 2D array


#You can use the for loop to iterate through the list

for name in names:
    print(name)

for age in ages:
    print(age)



for name,age in zip(names,ages):
    print(name,age)

#zip function is used to combine the two lists
#it created the tuples one to one. 
#it will stop when the shortest list is exhausted
zipped_data = zip(names,ages)
print(zipped_data)
print(list(zipped_data))





