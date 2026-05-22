import random

def get_player_choice():
    """Get the player's choice and validate it."""
    valid_choices = ["rock", "paper", "scissors", "quit"]
    
    while True:
        player_input = input("\nEnter your choice (rock, paper, scissors, or quit): ").strip().lower()
        
        if player_input in valid_choices:
            return player_input
        else:
            print(f"❌ Invalid option: '{player_input}'. Please choose rock, paper, scissors, or quit.")

def get_computer_choice():
    """Have the computer randomly choose rock, paper, or scissors."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of a round.
    Returns: "win", "lose", or "tie"
    """
    if player_choice == computer_choice:
        return "tie"
    
    # Define winning conditions
    winning_conditions = {
        "rock": "scissors",      # rock beats scissors
        "paper": "rock",         # paper beats rock
        "scissors": "paper"      # scissors beats paper
    }
    
    if winning_conditions[player_choice] == computer_choice:
        return "win"
    else:
        return "lose"

def display_round_result(player_choice, computer_choice, result):
    """Display the result of a round."""
    print(f"\n{'='*50}")
    print(f"Player chose: {player_choice.upper()}")
    print(f"Computer chose: {computer_choice.upper()}")
    
    if result == "win":
        print("🎉 You WON this round!")
    elif result == "lose":
        print("😔 You LOST this round!")
    else:
        print("🤝 It's a TIE!")
    print(f"{'='*50}")

def play_again():
    """Ask the player if they want to play another round."""
    while True:
        choice = input("\nDo you want to play again? (yes/no/quit): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n", "quit", "q"]:
            return False
        else:
            print("❌ Invalid option. Please enter 'yes', 'no', or 'quit'.")

def display_final_score(player_wins, total_games):
    """Display the final score and game statistics."""
    if total_games == 0:
        print("\nNo games were played.")
        return
    
    player_loss_rate = total_games - player_wins
    win_percentage = (player_wins / total_games) * 100
    
    print(f"\n{'='*50}")
    print(f"🎮 GAME OVER - Final Statistics:")
    print(f"{'='*50}")
    print(f"Total games played: {total_games}")
    print(f"Games won: {player_wins}")
    print(f"Games lost: {player_loss_rate}")
    print(f"Win percentage: {win_percentage:.1f}%")
    print(f"{'='*50}\n")

def main():
    """Main game loop."""
    print("\n" + "="*50)
    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("="*50)
    print("Rules:")
    print("  • Rock beats Scissors")
    print("  • Scissors beats Paper")
    print("  • Paper beats Rock")
    print("\nYou can type 'quit' at any time to exit the game.")
    print("="*50)
    
    player_wins = 0
    total_games = 0
    
    while True:
        # Get choices
        player_choice = get_player_choice()
        
        # Check if player wants to quit
        if player_choice == "quit":
            print("\n👋 Quitting the game...")
            break
        
        computer_choice = get_computer_choice()
        
        # Determine winner
        result = determine_winner(player_choice, computer_choice)
        
        # Display result
        display_round_result(player_choice, computer_choice, result)
        
        # Update score
        if result == "win":
            player_wins += 1
        total_games += 1
        
        print(f"\n📊 Current Score: {player_wins}/{total_games} wins")
        
        # Ask to play again
        if not play_again():
            break
    
    # Display final score
    display_final_score(player_wins, total_games)

if __name__ == "__main__":
    main()
