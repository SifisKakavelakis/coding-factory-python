fruits = ["Apple", "Banana", "Cherry", "Apple"]
 
print("Initial list of fruits:", fruits)
 
# Add a single element at the end of the list
fruits.append("Berry")
print(f"After addding Berry: {fruits}")
 
# Add multiple elements at the end of the list
fruits.extend(["Grapes", "Fig"])
print(f"After adding Grapes and Fig:", fruits)
 
# fruits.extend("Panos")
# print(f"Don't do that: {fruits}")
 
# fruits.extend(["Panos"])
# print(f"Don't do that: {fruits}")