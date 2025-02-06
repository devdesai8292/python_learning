#write a code to shift the characters of the string by 3
#Example:
#Input: "abc"
#Output: "def"



#python progrma to shift the characters of the string by 3
#you can also have shift as a user input as well
def shift_cipher(input_string):
    output_string = ""
    for i in input_string:
        output_string += chr(ord(i) + 3) #ord() function returns the ASCII value of the character and chr() function returns the character of the ASCII value and then adding 3 to the ASCII value
    return output_string

user_input = input("Enter the string: ")
output = shift_cipher(user_input)

print("The shifted string is: ", output)


def shift_cipher_adv(input_string, shift):
    output_string = ""
    for i in input_string:
        output_string += chr(ord(i) + shift)
    return output_string


user_input = input("Enter the string: ")
shift = int(input("Enter the shift: "))
output = shift_cipher_adv(user_input, shift)
print("The shifted string is: ", output)



