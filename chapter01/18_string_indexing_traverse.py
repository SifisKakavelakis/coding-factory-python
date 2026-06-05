
character = 'a'  

print(f"'{character}' is type of: {type(character)}")

message = "Coding Factory"

print(message[0])  
print(message[1])  
print(message[2])  
print(message[3])  
print(message[4])  
print(message[5])  

print(f"Number of letters inside the {message}: {len(message)}")  

for char in message:
    print(char)  

for i in range(10):
    print(i)  

for i in range(len(message)):
    print(message[i], end=" ")  
print()  

number = 12345678
number_str = str(number)

print("\nPrint the variable number_str per char\n")
print(int(number_str[0]))  
print(int(number_str[1]))  
print(number_str[2])  
print(number_str[3])  
print(number_str[4])  
print(number_str[5])  
print(number_str[6])  
print(int(number_str[7]))  
print("... end of variable number_str\n")

print("\n-----\nThe sum of the first [0] and second digit [1] is:", int(number_str[0]) + int(number_str[1]), ".")
print("The sum of the first [0] and eighth digit [7] is:", int(number_str[0]) + int(number_str[7]), ".  \n-----\n")