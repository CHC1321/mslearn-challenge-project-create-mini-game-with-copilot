# Rock, Paper, Scissors - Multiplayer Console Game

A fun and interactive console-based Rock, Paper, Scissors game where you can play against the computer. Built with Python, this game features input validation, real-time score tracking, and the ability to quit at any time.

## Overview

This is a multiplayer (player vs. computer) implementation of the classic Rock, Paper, Scissors game. The computer randomly selects its move, and the game determines the winner based on standard rules. Perfect for learning Python fundamentals and game development concepts.

## Features

✨ **Game Features:**
- **Multiplayer Mode**: Play against the computer opponent
- **Input Validation**: Invalid inputs are caught and handled gracefully (lowercase conversion)
- **Round Results**: Immediate feedback on win, loss, or tie for each round
- **Score Tracking**: Real-time score display after each round
- **Play Again Option**: Choose to play another round or exit after each game
- **Quit Anytime**: Exit the game at any point during gameplay
- **Game Statistics**: Final score summary with win percentage displayed at the end

## Game Rules

- **Rock beats Scissors** ✊
- **Scissors beats Paper** ✌️
- **Paper beats Rock** 📄
- If both player and computer choose the same option, it's a **TIE**

## How to Play

### Running the Game

```bash
python app.py
```

### Gameplay

1. **Start the game**: Run the script and you'll see the welcome screen with game rules
2. **Make your choice**: Enter one of the following options:
   - `rock` - Choose rock
   - `paper` - Choose paper
   - `scissors` - Choose scissors
   - `quit` - Exit the game immediately

3. **View the result**: The game displays:
   - Your choice
   - Computer's choice
   - Round result (Win 🎉 / Loss 😔 / Tie 🤝)
   - Current score

4. **Play again**: After each round, you'll be asked if you want to continue:
   - `yes` or `y` - Play another round
   - `no` or `n` - End the game
   - `quit` or `q` - Exit the game

5. **See your stats**: When you finish, the game displays:
   - Total games played
   - Games won
   - Games lost
   - Win percentage

## Example Gameplay

```
==================================================
🎮 Welcome to Rock, Paper, Scissors!
==================================================
Rules:
  • Rock beats Scissors
  • Scissors beats Paper
  • Paper beats Rock

You can type 'quit' at any time to exit the game.
==================================================

Enter your choice (rock, paper, scissors, or quit): rock

==================================================
Player chose: ROCK
Computer chose: SCISSORS
🎉 You WON this round!
==================================================

📊 Current Score: 1/1 wins

Do you want to play again? (yes/no/quit): yes

Enter your choice (rock, paper, scissors, or quit): quit

👋 Quitting the game...

==================================================
🎮 GAME OVER - Final Statistics:
==================================================
Total games played: 1
Games won: 1
Games lost: 0
Win percentage: 100.0%
==================================================
```

## Code Structure

The game is organized into modular functions:

- **`get_player_choice()`** - Prompts for and validates player input
- **`get_computer_choice()`** - Randomly selects computer's move
- **`determine_winner()`** - Compares choices and determines the winner
- **`display_round_result()`** - Shows the round outcome with visual feedback
- **`play_again()`** - Asks if the player wants to continue
- **`display_final_score()`** - Shows final game statistics
- **`main()`** - Manages the main game loop

## Input Handling

All user inputs are converted to lowercase automatically, so you can enter:
- `Rock`, `ROCK`, `rock` - All are treated as rock
- `Paper`, `PAPER`, `paper` - All are treated as paper
- `Scissors`, `SCISSORS`, `scissors` - All are treated as scissors
- `Quit`, `QUIT`, `quit` - All are treated as quit

Invalid inputs will display an error message and prompt you to try again.

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Getting Started

1. Clone or download this repository
2. Navigate to the project directory
3. Run `python app.py`
4. Follow the on-screen prompts

Enjoy the game! 🎮