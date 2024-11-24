# Spartan Shuttlers: Badminton Players Management System

Badminton Player Management System is a program that allow users to manage players, tournaments, and matches, providing features to add, view, update, and delete players, tournaments, and matches, as well as track gender statistics through a command-line interface 

# Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Explanation of how Python concepts, libraries, etc. were applied](#Explanation-of-how-Python-concepts,-libraries,-etc.-were-applied)
- [Classes and Objects](#classes-and-objects)
- [Methods and Functionality](#methods-and-functionality)
- [Input Validation and Error Handling](#Input-validation-and-error-handling)
- [Data Storage](#data-storage)
- [String Formatting](#string-formatting)
- [Control Flow](#control-flow)
- [User Interaction](#user-interaction)
4. [SDG 5 Gender Equality](#sdg-5-gender-equality)
5. [Instructions for running the program](#instructions-for-running-the-program)

# l. Project Overview
The Badminton Player Management System is a Python-based application designed to streamline the management of players, tournaments, and matches in the sport of badminton. This system allows users to easily add, view, and update information related to players, tournaments, and matches, providing a comprehensive solution for managing badminton events and player statistics.

# ll. Features
Add a Player

View All Players

Add Tournament

View Tournaments

Add Match

View Matches

Update Player Information

Delete a Player

Display Gender Statistics

# lll. Explanation of how Python concepts, libraries, etc. were applied
## Classes and Objects
1.1. The system leverages Object-Oriented Programming (OOP) principles to define entities such as Player, Match, and Tournament.

1.2. Each entity is modeled using a class, encapsulating attributes and behaviors. For instance:
- The Player class stores player information (ID, name, age, rank, country, and gender).
- The Match class stores details of a match, including the players and the winner.
- The Tournament class stores tournament details and manages the matches within the tournament.

## Methods and Functionality
2.1. Methods within each class perform specific actions like adding a match to a tournament (add_match()), updating player details (update_player()), or displaying gender statistics (show_gender_statistics()).

2.2. Functions like get_player_by_id() and get_tournament_by_id() are used to retrieve specific objects from lists by ID, showcasing how functions and iteration work together.

## Input Validation and Error Handling
3.1. The system employs input validation using while loops and try-except blocks to ensure correct data is entered for numeric fields such as age, rank, and match ID.

3.2. This prevents runtime errors and guides the user to input data in the correct format, improving the user experience.

## Data Storage
4.1. he system uses lists (self.players, self.tournaments, self.matches) to store collections of Player, Tournament, and Match objects.

4.2. This allows the system to dynamically manage multiple players, tournaments, and matches. The use of lists facilitates easy iteration over objects to display data or apply operations, such as viewing all players or finding a player by ID.

## String Formatting
5.1 Python’s **f-string formatting** is used to generate formatted output, ensuring that details about players, matches, and tournaments are displayed neatly.

## Control Flow
6.1. The **while loop** is used in multiple places to repeatedly prompt the user for input until valid input is received (e.g., entering a valid player ID, rank, or age).

6.2. **If-else statements** are used to check user choices from the menu and navigate between different options, such as adding a player or viewing matches.

## User Interaction
7.1. The input() function is extensively used to interact with the user, accepting input for player details, match results, and other actions like adding tournaments or players. It also serves as the main method to accept user choices for navigating the system.

7.2. The print() function is used throughout the program to provide output to the user, displaying information about players, tournaments, matches, and statistics.

# IV. SDG 5 Gender Equality
Badminton Player Management System contributes to both **SDG 3 (Good Health and Well-Being)** and **SDG 5 (Gender Equality)** by promoting a healthy and active lifestyle through badminton, while also ensuring gender equality in sports.
- **SDG 3** is supported through the system’s facilitation of physical activity, mental well-being, and potential future features for tracking player health.
- **SDG 5** is enhanced by promoting equal opportunities for male and female athletes, helping to ensure gender equality in sports and empowering women and girls through their involvement in badminton.  

# V. Instructions for running the program
### Add a Player

- You will be asked to provide information such as the player's name, age, rank, country, and gender (M/F). The system will generate a unique player ID.

![Screenshot 2024-11-24 211115](https://github.com/user-attachments/assets/fb38900e-9824-4201-9eb2-99ff40e59ec9)

### View All Players

- Select option 2 to see a list of all players added so far.
  
![Screenshot 2024-11-24 211242](https://github.com/user-attachments/assets/26c85085-2788-459a-a1c2-86bb4e5d183d)

### Add Tournament

- Option 3 allows you to add a tournament by providing its name, date, and location.
  
![Screenshot 2024-11-24 211359](https://github.com/user-attachments/assets/ed55abeb-6b7c-4edf-8cd7-66eb2ca9fd26)

### View Tournaments

- Select option 4 to see a list of all Tournaments added so far.
  
![Screenshot 2024-11-24 211518](https://github.com/user-attachments/assets/dbe27bfb-3967-4377-b4a0-4eda05b1c3fc)

### Add Match

- Option 5 enables you to create a match between two players. You will need to select the players by their IDs and input the match details.
  
![Screenshot 2024-11-24 211627](https://github.com/user-attachments/assets/c4139b98-abda-4d44-a316-0992a688ced3)

### View Matches

- Select option 6 to view all the matches that have been added.
  
![Screenshot 2024-11-24 211710](https://github.com/user-attachments/assets/f854bebe-5156-466c-904d-497a5b88e157)

### Update Player Information

- Option 7 allows you to update a player's details such as name, age, country, and gender.

![Screenshot 2024-11-24 211802](https://github.com/user-attachments/assets/b434432c-7a5b-4e3a-aa12-f8002d6e243d)

### Delete a Player

- Option 8 enables you to remove a player from the system by their ID.

![Screenshot 2024-11-24 212044](https://github.com/user-attachments/assets/6f460ba0-bfcd-4edb-b9ee-97e632c53b93)

### Display Gender Statistics

- Option 9 will display the number of male and female players.

![Screenshot 2024-11-24 212023](https://github.com/user-attachments/assets/d0896ec1-70b5-4584-a710-c2b48ff392b7)

### Exit

- Option 10 allows you to exit the system.
