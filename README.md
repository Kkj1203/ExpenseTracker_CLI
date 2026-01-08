# 💰 Expense Tracker (CLI-Based)

A simple **Command Line Expense Tracker** built using **Python** that allows users to record daily expenses and view category-wise summaries.  
The data is stored locally using a JSON file, making the project lightweight and easy to extend.

---

## 📌 Features

- Add daily expenses with:
  - Date
  - Category
  - Amount
- Automatically stores data in a JSON file
- View total expenses grouped by category
- User-friendly menu-driven CLI interface
- Persistent data storage (expenses are not lost after program exit)

---

## 🛠 Tech Stack

- **Language:** Python  
- **Storage:** JSON file (`expenses.json`)  
- **Libraries Used:**
  - `json`
  - `datetime`

---
ExpenseTracker/
│
├── expense_tracker.py # Main Python script
├── expenses.json # Stores expense data
└── README.md # Project documentation


---

## 🗄 Data Format (expenses.json)

Expenses are stored as a list of records in the following format:

```json
[
    {
        "date": "2002-03-12",
        "category": "horror",
        "amount": 1000.0
    },
    {
        "date": "2000-04-16",
        "category": "travel",
        "amount": 1200.0
    }
]
```

## ▶ How to Run the Project
Make sure Python 3 is installed on your system
Clone or download this repository
Open a terminal in the project folder

Run the script:
python expense_tracker.py

## 📋 How It Works
Menu Options
1. Add Expense
2. View Summary
3. Exit

- Add Expense
- Enter date (or leave blank to use today’s date)
- Enter category (Food, Travel, Shopping, etc.)
- Enter amount
- View Summary
- Displays total expenses grouped by category

## 🚀 Future Enhancements

- Monthly and yearly expense reports
- Export data to CSV
- Budget limits and alerts
- Category-wise charts
- Delete or edit existing expenses

## 📌 Note

This project is ideal for:
Python beginners
Practicing file handling
Understanding basic CLI applications
Learning JSON-based persistence
## 📂 Project Structure

