# The Player class represents a badminton player with their personal information.
class Player:
    def __init__(self, player_id, name, age, rank, country, gender):
        self.player_id = player_id  # Unique identifier for the player
        self.name = name  # Name of the player
        self.age = age  # Age of the player
        self.rank = rank  # Rank of the player
        self.country = country  # Country the player represents
        self.gender = gender  # Gender of the player

    # Method to return a string representation of the player object
    def __str__(self):
        return f"ID NUMBER: {self.player_id}, Name: {self.name}, Age: {self.age}, Rank: {self.rank}, Country: {self.country}, Gender: {self.gender}"

# The Tournament class represents a badminton tournament with matches
class Tournament:
    def __init__(self, tournament_id, name, location, date):
        self.tournament_id = tournament_id  # Unique identifier for the tournament
        self.name = name  # Name of the tournament
        self.location = location  # Location of the tournament
        self.date = date  # Date of the tournament
        self.matches = []  # List to store matches in this tournament

    def add_match(self, match):
        self.matches.append(match)

    def view_matches(self):
        if not self.matches:
            print(f"No matches scheduled for the tournament: {self.name}")
        else:
            for match in self.matches:
                print(match)

    def __str__(self):
        return f"Tournament ID: {self.tournament_id}, Name: {self.name}, Location: {self.location}, Date: {self.date}"

# The Match class represents a match between two players in a tournament
class Match:
    def __init__(self, match_id, player1, player2, date):
        self.match_id = match_id  # Unique identifier for the match
        self.player1 = player1  # Player 1 in the match
        self.player2 = player2  # Player 2 in the match
        self.date = date  # Date of the match
        self.result = None  # Result of the match (e.g., 'Player1 wins', 'Player2 wins', or 'Draw')

    def set_result(self, result):
        self.result = result

    def __str__(self):
        return f"Match ID: {self.match_id}, {self.player1.name} vs {self.player2.name} on {self.date}. Result: {self.result if self.result else 'Not Played Yet'}"

# The main system class for managing badminton players and tournaments
class BadmintonPlayerManagementSystem:
    def __init__(self):
        self.players = []  # List to store all players
        self.tournaments = []  # List to store all tournaments
        self.next_player_id = 1  # Player ID counter
        self.next_tournament_id = 1  # Tournament ID counter
        self.next_match_id = 1  # Match ID counter
        self.users = {
            'admin': 'admin123',  # Admin credentials for login
            'player1': 'player123'  # Player credentials for login
        }
        self.logged_in = False  # Boolean flag to check if a user is logged in
        self.current_user = None  # Store the currently logged-in user

    # Method to handle user login
    def login(self):
        print("\nLogin")
        attempts = 3  # Allow 3 login attempts
        while attempts > 0:
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if username in self.users and self.users[username] == password:
                print(f"Welcome {username}!")
                self.logged_in = True
                self.current_user = username  # Store the logged-in user
                return True
            else:
                attempts -= 1
                print(f"Invalid credentials. You have {attempts} attempt(s) left.")
        
        print("Too many failed attempts. Exiting.")
        return False

    # Method to handle user logout
    def logout(self):
        self.logged_in = False
        self.current_user = None
        print("You have logged out successfully.")

    # Method to add a new player to the system
    def add_player(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        print("******************************")
        print("Enter player Information:")

        name = input("Name: ")

        # Input validation for age
        while True:
            try:
                age = int(input("Age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid age.")

        # Input validation for rank
        while True:
            try:
                rank = int(input("Rank (must be a number): "))
                if rank <= 0:
                    raise ValueError("Rank must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid rank.")

        country = input("Country: ")

        # Gender input validation
        while True:
            gender = input("Gender (M/F): ").strip().lower()
            if gender in ['m', 'f']:
                gender = gender.capitalize()  # Capitalize gender input for uniformity
                break
            else:
                print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

        # Create a new Player object and add it to the players list
        player = Player(self.next_player_id, name, age, rank, country, gender)
        self.players.append(player)
        self.next_player_id += 1  # Increment the player ID counter

        print(f"Player {name} added successfully!")

    # Method to view all players in the system
    def view_players(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        if not self.players:
            print("No players found.")
            return

        print("\nLIST OF THE PLAYERS:")
        for player in self.players:
            print(player)

    # Method to search for a player by ID
    def search_player(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        while True:
            try:
                print("**************")
                player_id = int(input("Enter player ID NUMBER to search: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        player = self.get_player_by_id(player_id)
        if player:
            print(player)
        else:
            print(f"No player found with ID: {player_id}")

    # Helper method to get a player by ID
    def get_player_by_id(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    # Method to add a new tournament
    def add_tournament(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        print("******************************")
        print("Enter tournament Information:")

        name = input("Name: ")
        location = input("Location: ")
        date = input("Date: ")

        tournament = Tournament(self.next_tournament_id, name, location, date)
        self.tournaments.append(tournament)
        self.next_tournament_id += 1

        print(f"Tournament '{name}' added successfully!")

    # Method to view all tournaments
    def view_tournaments(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        if not self.tournaments:
            print("No tournaments found.")
            return

        print("\nLIST OF TOURNAMENTS:")
        for tournament in self.tournaments:
            print(tournament)

    # Method to add a match to a tournament
    def add_match(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        tournament_name = input("Enter the tournament name: ")
        tournament = next((t for t in self.tournaments if t.name == tournament_name), None)

        if not tournament:
            print(f"Tournament '{tournament_name}' not found.")
            return

        print("Enter match details:")
        player1_id = int(input("Enter player 1 ID: "))
        player2_id = int(input("Enter player 2 ID: "))
        match_date = input("Match date: ")

        player1 = next((p for p in self.players if p.player_id == player1_id), None)
        player2 = next((p for p in self.players if p.player_id == player2_id), None)

        if not player1 or not player2:
            print("One or both players not found.")
            return

        match = Match(self.next_match_id, player1, player2, match_date)
        tournament.add_match(match)
        self.next_match_id += 1

        print(f"Match between {player1.name} and {player2.name} added to tournament '{tournament_name}'.")

    # Method to view matches in a tournament
    def view_matches(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        tournament_name = input("Enter the tournament name: ")
        tournament = next((t for t in self.tournaments if t.name == tournament_name), None)

        if not tournament:
            print(f"Tournament '{tournament_name}' not found.")
            return

        print("\nLIST OF MATCHES:")
        tournament.view_matches()

    # Method to update the information of an existing player
    def update_player(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        while True:
            try:
                print("******************************")
                player_id = int(input("Enter player ID to update: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        player = self.get_player_by_id(player_id)
        if player:
            print("Update player Information:")

            player.name = input(f"Name ({player.name}): ") or player.name

            # Update age with validation
            while True:
                try:
                    age = input(f"Age ({player.age}): ") or player.age
                    age = int(age)
                    if age <= 0:
                        raise ValueError("Age must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid age.")

            # Update rank with validation
            while True:
                try:
                    rank = input(f"Rank ({player.rank}): ") or player.rank
                    rank = int(rank)
                    if rank <= 0:
                        raise ValueError("Rank must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid rank.")

            player.country = input(f"Country ({player.country}): ") or player.country

            # Update gender
            while True:
                gender = input(f"Gender ({player.gender}): ").strip().lower()
                if gender in ['m', 'f', '']:  # Allow empty input to keep current gender
                    player.gender = gender.capitalize() if gender else player.gender
                    break
                else:
                    print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

            print("PLAYER INFORMATION UPDATED SUCCESSFULLY!")
        else:
            print(f"No player found with ID Number: {player_id}")

    # Method to delete a player by ID
    def delete_player(self):
        if not self.logged_in:
            print("You need to log in first.")
            return

        while True:
            try:
                player_id = int(input("Enter player ID Number to delete: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID.")

        player = self.get_player_by_id(player_id)
        if player:
            self.players.remove(player)
            print(f"Player with ID NUMBER {player_id} deleted successfully!")
        else:
            print(f"No player found with ID Number: {player_id}")

    # Method to display the main menu for the system
    def display_menu(self):
        print("\nWelcome to the Badminton Players Management System")
        print("1. Add a Player")
        print("2. View All Players")
        print("3. Add a Tournament")
        print("4. View All Tournaments")
        print("5. Add a Match")
        print("6. View Matches in a Tournament")
        print("7. Update Player Information")
        print("8. Delete a Player")
        print("9. Logout")
        print("10. Exit")

    # Main method to run the system
    def run(self):
        if not self.login():
            return

        while True:
            self.display_menu()
            choice = input("Enter your choice number: ")

            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.view_players()
            elif choice == '3':
                self.add_tournament()
            elif choice == '4':
                self.view_tournaments()
            elif choice == '5':
                self.add_match()
            elif choice == '6':
                self.view_matches()
            elif choice == '7':
                self.update_player()
            elif choice == '8':
                self.delete_player()
            elif choice == '9':
                self.logout()
                break
            elif choice == '10':
                print("Exiting the system...")
                break
            else:
                print("Invalid number. Please try again.")

# Run the system if this script is executed directly
if __name__ == "__main__":
    system = BadmintonPlayerManagementSystem()
    system.run()
