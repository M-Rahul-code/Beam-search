import random

def initialize_board(N):
    return [random.randint(0, N - 1) for _ in range(N)]

def count_conflicts(board):
    conflicts = 0
    N = len(board)
    for i in range(N):
        for j in range(i + 1, N):
            if (
                board[i] == board[j] or
                abs(i - j) == abs(board[i] - board[j])
            ):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    N = len(board)
    neighbors = []
    
    for col in range(N):
        for row in range(N):
            if board[col] != row:
                neighbor_board = board.copy()
                neighbor_board[col] = row
                neighbors.append(neighbor_board)
    
    return neighbors

def beam_search(N, beam_width=5, max_iter=1000):
    current_boards = [initialize_board(N) for _ in range(beam_width)]
    
    for _ in range(max_iter):
        for i in range(beam_width):
            if count_conflicts(current_boards[i]) == 0:
                return current_boards[i] 
        
        neighbors = []
        for board in current_boards:
            neighbors.extend(generate_neighbors(board))
        
        neighbors.sort(key=lambda board: count_conflicts(board))
        current_boards = neighbors[:beam_width]
    
    return None 

def print_board(board):
    N = len(board)
    for row in range(N):
        line = ""
        for col in range(N):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    N = 8  
    solution = beam_search(N)
    
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found within the maximum iterations.")
import random

def initialize_board(N):
    return [random.randint(0, N - 1) for _ in range(N)]

def count_conflicts(board):
    conflicts = 0
    N = len(board)
    for i in range(N):
        for j in range(i + 1, N):
            if (
                board[i] == board[j] or
                abs(i - j) == abs(board[i] - board[j])
            ):
                conflicts += 1
    return conflicts

def generate_neighbors(board):
    N = len(board)
    neighbors = []
    
    for col in range(N):
        for row in range(N):
            if board[col] != row:
                neighbor_board = board.copy()
                neighbor_board[col] = row
                neighbors.append(neighbor_board)
    
    return neighbors

def beam_search(N, beam_width=5, max_iter=1000):
    current_boards = [initialize_board(N) for _ in range(beam_width)]
    
    for _ in range(max_iter):
        for i in range(beam_width):
            if count_conflicts(current_boards[i]) == 0:
                return current_boards[i] 
        
        neighbors = []
        for board in current_boards:
            neighbors.extend(generate_neighbors(board))
        
        neighbors.sort(key=lambda board: count_conflicts(board))
        current_boards = neighbors[:beam_width]
    
    return None 

def print_board(board):
    N = len(board)
    for row in range(N):
        line = ""
        for col in range(N):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    N = 8  
    solution = beam_search(N)
    
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found within the maximum iterations.")