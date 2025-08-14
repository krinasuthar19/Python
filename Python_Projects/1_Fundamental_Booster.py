print("Welcome to interactive personal data Collector!\n\n")
name= input("Please enter your name: ")
age = int(input("Please enter your age: ")) 
height = input("Please enter your height in meters: ")
fav_number = int(input("Please enter your favorite number: "))
print("\n\nThank you! Here is the information we collected:\n\n")
print(f"Name: {name}, Type: {type(name)}, Id: {id(name)}")
print(f"Age: {age}, Type: {type(age)}, Id: {id(age)}")
print(f"Height: {height}, Type: {type(height)}, Id: {id(height)}")
print(f"Favorite Number: {fav_number}, Type: {type(fav_number)}, Id: {id(fav_number)}")

Birth_year = 2025 - age
print(f"\nYour birth year is approximately: {Birth_year} (based on youtr age of {age})")
print("\n\nThank you for using the Personal data Collector. Goodbye!")