# Class to represent a Player
class Player:
    def __init__(self, player_id, name, age, rank, country, gender):
        self.player_id = player_id  # Unique ID for the player
        self.name = name            # Name of the player
        self.age = age              # Age of the player
        self.rank = rank            # Rank of the player in the game
        self.country = country      # Country of the player
        self.gender = gender        # Gender of the player (M/F)

    # String representation of the Player class
    def __str__(self):
        return f"ID NUMBER: {self.player_id}, Name: {self.name}, Age: {self.age}, Rank: {self.rank}, Country: {self.country}, Gender: {self.gender}"

# Class to represent a Match between two players
class Match:
    def __init__(self, match_id, player1, player2, winner):
        self.match_id = match_id    # Unique ID for the match
        self.player1 = player1      # First player in the match
        self.player2 = player2      # Second player in the match
        self.winner = winner        # The winner of the match

    # String representation of the Match class
    def __str__(self):
        return f"Match ID: {self.match_id}, Player1: {self.player1.name}, Player2: {self.player2.name}, Winner: {self.winner.name}"

# Class to represent a Tournament
class Tournament:
    def __init__(self, tournament_id, name, date, location):
        self.tournament_id = tournament_id  # Unique ID for the tournament
        self.name = name                    # Name of the tournament
        self.date = date                    # Date of the tournament
        self.location = location            # Location of the tournament
        self.matches = []                   # List of matches in the tournament

    # Method to add a match to the tournament
    def add_match(self, match):
        self.matches.append(match)

    # String representation of the Tournament class
    def __str__(self):
        return f"Tournament ID: {self.tournament_id}, Name: {self.name}, Date: {self.date}, Location: {self.location}, Matches: {len(self.matches)}"

# Main class for managing the badminton player system
class BadmintonPlayerManagementSystem:
    def __init__(self):
        self.players = []              # List to store all player objects
        self.tournaments = []          # List to store all tournaments
        self.matches = []              # List to store all matches
        self.next_player_id = 1        # ID counter for players
        self.next_tournament_id = 1    # ID counter for tournaments
        self.next_match_id = 1         # ID counter for matches

    # Method to add a new player to the system
    def add_player(self):
        print("****************************")
        print("Enter player Information:")
        name = input("Name: ")
        
        # Validate and input age
        while True:
            try:
                age = int(input("Age: "))
                if age <= 0:
                    raise ValueError("Age must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid age.")

        # Validate and input rank
        while True:
            try:
                rank = int(input("Rank (must be a number): "))
                if rank <= 0:
                    raise ValueError("Rank must be a positive integer.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid rank.")

        country = input("Country: ")

        # Validate and input gender
        while True:
            gender = input("Gender (M/F): ").strip().lower()
            if gender in ['m', 'f']:
                gender = gender.capitalize()
                break
            else:
                print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

        # Create a new player object and add to the player list
        player = Player(self.next_player_id, name, age, rank, country, gender)
        self.players.append(player)
        self.next_player_id += 1

        print(f"Player {name} added successfully!")

    # Method to view all players
    def view_players(self):
        if not self.players:
            print("No players found.")
            return
        print("\nLIST OF THE PLAYERS:")
        for player in self.players:
            print(player)

    # Method to add a new tournament
    def add_tournament(self):
        print("****************************")
        print("Enter tournament Information:")
        name = input("Tournament Name: ")
        date = input("Tournament Date (YYYY-MM-DD): ")
        location = input("Tournament Location: ")

        # Create a new tournament object and add to the tournament list
        tournament = Tournament(self.next_tournament_id, name, date, location)
        self.tournaments.append(tournament)
        self.next_tournament_id += 1

        print(f"Tournament {name} added successfully!")

    # Method to view all tournaments
    def view_tournaments(self):
        if not self.tournaments:
            print("No tournaments found.")
            return
        print("\nLIST OF TOURNAMENTS:")
        for tournament in self.tournaments:
            print(tournament)

    # Method to add a match between two players
    def add_match(self):
        print("****************************")
        print("Enter match details:")
        while True:
            try:
                match_id = int(input("Match ID: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid match ID.")

        # Select Player 1 and Player 2
        print("\nSelect Player 1:")
        self.view_players()
        player1_id = int(input("Enter player ID for Player 1: "))
        player1 = self.get_player_by_id(player1_id)

        print("\nSelect Player 2:")
        self.view_players()
        player2_id = int(input("Enter player ID for Player 2: "))
        player2 = self.get_player_by_id(player2_id)

        # Check if both players exist and determine the winner
        if player1 and player2:
            print("\nEnter Winner:")
            winner_id = int(input("Enter the ID of the winner: "))
            winner = player1 if winner_id == player1.player_id else player2
            match = Match(self.next_match_id, player1, player2, winner)
            self.matches.append(match)
            self.next_match_id += 1
            print(f"Match between {player1.name} and {player2.name} added. Winner: {winner.name}")
        else:
            print("Invalid player IDs.")

    # Method to view all matches
    def view_matches(self):
        if not self.matches:
            print("No matches found.")
            return
        print("\nLIST OF MATCHES:")
        for match in self.matches:
            print(match)

    # Helper method to find a player by their ID
    def get_player_by_id(self, player_id):
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

    # Helper method to find a match by its ID
    def get_match_by_id(self, match_id):
        for match in self.matches:
            if match.match_id == match_id:
                return match
        return None

    # Helper method to find a tournament by its ID
    def get_tournament_by_id(self, tournament_id):
        for tournament in self.tournaments:
            if tournament.tournament_id == tournament_id:
                return tournament
        return None

    # Display menu options for the user
    def display_menu(self):
        print("\nWelcome Players!")
        print("Badminton Players Management System")
        print("1. Add a Player")
        print("2. View All Players")
        print("3. Add Tournament")
        print("4. View Tournaments")
        print("5. Add Match")
        print("6. View Matches")
        print("7. Update Player Information")
        print("8. Delete a Player")
        print("9. Display Gender Statistics")
        print("10. Exit")

    # Display gender statistics for players
    def show_gender_statistics(self):
        male_count = sum(1 for player in self.players if player.gender == 'M')
        female_count = sum(1 for player in self.players if player.gender == 'F')

        print("\nGENDER STATISTICS:")
        print(f"Male Players: {male_count}")
        print(f"Female Players: {female_count}")

    # Main function to run the system
    def run(self):
        while True:
            self.display_menu()  # Show the menu to the user
            choice = input("Enter your choice number: ")

            # Process user choice
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
                self.show_gender_statistics()
            elif choice == '10':
                print("Exiting the system...")
                break
            else:
                print("Invalid number. Please try again.")

    # Method to update a player's information
    def update_player(self):
        while True:
            try:
                player_id = int(input("Enter player ID to update: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID NUMBER.")

        player = self.get_player_by_id(player_id)
        if player:
            print("Update player Information:")
            player.name = input(f"Name ({player.name}): ") or player.name
            while True:
                try:
                    age = input(f"Age ({player.age}): ") or player.age
                    age = int(age)
                    if age <= 0:
                        raise ValueError("Age must be a positive integer.")
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}. Please enter a valid age.")
            player.country = input(f"Country ({player.country}): ") or player.country
            while True:
                gender = input(f"Gender ({player.gender}): ").strip().lower()
                if gender in ['m', 'f', ''] :
                    player.gender = gender.capitalize() if gender else player.gender
                    break
                else:
                    print("Invalid input. Please enter 'M' for Male or 'F' for Female.")
            print("\nPLAYER INFORMATION UPDATED SUCCESSFULLY!")
        else:
            print(f"No player found with ID Number: {player_id}")

    # Method to delete a player
    def delete_player(self):
        while True:
            try:
                player_id = int(input("Enter player ID Number to delete: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid player ID.")

        player = self.get_player_by_id(player_id)
        if player:
            self.players.remove(player)  # Remove the player from the list
            print(f"Player with ID NUMBER {player_id} deleted successfully!")
        else:
            print(f"No player found with ID Number: {player_id}")

# Main entry point to run the system
if __name__ == "__main__":
    system = BadmintonPlayerManagementSystem()  # Initialize the system
    system.run()  # Start the system