"""
File: car_management_system.py
Description: A menu-based Car Management System with database
Last modified: 22/11/2025
Version: 2.1

Contact: cameroncarlisle1992@gmail.com
"""

import re
import sys
import json
import os

DATA_FILE = "car_data.json"

class CarDatabase:
    """Class to manage car details with persistence."""

    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.cars = {}

# Persistence Methods
    def load_database(self):
        """Load car data from JSON file or return empty dict."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    self.cars = json.load(f)
                    print("Database loaded successfully.\n")
            except json.JSONDecodeError:
                print("Warning: Database file is corrupted. Starting new database.")
                self.cars = {}
        else:
            print("No existing database found. Starting new database.")
            self.cars = {}

    def create_new_database(self):
        """Start a fresh empty database, overwriting existing one if present."""
        self.cars = {}
        self.save_database()
        print("New database created.\n")

    def save_database(self):
        """Save current car data to JSON file."""
        with open(self.data_file, "w") as f:
            json.dump(self.cars, f, indent=4)

# Car Management Methods
    def add_car(self):
        valid_reg = r"^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$"

        while True:
            try:
                num_cars = int(input("How many cars would you like to add? "))
                break
            except ValueError:
                print("Please input numerical value only.")

        for i in range(num_cars):
            print(f"\nEnter details for car {i + 1} or press 5 to quit to menu:")

            while True:
                reg = input("Enter Registration Number: ").upper()
                if reg == "5":
                    return
                if re.match(valid_reg, reg):
                    if reg in self.cars:
                        print(f"A car with registration '{reg}' already exists.")
                        continue
                    break
                else:
                    print("Invalid UK registration. Try again or press 5.")

            make = self.get_car_detail("Enter Make: ")
            model = self.get_car_detail("Enter Model: ")

            while True:
                year = input("Enter Year: ").strip()
                if year.isdigit() and len(year) == 4:
                    break
                print("Please enter a valid 4-digit year.")

            self.cars[reg] = {"make": make, "model": model, "year": year}
            self.save_database()
            print("\nCar added successfully!\n")
            self.list_all_cars()

    def delete_car(self):
        while True:
            reg = input("Enter registration to delete or press 5 to quit: ").upper()
            if reg == "5":
                return
            if reg in self.cars:
                del self.cars[reg]
                self.save_database()
                print(f"Car '{reg}' deleted successfully.")
                return
            else:
                print("Registration not found. Try again.")

    def find_car(self):
        while True:
            reg = input("Enter registration to find or press 5 to quit: ").upper()
            if reg == "5":
                return
            if reg in self.cars:
                car = self.cars[reg]
                print("\n--- Car Details ---")
                print(f"Registration: {reg}")
                print(f"Make: {car['make']}")
                print(f"Model: {car['model']}")
                print(f"Year: {car['year']}")
                print("------------------\n")
                return
            else:
                print("Car not found. Try again.")

    def list_all_cars(self):
        if not self.cars:
            print("\nDatabase is currently empty.\n")
            return
        print("\n--- All Cars in Database ---")
        for reg, car in self.cars.items():
            print(f"Registration: {reg}")
            print(f"Make: {car['make']}")
            print(f"Model: {car['model']}")
            print(f"Year: {car['year']}")
            print("-" * 30)
        print()

    @staticmethod
    def get_car_detail(prompt):
        while True:
            detail = input(prompt).strip().capitalize()
            if detail:
                return detail
            print("Field cannot be empty.")

# Menu / Program Flow
def main():
    db = CarDatabase()

    # Startup choice: load existing or create new
    if os.path.exists(DATA_FILE):
        while True:
            choice = input(
                "Database exists. Load existing database or create new? (L/N): "
            ).strip().upper()
            if choice == "L":
                db.load_database()
                break
            elif choice == "N":
                db.create_new_database()
                break
            else:
                print("Please enter 'L' to load or 'N' to create new database.")
    else:
        db.create_new_database()

    # Main menu loop
    while True:
        print("\nCar Management System\n")
        print("1. Add Car Details")
        print("2. Delete Car Details")
        print("3. Find Car Details")
        print("4. Show All Car Details")
        print("5. Exit\n")

        choice = input("Please select an option: ").strip()

        if choice == "1":
            db.add_car()
        elif choice == "2":
            db.delete_car()
        elif choice == "3":
            db.find_car()
        elif choice == "4":
            db.list_all_cars()
        elif choice == "5":
            print("Exiting program...")
            db.save_database()
            sys.exit()
        else:
            print("Invalid selection. Please choose a valid option.")

if __name__ == "__main__":
    main()
