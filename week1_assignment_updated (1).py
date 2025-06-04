
# Week 1 Assignment: Python Foundations (Updated Part A with User Input)

# --- Part A: Data Structures with User Input ---

# List: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))
print("Original list:", numbers)

# Add a new number from user input
add_num = int(input("Enter a number to add to the list: "))
numbers.append(add_num)
print("After adding", add_num, ":", numbers)

# Remove a number from user input
remove_num = int(input("Enter a number to remove from the list: "))
if remove_num in numbers:
    numbers.remove(remove_num)
    print("After removing", remove_num, ":", numbers)
else:
    print(remove_num, "is not in the list.")

# Tuple: Tuple of 5 city names from user input
cities = tuple(input("Enter 5 city names separated by commas: ").split(","))
print("Tuple of cities:", cities)

# Try to change one value (this will raise an error)
try:
    index = int(input("Enter the index of the city you want to change (0-4): "))
    new_city = input("Enter the new city name: ")
    cities[index] = new_city
except TypeError as e:
    print("Error when trying to change tuple (tuples are immutable):", e)

# Set: Create a set of student names from user input
student_input = input("Enter student names separated by commas: ")
students = set(student_input.split(","))
print("Original set:", students)

# Add a duplicate name
duplicate_name = input("Enter a duplicate student name to add: ")
students.add(duplicate_name)
print("After adding duplicate '{}':".format(duplicate_name), students)

# Dictionary: Person details from user input
name = input("Enter person's name: ")
age = int(input("Enter person's age: "))
email = input("Enter person's email: ")

person = {
    "name": name,
    "age": age,
    "email": email
}
print("Original dictionary:", person)

# Update email
new_email = input("Enter a new email to update: ")
person["email"] = new_email

# Print all keys and values
print("Updated dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")


# --- Part B: Control Flow ---

# Loop to print odd or even from 1 to 20
print("\nOdd or Even from 1 to 20:")
for num in range(1, 21):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# Iterate over dictionary keys and values
print("\nIterating over person dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Student grade checker
try:
    grade = int(input("\nEnter student grade (0-100): "))
    if grade >= 80:
        print("Grade: A")
    elif grade >= 70:
        print("Grade: B")
    elif grade >= 60:
        print("Grade: C")
    elif grade >= 50:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError:
    print("Invalid input. Please enter a numeric grade.")
