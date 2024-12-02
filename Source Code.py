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

# The main system class for managing badminton players.
class BadmintonPlayerManagementSystem:
    def __init__(self):
        self.players = []  # List to store all players
        self.next_player_id = 1  # Player ID counter
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

            # Check if the entered credentials are valid
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
        if not self.logged_in:  # Ensure the user is logged in
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
        if not self.logged_in:  # Ensure the user is logged in
            print("You need to log in first.")
            return

        if not self.players:  # Check if there are any players in the system
            print("No players found.")
            return

        print("\nLIST OF THE PLAYERS:")
        for player in self.players:
            print(player)

    # Method to search for a player by ID
    def search_player(self):
        if not self.logged_in:  # Ensure the user is logged in
            print("You need to log in first.")
            return

        # Input validation for player ID
        while True:
            try:
                print("**************")
                player_id = int(input("Enter player ID NUMBER to search: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        # Fetch player by ID and display information
        player = self.get_player_by_id(player_id)
        if player:
            print(player)
        else:
            print(f"No player found with ID: {player_id}")

    # Method to update the information of an existing player
    def update_player(self):
        if not self.logged_in:  # Ensure the user is logged in
            print("You need to log in first.")
            return

        # Input validation for player ID
        while True:
            try:
                print("******************************")
                player_id = int(input("Enter player ID to update: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        # Fetch player by ID to update their details
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
        if not self.logged_in:  # Ensure the user is logged in
            print("You need to log in first.")
            return

        # Input validation for player ID
        while True:
            try:
                player_id = int(input("Enter player ID Number to delete: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID.")

        # Find and remove the player from the list
        player = self.get_player_by_id(player_id)
        if player:
            self.players.remove(player)
            print(f"Player with ID NUMBER {player_id} deleted successfully!")
        else:
            print(f"No player found with ID Number: {player_id}")

    # Helper method to get a player by ID
    def get_player_by_id(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    # Method to display the main menu for the system
    def display_menu(self):
        print("\nWelcome to the Badminton Players Management System")
        print("1. Add a Player")
        print("2. View All Players")
        print("3. Search for a Player")
        print("4. Update Player Information")
        print("5. Delete a Player")
        print("6. View Gender Statistics")
        print("7. Logout")
        print("8. Exit")

    # Method to show gender statistics (male/female player count)
    def show_gender_statistics(self):
        male_count = sum(1 for player in self.players if player.gender == 'M')
        female_count = sum(1 for player in self.players if player.gender == 'F')

        print("\nGENDER STATISTICS:")
        print(f"Male Players: {male_count}")
        print(f"Female Players: {female_count}")

    # Main method to run the system
    def run(self):
        if not self.login():  # Attempt login before running the system
            return

        # Main loop for system menu and operations
        while True:
            self.display_menu()  # Display menu options
            choice = input("Enter your choice number: ")

            if choice == '1':
                self.add_player()
            elif choice == '2':
                self.view_players()
            elif choice == '3':
                self.search_player()
            elif choice == '4':
                self.update_player()
            elif choice == '5':
                self.delete_player()
            elif choice == '6':
                self.show_gender_statistics()
            elif choice == '7':
                self.logout()  # Log out the user and break the loop
                break
            elif choice == '8':
                print("Exiting the system...")
                break
            else:
                print("Invalid number. Please try again.")

# Run the system if this script is executed directly
if __name__ == "__main__":
    system = BadmintonPlayerManagementSystem()
    system.run()
