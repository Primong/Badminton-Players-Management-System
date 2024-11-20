# Spartan Shuttlers: Badminton Players Management System

Badminton Player Management System is a program that allow users to manage player information through various functionalities such as adding, viewing, searching, updating, and deleting player details. 

# Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Explanation of how Python concepts, libraries, etc. were applied](#Explanation-of-how-Python-concepts,-libraries,-etc.-were-applied)
   - [Object-Oriented Programming (OOP)](#object-oriented-programming-(oop))
   - [Data Structures](#data-structures)
   - [Input Validation](#input-validation)
   - [Methods and Functions](#methods-and-functions)
   - [String Manipulation](#string-manipulation)
   - [Control Flow](#control-flow)
   - [Gender Statistics](#gender-statistics)
   - [Error Handling](#error-handling)
   - [Main Program Execution](#main-program-execution)
4. [SDG 5 Gender Equality](#sdg-5-gender-equality)
5. [Instructions for running the program](#instructions-for-running-the-program)

# l. Project Overview
The Badminton Player Management System is a console-based application designed to help manage and maintain a list of badminton players. This system allows administrators to add, view, update, delete, and search for players based on unique identifiers. It also includes a feature to display gender statistics, showing the number of male and female players in the system. The system is designed to be user-friendly, offering a simple menu interface to perform various actions related to player data management.

# ll. Features
Add a Player

View All Players

Search for a Player

Update Player Information

Delete a Player

Display Gender Statistics

Exit the System

# lll. Explanation of how Python concepts, libraries, etc. were applied
### Object-Oriented Programming (OOP)
1.1 The system utilizes two classes: Player and BadmintonPlayerManagementSystem. OOP principles like encapsulation were applied.

1.2 Encapsulation: The player data is encapsulated inside the Player object, and the system is responsible for managing multiple players.

### Data Structures
2.1 Lists: The player information is stored in a list (self.players), where each element is an instance of the Player class. This allows dynamic management and retrieval of player data.

### Input Validation
3.1 Input Handling and Validation: The system handles user input through the input() function and performs validation to ensure that the inputs for age, rank, and gender are valid. This is done using try-except blocks to catch invalid values (e.g., non-integer values for age or rank).

3.2 While Loops: These are used to repeatedly ask the user for input until valid data is entered. This ensures that the system is robust and prevents invalid data entry.

### Methods and Functions
4.1 Methods: Functions are defined as methods inside the classes to carry out specific tasks like adding a player (add_player()), viewing players (view_players()), searching for a player (search_player()), and updating player details (update_player()).

### String Manipulation
5.1 String Formatting: Python's string formatting (f"...") is used to generate readable and user-friendly output when displaying player details. This helps present player information in a clear, readable format.

### Control Flow
6.1 Conditional Statements: if-else statements are used to check conditions, such as whether a player is found during the search or update process. For example, if the user enters an invalid ID, the system informs the user that no such player exists.

### Gender Statistics
7.1 Gender Statistics: The show_gender_statistics() method counts and displays the number of male and female players. This is done using Python's sum() function combined with list comprehensions. It iterates over the self.players list and counts the gender occurrences.

### Error Handling
8.1 Try-Except: Error handling is employed to prevent the program from crashing due to invalid input. For example, if a user enters a non-integer value for the player’s age or rank, the program will catch the error and ask for the input again. This ensures the program remains robust.

### Main Program Execution
9.1 The system starts by creating an instance of the BadmintonPlayerManagementSystem class and calling the run() method, which keeps the system running and waiting for user input.

# lV. SDG 5 Gender Equality
The Sustainable Development Goal (SDG) chosen for integration into the Badminton Player Management System is SDG 5: Gender Equality.

- **Target**: Achieve gender equality and empower all women and girls.
- **Goal**: End all forms of discrimination against women and girls everywhere, eliminate violence, and ensure equal participation in leadership and decision-making processes. This goal also emphasizes equal access to education, healthcare, decent work, and the benefits of economic development for all genders.
- **Purpose**: The system’s ability to track and report on gender statistics could be used by sports organizations to assess gender equality within the sport. For example, if a sports federation notices that there are significantly fewer female players, they may decide to implement programs to encourage more women to participate in badminton.
- **Impact**: This can guide the development of programs that focus on improving female participation in badminton, encouraging sports authorities to create gender-specific training programs, leagues, or funding opportunities to increase female representation.
- **Promoting Female Athlete Participation**: Through visible gender statistics, the system could also promote initiatives that encourage more female athletes to enter competitive badminton, thus advancing gender equality in the sport.

# V. Instructions for running the program
