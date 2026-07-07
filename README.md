# Snake and Ladder (Terminal Edition)

A terminal-based Snake and Ladder game for two players, written in Python. Roll the dice, climb ladders, avoid snakes, and race to reach square 100 first!

## Features

- 🎲 Classic two-player Snake and Ladder gameplay
- 🖥️ ASCII board rendered directly in the terminal, updated after every turn
- 🪜 Ladders that boost you forward
- 🐍 Snakes that send you backward
- 🔢 Player positions tracked and displayed live on the board
- Turn-based play with simple Enter-to-roll input

## Demo

```
🎲 SNAKE AND LADDER 🎲
==================================================
 100    99    98    97    96    95    94    93    92    91  
  81    82    83    84    85    86    87    88    89    90  
  80    79    78    77    76    75    74    73    72    71  
  61    62    63    64    65    66    67    68    69    70  
  60    59    58    57    56    55    54    53    52    51  
  41    42    43    44    45    46    47    48    49    50  
  40    39    38    37    36    35    34    33    32    31  
  21    22    23    24    25    26    27    28    29    30  
  20    19    18    17    16    15    14    13    12    11  
  01    02    03    04    05    06    07    08    09    10  
==================================================
Player 1 press Enter to roll dice...
Player 1 rolled 6
🪜 Ladder! 6 -> 25
Player 1 is now at 25
Player 2 press Enter to roll dice...
Player 2 rolled 3
Player 2 is now at 3
```

## Getting Started

### Prerequisites

- Python 3 installed on your system

### Installation

```bash
git clone https://github.com/anshikaaaasingh-afk/snake-and-ladder.git
cd snake-and-ladder
```

### Run

```bash
python3 snake.py
```

## Usage

1. Run the program to see the game board and welcome message.
2. Each turn, the current player presses **Enter** to roll the dice.
3. The player's token moves forward based on the dice roll.
4. Landing on a ladder's bottom square moves you up; landing on a snake's head sends you down.
5. The board reprints after each move, showing updated player positions.
6. Play continues, alternating turns between Player 1 and Player 2, until a player reaches square 100.

## How It Works

- **Board**: A 10x10 grid (squares 1–100) is rendered in a boustrophedon (zigzag) layout, matching a traditional Snake and Ladder board.
- **Dice Roll**: Each turn generates a random number (1–6) to determine how far the player moves.
- **Ladders**: Predefined squares that move a player forward to a higher square.
- **Snakes**: Predefined squares that move a player backward to a lower square.
- **Winning**: The first player to land exactly on (or pass, depending on the rules implemented) square 100 wins the game.

## Project Structure

```
snake-and-ladder/
├── snake.py    # Main source file
└── README.md   # Project documentation
```

## Possible Improvements

- Add support for more than 2 players
- Add a rule requiring an exact roll to win on square 100
- Add colored terminal output to distinguish players and highlight snakes/ladders
- Add a win screen and option to replay
- Allow customizable snake/ladder positions or board size

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Made by [Anshika](https://github.com/anshikaaaasingh-afk) as part of a growing Python/C/JavaScript portfolio.
