# Student Data Analyzer

A simple command-line Python project for managing student exam records using a CSV file.  
It lets you add students, validate input marks, calculate averages, view top performers and display table data cleanly.

## Features

- Add student records (name, roll number, subject marks)
- Validates marks between 1 and 100
- Calculates:
  - Class average score
  - Individual student percentage
- Finds top 5 students based on percentage
- Displays number of rows and first 5 entries
- Creates a default CSV file automatically if the file doesn't exist
- Uses clean menu-based user interface

## How It Works

1. Enter the path of an existing CSV file  
2. If the file doesn't exist, the program creates a new one
3. Choose from a menu:
   - Add student
   - Calculate averages
   - Show top performers
   - Display data
   - Exit

The data is stored in simple CSV format, so you can open it in Excel anytime.

## Technologies Used

- Python
- CSV module
- Basic file handling and data validation

## Why I Built This

I created this project to practice:
- Working with CSV files
- Validating user input
- Implementing menu-driven applications
- Understanding basic data analysis logic

This small project helped me improve my Python skills and understand how real data processing works.

## Future Improvements

- Edit or delete student records
- Search by name or roll number
- Export data in different formats
- Replace menu system with a GUI 

## How to Run

```bash
python student_data.py
