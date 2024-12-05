import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [["." for _ in range(7)] for _ in range(7)]

def display_board(board):
    print("  1 2 3 4 5 6 7")
    print("  -------------")
    for i in range(7):
        print(chr(65 + i), " ".join(board[i]))

def is_valid_position(board, positions):
    for x, y in positions:
        if not (0 <= x < 7 and 0 <= y < 7) or board[x][y] != ".":
            return False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < 7 and 0 <= y + j < 7 and board[x + i][y + j] == "S":
                    return False
    return True

def place_ship(board, size):
    while True:
        direction = random.choice(["H", "V"])
        if direction == "H":
            start_x = random.randint(0, 6)
            start_y = random.randint(0, 6 - size)
            positions = [(start_x, start_y + k) for k in range(size)]
        else:
            start_x = random.randint(0, 6 - size)
            start_y = random.randint(0, 6)
            positions = [(start_x + k, start_y) for k in range(size)]
        if is_valid_position(board, positions):
            for x, y in positions:
                board[x][y] = "S"
            return positions

def setup_ships(board):
    ship_sizes = [3, 2, 2, 1, 1, 1, 1]
    ships = [place_ship(board, size) for size in ship_sizes]
    return ships

def all_cells_hit(ship, board):
    return all(board[x][y] == "H" for x, y in ship)

def main():
    player_history = []

    while True:
        print("Welcome to Seabattle!")
        player_name = input("Enter your name: ")

        player_board = create_board()
        hidden_board = create_board()
        ships = setup_ships(hidden_board)

        total_shots = 0
        hits = 0
        misses = 0
        sunk_ships = 0
        total_ship_cells = 11
        ship_hits = {tuple(ship): 0 for ship in ships}

        while total_shots < 30 and hits < total_ship_cells:
            clear_screen()
            display_board(player_board)
            print(f"Shots: {total_shots}, Hits: {hits}, Misses: {misses}")
            print(f"Sunk Ships: {sunk_ships}, Remaining Ships: {7 - sunk_ships}")

            move = input("Enter your shot (e.g., B5): ").upper()
            if len(move) < 2 or not ("A" <= move[0] <= "G") or not ("1" <= move[1] <= "7"):
                print("Invalid input. Try again.")
                continue

            row = ord(move[0]) - ord("A")
            col = int(move[1]) - 1

            if player_board[row][col] != ".":
                print("You already shot here! Try again.")
                continue

            total_shots += 1

            if hidden_board[row][col] == "S":
                for ship in ships:
                    if (row, col) in ship:
                        player_board[row][col] = "H"
                        hidden_board[row][col] = "H"
                        print("Hit!")
                        hits += 1
                        ship_hits[tuple(ship)] += 1

                        if ship_hits[tuple(ship)] == len(ship):
                            for x, y in ship:
                                player_board[x][y] = "S"
                            print(f"You sunk a {len(ship)}-cell ship!")
                            sunk_ships += 1
                        break
            else:
                player_board[row][col] = "M"
                print("Miss!")
                misses += 1

        player_history.append({
            "name": player_name,
            "shots": total_shots,
            "hits": hits,
            "misses": misses,
            "sunk_ships": sunk_ships
        })

        if hits == total_ship_cells:
            print("Congratulations! You sank all the ships!")
        else:
            print("Game over! You ran out of shots.")

        if input("Play again? (yes/no): ").lower() != "yes":
            break

    print("Thanks for playing Seabattle!")
    print("\nPlayer History:")
    for record in player_history:
        print(f"Player: {record['name']}, Shots: {record['shots']}, Hits: {record['hits']}, Misses: {record['misses']}, Sunk Ships: {record['sunk_ships']}")

main()
