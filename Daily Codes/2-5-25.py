# List of characters to find the unicode numbers of:
letters = ["s", "t", "i", "n", "k"]

# Print the symbol corresponding to each Unicode point 
print()
print("unicode numbers for", letters)
for i in letters:
    print(ord(i), end=" ")
# List of Unicode points for various symbols
symbols = [0x24BB, 0x24B6, 0x24C7, 0x271E, 0x1F923]

# Print the symbol corresponding to each Unicode point
print()
print("unicode symbols for", symbols)
for j in symbols:
    print(chr(j), end=" ")
    
for i in range (1,50):
    print(i % 5, end = " ")

# ask a user for the current hour (1-12)
current_hour = int(input("Enter the current hour (1-12):"))

#Ask the user how many hours to add
hours_to_add = int(input("How many hours do you want to add?"))

#Caculate the new hour using modulo 12 to wrap around after 12
#adjust by subtracting 1 before the modulo and adding 1 after to ensure the 1-12 range
new_hour = ((current_hour - 1 + hours_to_add) % 12) + 1

#Print the result
print("In", hours_to_add, "hours, the time will be", new_hour, ":00.")

#ask the user fopr the message to encrypt
message = (input("What message would you like to encrpyt?"))

#Ask the user for the number of positions to shift
shift = int(input("How many letters do you want to shift?"))

#Create an empty stringsz to hold the encrypted message
encrypted_message = ""

#loop[ through each character in the message
for i in message:
    # shift t6he chracter by the shift amound and wrap around using modulo 26
    shifted = (ord(i) - ord('A') + shift) % 26
    # Convert the shifted numeric value back to a character and directly add to the string
    encrypted_message += chr(shifted + ord('A'))
    
print("Here is the NEW encrypted message!", encrypted_message)
