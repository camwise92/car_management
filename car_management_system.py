"""
File: car_management_system.py
Description: A menu-based interface to add, delete, and find car details
Date created: 15/01/2025
Last modified: 29/01/2025
Version: 1.1

Contact: cameroncarlisle1992@gmail.com
"""

import re  # used for regex
import sys  # used to exit program with message

car_details = {} # Empty dictionary to add car details to.

def main():
    """
    Display menu and execute functions based on menu selection.
    """
    while True:
        menu()
        
        menu_selection = input("Please select option from menu: ").strip()
        if menu_selection == "1":
            add_car()
        elif menu_selection == "2":
            delete_car()
        elif menu_selection == "3":
            find_car()
        elif menu_selection == "4":
            # Program exits with message
            sys.exit("Exiting Program.")
        else:
            # Error message if input is invalid
            print("Invalid selection. Please choose a valid option.")

def menu(): 
    """
    Displays menu options.
    """
    print("\nCar Management System\n")
    print("1. Add Car Details")
    print("2. Delete Car Details")
    print("3. Find Car Details")
    print("4. Exit Application\n")

def add_car():
    """
    Add car details to the car_details dictionary.

    This function prompts the user to input the number of cars to add,
    and then for each car, it gathers details such as registration number,
    make, model, and year. Validates inputs and handles duplicates.
    """
    valid_reg = r"^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$"  # RegEx for valid UK license pattern

    while True:
        # Loop until valid input given (numerical values only)
        try:
            num_cars = int(input("How many cars would you like to add? "))
            break
        except ValueError:
            print("Please input numerical value only.")  # Error message if input invalid

    for i in range(num_cars):
        print(f"\nEnter details for car {i + 1} or press 4 to quit to menu:")
        
        while True:
            reg = input("Enter Registration Number: ").upper()
            if re.match(valid_reg, reg):  # Checks input against valid pattern
                break
            elif reg == "4":
                break
            else:
                print("Please enter a valid UK registration number or press 4 to quit to menu.")  # Error message if input invalid
        
        if reg == "4":
            break       
        if reg in car_details:
            print(f"A car with registration number '{reg}' already exists.")  # If reg already exists, don't log the details
        else:   
            make = get_car_detail("Enter Make: ")
            model = get_car_detail("Enter Model: ")

            while True:
                year = input("Enter Year: ").strip()
                if year.isdigit() and len(year) == 4:  # Check if it's a 4-digit year
                    break
                else:
                    print("Please enter a valid 4-digit year.")
            
            car_details[reg] = {"make": make, "model": model, "year": year}
            print("Car details added successfully.")
            print(car_details)

def delete_car():
    """
    Delete car details from the car_details dictionary.

    This function prompts the user to input the registration number of the car 
    to be deleted. It checks if the registration number exists in the dictionary 
    and deletes it if found.
    """
    while True:
        reg = input("Please enter registration of car you wish to delete from database: ").upper()    
        if reg in car_details:
            del car_details[reg]
            print(f"Car: {reg}, successfully deleted.")
            break
        elif reg == "4":
            break
        else:
            print("Registration not in database.")

def find_car():
    """
    Find and display car details from the car_details dictionary.

    This function prompts the user to input the registration number of the car 
    to be found. It checks if the registration number exists in the dictionary 
    and displays the details if found.
    """
    while True:
        car = input("Please input registration of car or press 4 to quit to menu: ").upper()
        if car in car_details:
            print(f"\nRegistration: {car}\nMake: {car_details[car]['make']}\nModel: {car_details[car]['model']}\nYear: {car_details[car]['year']}\n")
            break
        elif car == "4":
            break
        else:
            print("Car not found. Please try again or enter valid registration.\n")

def get_car_detail(prompt):
    """
    Helper function to get car details (Make, Model) and ensure non-empty input.

    Parameters:
    prompt (str): The prompt to display to the user.

    Returns:
    str: The user's input, stripped of leading/trailing whitespace and capitalized.
    """
    while True:
        detail = input(prompt).strip().capitalize()
        if detail:
            return detail
        else:
            print("This field cannot be empty. Please enter a valid detail.")

if __name__ == "__main__":
    main()