# Employee Management System

## Overview

This is a simple command-line Employee Management System implemented in Python. The system allows a company to manage information about their employees and departments using Object-Oriented Programming (OOP) principles and data structures.

## Features

- **Employee Class**: Represents an employee with attributes for name, ID, title, and department.

- **Department Class**: Represents a department with attributes for the department name and a list of employees.

- **Company Class**: Represents the overall company, managing departments and employee data.

- **User Interaction**: Provides a menu for users to interact with the system. Users can add employees to departments, remove employees, display department details, and more.

- **Data Persistence (Optional)**: Allows saving company data to a file and loading it back into the system on startup.

## Usage

1. **Clone the Repository:**
   - ```bash
     git clone https://github.com/RachanaSonu/East_vantage.git
     ```

2. **Run the Program:**
   - ```bash
     python employee_management.py
     ```

3. **Menu Options:**
   - Enter the respective number to perform the desired operation.
   - Options include adding/removing departments, adding/removing employees, listing employees in a department, saving/loading data, and quitting the program.

4. **Data Persistence (Optional):**
   - When saving data, enter the filename to save the company data to a file.
   - When loading data, enter the filename to load existing data into the system.

## Requirements

- Python 3.x

## Installation

   ```bash
   pip install -r requirements.txt
