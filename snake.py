import random

# Snakes and ladders positions
snakes = {
    99: 54,
    70: 55,
    52: 42,
    25: 2,
    95: 72
}

ladders = {
    6: 25,
    11: 40,
    60: 85,
    46: 90,
    17: 69
}

player1 = 0
player2 = 0

def draw_board(p1, p2):
    print("\n" + "=" * 50)

    for row in range(10, 0, -1):

        start = (row - 1) * 10 + 1
        end = row * 10

        numbers = list(range(start, end + 1))

        if row % 2 == 0:
            numbers.reverse()

        line = ""

        for num in numbers:

            marker = ""

            if num == p1 and num == p2:
                marker = "B"
            elif num == p1:
                marker = "1"
            elif num == p2:
                marker = "2"

            cell = f"{num:02}"

            if marker:
                cell = marker + cell

            line += f"{cell:^6}"

        print(line)

    print("=" * 50)

def move_player(position, player_name):

    input(f"\n{player_name} press Enter to roll dice...")

    dice = random.randint(1, 6)

    print(f"{player_name} rolled {dice}")

    position += dice

    if position > 100:
        position -= dice
        print("Need exact number to reach 100!")
        return position

    if position in ladders:
        print(f"🪜 Ladder! {position} -> {ladders[position]}")
        position = ladders[position]

    elif position in snakes:
        print(f"🐍 Snake! {position} -> {snakes[position]}")
        position = snakes[position]

    print(f"{player_name} is now at {position}")

    return position

print("🎲 SNAKE AND LADDER 🎲")

while True:

    draw_board(player1, player2)

    player1 = move_player(player1, "Player 1")

    if player1 == 100:
        draw_board(player1, player2)
        print("\n🏆 PLAYER 1 WINS!")
        break

    player2 = move_player(player2, "Player 2")

    if player2 == 100:
        draw_board(player1, player2)
        print("\n🏆 PLAYER 2 WINS!")
        break