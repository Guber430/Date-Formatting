# Date Formatting and Standardization Program 📅

This Python program is designed to **standardize date inputs** from multiple formats into a consistent `YYYY-MM-DD` format. It supports two common date formats: `MM/DD/YYYY` and `Month DD, YYYY`, with input validation and error handling to ensure proper formatting and user-friendly feedback.

---

## Project Overview

The program:
- **Supports multiple date formats**: It can process both `MM/DD/YYYY` and `Month DD, YYYY` formats.
- **Validates user input**: Ensures the date entered is in the correct format and provides meaningful error messages for invalid input.
- **Converts dates to a consistent format**: After validation, the program converts all valid dates to the `YYYY-MM-DD` format, making them easy to process and compare.

---

## Key Features

- **Multiple Format Handling**  
  The program can handle both `MM/DD/YYYY` and `Month DD, YYYY` formats, allowing flexibility in user input.

- **Input Validation**  
  Built-in checks ensure that dates are entered correctly. Invalid inputs trigger helpful error messages for users to correct the input.

- **Consistent Output**  
  Converts all valid dates to the `YYYY-MM-DD` format, standardizing dates for consistent processing.

- **Error Handling**  
  Catches invalid inputs and ensures the user is prompted to re-enter the date in a valid format.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**: `datetime` for date manipulation and validation
- **Error Handling**: Ensures that all user inputs are validated and provides clear error messages for corrections.

---

## How to Use

**Clone the Repository**

Clone the project to your local machine:

```bash
git clone https://github.com/yourusername/Date-Formatting.git
cd Date-Formatting
