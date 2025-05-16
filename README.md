
# Student Seminar On Author - Allocation System

## Overview

This `Console(CLI)` Based Python Project allows each student in a class to uniquely select one author from a predefined list of 118 authors to present a seminar on. It validates student inputs, ensures no two students can choose the same author, and records all selections in an Excel file.

## Key Features

### 1. Robust Input Validation
- *Name*: Must contain only alphabets and at most one space.
- *Roll Number*: Must follow the pattern for first-year students as per our College, (e.g., starts with 24RA1A.... and is 10 characters long).
- *Branch*: Only specific branches (CSE, CSD, CSM, ECE, MECH, CIVIL) are allowed.
- *Section*: Only valid sections (A, B, C, D, E, F) are accepted.

### 2. *Author Selection*
- Authors are displayed in a formatted table with corresponding unique Codes/Numbers.
- Students must enter the Code/Number of the author they wish to choose.
- Once selected, the author is removed from the available Pool/List.

### 3. *Data Persistence*
- Student responses are saved to an Excel file named StudentsAuthorsChoosenList.xlsx.
- On the first run, the Excel file is created; subsequent runs append new student entries.
- Author availability is maintained across sessions by overwriting:
  - availableDictionaryOfAuthours.py
  - remainingAuthourCodes.py
  - siNo.py (serial number tracker)

### 4. *Excel Integration*
- I Had Used `pandas` and `openpyxl` to write student information and chosen authors to Excel.

### 5. *Sequential Record-Keeping*
- Maintains a serial number (SI.No) for each entry and auto-increments it every time the script is run.

---



## Setup Instructions

1. *Clone the repository*
```bash
git clone https://github.com/Laxminayanan/Choosing-Authours-By-Students.git
```
2. Install required libraries
```bash
pip install pandas openpyxl
```
3. Run the script
```bash
python main.py
```

---

# Example Output: 
```
Enter Your Name: John Doe
Enter Your Full Roll Number like (24RA1A....): 24RA1A1234
Enter Your Branch (CSE/CSD/CSM/ECE/MECH/CIVIL): cse
Enter Your Section (A/B/C/D/E/F): a

These Are The List of Authors Avaiable Right Now!

Corresponing Code Of The Authour   |  Authour Name
---------------------------------------------------
1                                  |  William Shakespeare
...
So Now, Please Enter The Authour Code On Whom You Want To Give The Seminar: 1

Choosen Authour: William Shakespeare and His Correspondoing code: 1
All Your Responses Has Been Saved In Our DataBase🎊🎉, You can Leave! Thank You For Your Patience😊!

```
---

-  `This Project was created as part of a mini-project to streamline and digitize seminar author selection for students in a classroom environment.`
---

# Use Case Flexibility:

- While originally I designed This system for assigning authors to students for seminar presentations,along That this Console Based System is versatile and can be repurposed for a variety of selection-based academic tasks. For example, Supporting Teaching Staff can predefine a list of seminar topics, and students can use the same interface to select a unique topic from the list. This makes the system broadly applicable for organizing topic-based assignments, project selections, or any scenario requiring unique student choices from a predefined pool—ensuring fairness, avoiding duplication, and maintaining well-structured records.

