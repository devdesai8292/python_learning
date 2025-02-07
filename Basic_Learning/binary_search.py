import random



### Binary search algorithm is the important question which has been asked in the interviwe with microsoft frequenctly. 
# 
# ###


#Get the user input 
random.seed(10)
list_of_numbers = random.sample(range(1, 100), 4)
#sort the list 
list_of_numbers.sort()

num_of_elements = len(list_of_numbers)
print(list_of_numbers)
lower_bound = 0
upper_bound = num_of_elements - 1

user_numer = int(input("Enter the number you want to search: "))

while True: 
    mid = (lower_bound + upper_bound + 1) // 2
    if lower_bound > upper_bound:
        print("The number is not found")
        break
    elif list_of_numbers[mid] == user_numer:
        print("The number is found at the index: ", mid)
        break
    elif list_of_numbers[mid] < user_numer:
        lower_bound = mid + 1
    else:
        upper_bound = mid - 1
    





