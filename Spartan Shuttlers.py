class Player:
    def __init__(self, player_id, name, age, rank, country, gender):
        # Initialize the player object with the provided attributes
        self.player_id = player_id  # Unique identifier for each player
        self.name = name            # Name of the player
        self.age = age              # Age of the player
        self.rank = rank            # Ranking of the player
        self.country = country      # Country of the player
        self.gender = gender        # Gender of the player ('M' or 'F')

    def __str__(self):
        # Return a formatted string to display player details
        return f"ID NUMBER: {self.player_id}, Name: {self.name}, Age: {self.age}, Rank: {self.rank}, Country: {self.country}, Gender: {self.gender}"

class BadmintonPlayerManagementSystem:
    def __init__(self):
        # Initialize the management system with an empty player list and the next player ID
        self.players = []          # List to store all player objects
        self.next_player_id = 1    # Player IDs start from 1 and increment for each new player

    def add_player(self):
        # Function to add a new player to the system
        print("******************************")
        print("Enter player Information:")
        
        # Get player details from user input
        name = input("Name: ")

        # Validate and get age input
        while True:
            try:
                age = int(input("Age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid age.")

        # Validate and get rank input
        while True:
            try:
                rank = int(input("Rank (must be a number): "))
                if rank <= 0:
                    raise ValueError("Rank must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid rank.")

        # Get country input
        country = input("Country: ")

        # Validate and get gender input
        while True:
            gender = input("Gender (M/F): ").strip().lower()
            if gender in ['m', 'f']:  # Only 'M' or 'F' are accepted
                gender = gender.capitalize()  # Capitalize the input ('m' -> 'M', 'f' -> 'F')
                break
            else:
                print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

        # Create a new player object and add it to the player list
        player = Player(self.next_player_id, name, age, rank, country, gender)
        self.players.append(player)
        self.next_player_id += 1  # Increment the player ID for the next player

        print(" ")
        print("-------------------------------------")
        print(f"Player {name} added successfully!")
        print("-------------------------------------")

    def view_players(self):
        # Function to display all players in the system
        if not self.players:
            print("No players found.")  # If there are no players, display this message
            return
        print("\nLIST OF THE PLAYERS:")
        for player in self.players:
            print(player)  # Print each player's details

    def search_player(self):
        # Function to search for a player by their ID
        while True:
            try:
                print("**************")
                player_id = int(input("Enter player ID NUMBER to search: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        # Retrieve the player by ID and display their information
        player = self.get_player_by_id(player_id)
        if player:
            print(player)
        else:
            print(f"No player found with ID: {player_id}")  # If player is not found, display this message

    def update_player(self):
        # Function to update an existing player's information
        while True:
            try:
                print("******************************")
                player_id = int(input("Enter player ID to update: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        # Retrieve the player to be updated by ID
        player = self.get_player_by_id(player_id)
        if player:
            print("Update player Information:")

            # Prompt user for updated name (or keep the existing name if no input is given)
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

            # Update country if necessary
            player.country = input(f"Country ({player.country}): ") or player.country

            # Update gender with validation, keeping the existing gender if no new input is given
            while True:
                gender = input(f"Gender ({player.gender}): ").strip().lower()
                if gender in ['m', 'f', '']:  # Allow empty input to keep the existing gender
                    player.gender = gender.capitalize() if gender else player.gender
                    break
                else:
                    print("Invalid input. Please enter 'M' for Male or 'F' for Female.")
            
            print("\nPLAYER INFORMATION UPDATED SUCCESSFULLY!")
        else:
            print(f"No player found with ID Number: {player_id}")

    def delete_player(self):
        # Function to delete a player by their ID
        while True:
            try:
                player_id = int(input("Enter player ID Number to delete: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID.")

        # Retrieve the player by ID
        player = self.get_player_by_id(player_id)
        if player:
            self.players.remove(player)  # Remove the player from the list
            print(" ")
            print(f"Player with ID NUMBER {player_id} deleted successfully!")
        else:
            print(f"No player found with ID Number: {player_id}")  # If player is not found, display this message

    def get_player_by_id(self, player_id):
        # Function to find a player by their ID
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None  # Return None if the player with the given ID doesn't exist

    def display_menu(self):
        # Function to display the main menu with options
        print("\nWelcome Players!")
        print("Badminton Players Management System")
        print("1. Add a Player")
        print("2. View All Players")
        print("3. Search for a Player")
        print("4. Update Player Information")
        print("5. Delete a Player")
        print("6. Display Gender Statistics")
        print("7. Exit")

    def show_gender_statistics(self):
        # Function to display gender statistics (count of male and female players)
        male_count = sum(1 for player in self.players if player.gender == 'M')
        female_count = sum(1 for player in self.players if player.gender == 'F')

        print("\nGENDER STATISTICS:")
        print(f"Male Players: {male_count}")
        print(f"Female Players: {female_count}")

    def run(self):
        # Main function to run the system and process user input
        while True:
            self.display_menu()
            choice = input("Enter your choice number: ")

            # Call the corresponding function based on the user's choice
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
                print("Exiting the system...")
                break  # Exit the system
            else:
                print("Invalid number. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    # Instantiate the system and run it
    system = BadmintonPlayerManagementSystem()
    system.run()
