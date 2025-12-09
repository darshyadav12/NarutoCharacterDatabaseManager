
# Naruto Character Database Manager
![Naruto GIF](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW52NGM1OWg5cnR6bmU5Y3pmZGtpYmoxa3JscGVpZmpxdHBqd2JhZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohc0PsZLDN5Dgcf5e/giphy.gif)
A Python + MySQL project for managing a custom database of Naruto characters.
This project was created as a school SQL project and includes complete CRUD functionality with a simple, menu-driven interface.
## Features

### Create Database and Table
Automatically sets up:
- Database: NarutoCharacters
- Table: Characters
### Insert Character Data
Add multiple Naruto characters with attributes:
- Serial Number
- Name
- Village
- Clan
- Chakra Type
- Summoning Animal
- Ninja Rank
### Display Stored Data
Multiple display options:
- Entire table
- Search by village
- Search by name
- Search by clan
### Update Character Details
Update any of these fields:
- Name
- Village
- Clan
- Chakra Type
- Summoning Animal
- Ninja Rank
### Delete Records
Delete characters by name.
### User-Friendly Menu
Menu-driven CLI for smooth navigation.


## How It Works
Every run displays this menu:
- 1.) Create Database & Table 
- 2.) Insert Data  
- 3.) Display  
- 4.) Update 
- 5.) Delete  
- 6.) Exit
## Installation

### 1.) Install MySQL Server
Make sure MySQL is installed and running on your system.
### 2.) Install Python Packages
``` bash
pip install mysql-connector-python
```
### 3.) Update MySQL Credentials
``` python
mydb = my_sql.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD"
)
```
### 4.) Run the Program
``` bash
python naruto_db_manager.py
```

## Tech Stack

- Python 3(mysql.connector)
- MySQL Database
- Command-line Interface (CLI)


## Lessons Learned

- Understood how to connect Python with MySQL using mysql.connector.
- Learned to create, manage, and query databases and tables in SQL.
- Gained experience in implementing full CRUD operations.
- Improved handling of user input through a menu-driven CLI.
- Practiced writing modular Python functions for cleaner structure.
- Strengthened debugging skills while testing database operations.
- Learned to design a simple but functional real-world database system.


## Future Improvements
- GUI using Tkinter or PyQt
- Export to CSV
- Search by Chakra type or Ninja Rank
- Add Jutsu lists
- Add authentication system


## Contributing

Contributions are always welcome!
Feel free to fork the repo and add more Naruto characters or features!


## License

This is a school project and free for educational use.

