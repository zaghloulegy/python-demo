# Example of different data types, variables, functions, and loops

# Integer variable
age = 25

# Floating-point variable
height = 1.75

# String variable
name = "John Doe"

# Boolean variable
is_student = True

# Dictionary variable
person1 = {
    "name": name,
    "age": age,
    "height": height,
    "is_student": is_student
}

# Dictionary variable2
person2 = {
    "name": "Jane Smith",
    "age": 30,
    "height": 1.65,
    "is_student": False
}

# List variable
grades = [80, 90, 75, 95, 85]

# Function to calculate the average of a list
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Function to calculate the average of a list
def print_average_result(numbers):
    # Calling the calculate_average function and printing the result
    average = calculate_average(numbers)
    print("Average:", average)    

# Function to print all the grades in a list
def list_all_studets_grades(grades):
    # Looping over the grades list and printing each grade
    print("Grades:")
    for grade in grades:
        print(grade)

# Function to check if a person is a student
def is_person_student(person):
    # Checking if the person is a student and printing the result
    if person["is_student"]:
        print(person["name"], "is a student.")
    else:
        print(person["name"], "is not a student.")

# Printing all the grades in the grades list    
list_all_studets_grades(grades)
# Printing the average of the grades list
print_average_result(grades)
# Checking if the person is a student
is_person_student(person1)
# Checking if the person is a student
is_person_student(person2)