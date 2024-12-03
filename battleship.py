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