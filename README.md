# Car Management System

A menu-based interface for managing car details. This application allows users to add, delete, and find car details such as registration number, make, model, and year. Built with Python, it includes input validation, regex for UK registration patterns, and a simple, interactive command-line interface.

## Features

- **Add Car Details**: Input and store details for multiple cars.
- **Delete Car Details**: Remove car details using the registration number.
- **Find Car Details**: Search and display car details using the registration number.
- **Input Validation**: Ensures only valid inputs are accepted.
- **Regex Validation**: Checks for valid UK registration number patterns.

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/car-management-system.git
    ```
2. Navigate to the project directory:
    ```sh
    cd car-management-system
    ```

### Usage

1. Run the application:
    ```sh
    python car_management_system.py
    ```
2. Follow the on-screen instructions to add, delete, or find car details.

## Example

```sh
python car_management_system.py

Car Management System

1. Add Car Details
2. Delete Car Details
3. Find Car Details
4. Exit Application

Please select an option from the menu: 1

How many cars would you like to add? 1

Enter details for car 1 or press 4 to quit to menu:
Enter Registration Number: AB12 CDE
Enter Make: Toyota
Enter Model: Corolla
Enter Year: 2020
Car details added successfully.
