# Python PDBC Contact Book

## Description
Python Database Connectivity (PDBC) Contact Book is a console-based application built with **Python** and **MySQL**.  
It demonstrates **CRUD operations** (Create, Read, Update, Delete) on a contact list using **PyMySQL**.  
The data is stored in a **MySQL database**, and the output is displayed in a **clean tabular format** using **PrettyTable**.

## Features
- Add new contacts (name & phone number)
- View all contacts in a formatted table
- Update a contact’s phone number
- Search contacts by name or phone
- Delete contacts
- Handles input validation for IDs and phone numbers
- Uses **AUTO_INCREMENT** for unique contact IDs

## Requirements
- Python 3.x  
- MySQL Server  
- Python modules:  
  - `pymysql`  
  - `prettytable`  

Install required modules:
```bash
pip install pymysql prettytable
