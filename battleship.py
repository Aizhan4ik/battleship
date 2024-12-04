import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    board = []
    for i in range(7): 
        board.append(["." for _ in range(7)])
    return board

def display_board(board):
    print("  1 2 3 4 5 6 7")
    print("  -------------")
    for i in range(7):
        print(chr(65 + i), " ".join(board[i]))
        
def is_valid_position(board, positions):
    for x, y in positions:
        if not (0 <= x < 7 and 0 <= y < 7):  
            return False
        if board[x][y] != ".":  
            return False
    
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 7 and 0 <= ny < 7 and board[nx][ny] == "S":
                    return False
    return True

def place_ship(board, size):
    while True:
        direction = random.choice(["H", "V"])  
        if direction == "H":  
            x = random.randint(0, 6)
            y = random.randint(0, 6 - size)
            positions = [(x, y + i) for i in range(size)]  
        else:  
            x = random.randint(0, 6 - size)
            y = random.randint(0, 6)
            positions = [(x + i, y) for i in range(size)] 
        
        if is_valid_position(board, positions): 
            for px, py in positions:
                board[px][py] = "S"
            return positions
        
def setup_ships(board):
    ship_sizes = [3, 2, 2, 1, 1, 1, 1]  
    ship_positions = []  
    for size in ship_sizes:
        positions = place_ship(board, size) 
        ship_positions.append(positions) 
    return ship_positions

def get_input():
    move = input("Enter your shot (e.g., B5): ").upper() 
    if len(move) < 2:  
        return None
    row = ord(move[0]) - ord("A")  
    col = int(move[1]) - 1  
    if 0 <= row < 7 and 0 <= col < 7:  
        return row, col
    return None

def main():
    print("Welcome to Battleship!")
    player_name = input("Enter your name: ").strip()
    
    while True:
        player_board = create_board()  
        hidden_board = create_board()  
        ship_positions = setup_ships(hidden_board)  

        hits = 0  
        total_ships = 7  
        shots = 0 
        shot_cells = set()  

        while hits < total_ships and shots < 30:  
            clear_screen()
            display_board(player_board)  
            print(f"Shots taken: {shots}/30")  

            coords = get_input()  
            if not coords:
                print("Invalid input. Please enter a valid shot (e.g., B5).")
                continue

            x, y = coords
            if (x, y) in shot_cells:  
                print("You already shot here! Try again.")
                continue

            shot_cells.add((x, y))  
            shots += 1

            if hidden_board[x][y] == "S":  
                player_board[x][y] = "H" 
                hidden_board[x][y] = "H"  
                hits += 1
                print("Hit!")
            else:  
                player_board[x][y] = "M" 
                print("Miss!")
                
        for ship in ship_positions:
            if all(hidden_board[px][py] == "H" for px, py in ship):
             for px, py in ship:
                player_board[px][py] = "S"  
            print("You sunk a ship!")
            break
        
        if hits == total_ships:
            print(f"Congratulations, {player_name}! You sank all ships in {shots} shots!")
        else:
            print("Game over! You reached the maximum number of shots (30).")
            
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    print("Thanks for playing Battleship!")

main()