#CIS 103: Introduction to Programming
#Lab 01: "Getting Started with Python"
#Instructor: Md Ali
#Date: 08/24/2024
#Student: Pierina Brito
#Description: Simple Python Scrit


def main():

#Getting a greeting message
    print("Hello, Word!")
    print("How are you?")

#Getting user's name & age optional
    name = input("Enter your name: ")
   # age = int(input("Enter your age: "))

#Years old calculator
    current_year = int(input("Enter the current year: "))
    birth_year = int(input("Enter your birth year: "))
    years_old = current_year-birth_year
    print(f"You are {years_old} years old")
    print(f"Thank you {name}! and you are {years_old} years old")


if __name__ == "__main__":
    main()

