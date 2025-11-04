import time
import sys
import os
import math

# --- File Handling and I/O ---

def load_puzzle_from_file(input_filename):
    """
    Reads the Sudoku grid from the specified input file.
    
    The first line must contain the grid size (N).
    Subsequent lines contain the N x N puzzle values, separated by spaces.
    """
    try:
        with open(input_filename, 'r') as f:
            lines = f.readlines()
            # The first line is the grid size
            grid_size = int(lines[0].strip())
            
            grid = []
            # Read the puzzle lines
            for line in lines[1:]:
                # Convert the space-separated numbers into integers
                row = list(map(int, line.strip().split()))
                if row: # Ensure non-empty lines are processed
                    grid.append(row)
            
            # Basic validation check
            if len(grid) != grid_size or any(len(row) != grid_size for row in grid):
                raise ValueError("Grid dimensions do not match the declared size.")
                
            return grid, grid_size

    except FileNotFoundError:
        print(f"Error: Input file '{input_filename}' not found.")
        return None, None
    except ValueError as e:
        print(f"Error reading file content: {e}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return None, None

def save_solution_to_file(input_filename, solution_grid, time_taken_sec):
    """
    Writes the solved grid and performance metrics to a new output file.
    
    The output filename is derived from the input filename by appending 'Solution'.
    """
    # Create the required output filename
    # Example: 'sudoku_16.txt' -> 'sudoku_16Solution.txt'
    base, ext = os.path.splitext(input_filename)
    output_filename = base + 'Solution' + ext
    
    try:
        # Calculate space complexity (approximate bytes used by the grid object)
        space_complexity_bytes = sys.getsizeof(solution_grid) + sum(sys.getsizeof(row) for row in solution_grid)

        with open(output_filename, 'w') as f:
            # Write the solved grid, row by row
            for row in solution_grid:
                f.write(' '.join(map(str, row)) + '\n')
            
            # Write performance data as required
            f.write(f'\nTime complexity: {time_taken_sec:.6f} seconds\n')
            f.write(f'Space complexity: {space_complexity_bytes} bytes\n')
            
        print(f"✅ Solution saved successfully to: '{output_filename}'")
        print(f"⏱️ Solve Time: {time_taken_sec:.4f} seconds")

    except Exception as e:
        print(f"Error writing solution file: {e}")

def display_grid(grid):
    """Prints the Sudoku grid to the console in a readable format."""
    N = len(grid)
    subgrid_size = int(math.sqrt(N))
    
    print("\n" + "═" * (N * 2 + subgrid_size * 2 + 1))
    
    for r in range(N):
        row_str = "║"
        for c in range(N):
            val = grid[r][c]
            row_str += f" {val if val != 0 else '.'}"
            
            # Add vertical separators for subgrids
            if (c + 1) % subgrid_size == 0 and c != N - 1:
                row_str += " ║"
        row_str += " ║"
        print(row_str)
        
        # Add horizontal separators for subgrids
        if (r + 1) % subgrid_size == 0 and r != N - 1:
            separator = "═" * (N * 2 + subgrid_size * 2 + 1)
            print(separator)
            
    print("═" * (N * 2 + subgrid_size * 2 + 1) + "\n")


# --- Backtracking Logic (Constraint Satisfaction) ---

def check_validity(grid, row, col, candidate_num, grid_size):
    """
    Checks if placing 'candidate_num' at grid[row][col] violates Sudoku rules.
    Rules: No duplicate in row, column, or subgrid.
    """
    subgrid_size = int(math.sqrt(grid_size))
    
    # 1. Check Row Constraint
    # Check if the number already exists in the current row
    if candidate_num in grid[row]:
        return False
        
    # 2. Check Column Constraint
    # Check if the number already exists in the current column
    for r in range(grid_size):
        if grid[r][col] == candidate_num:
            return False
            
    # 3. Check Subgrid Constraint
    # Determine the top-left corner of the subgrid
    subgrid_row_start = row // subgrid_size * subgrid_size
    subgrid_col_start = col // subgrid_size * subgrid_size
    
    # Iterate through the subgrid cells
    for r in range(subgrid_row_start, subgrid_row_start + subgrid_size):
        for c in range(subgrid_col_start, subgrid_col_start + subgrid_size):
            if grid[r][c] == candidate_num:
                return False
                
    return True

def find_next_empty_cell(grid, grid_size):
    """Searches for the next empty cell (value 0) to fill."""
    for r in range(grid_size):
        for c in range(grid_size):
            if grid[r][c] == 0:
                return r, c
    return -1, -1 # Indicates the board is full

def solve_sudoku_puzzle(grid, grid_size):
    """
    The main backtracking function using recursion.
    It attempts to fill the grid, returning True if solved, False if unsolvable.
    """
    
    row, col = find_next_empty_cell(grid, grid_size)
    
    # Base Case: If no empty cells are found, the puzzle is solved
    if row == -1:
        return True

    # Recursive Step: Try numbers 1 to N in the empty cell
    for num in range(1, grid_size + 1):
        if check_validity(grid, row, col, num, grid_size):
            
            # 1. Place the number (Assignment/Forward Check)
            grid[row][col] = num
            
            # 2. Recurse: Try to solve the rest of the puzzle
            if solve_sudoku_puzzle(grid, grid_size):
                return True
                
            # 3. Backtrack: If the current path failed, reset the cell to 0
            # This is the core of the backtracking algorithm
            grid[row][col] = 0
            
    # Exhausted all numbers and no solution found from this state
    return False

# --- Main Execution ---

def main_solver():
    """Reads input, solves the puzzle, and reports the outcome."""
    
    # 🌟 YOU MUST CHANGE THIS LINE! 🌟
    # Set the input file name to your empty 16x16 test case.
    input_file_name = 'sudoku_16_empty.txt'
    
    grid, grid_size = load_puzzle_from_file(input_file_name)
    
    if grid is None:
        return # Exit if file loading failed

    print(f"Loaded {grid_size}x{grid_size} Sudoku puzzle:")
    display_grid(grid)
    
    start_time = time.time()
    
    if solve_sudoku_puzzle(grid, grid_size):
        end_time = time.time()
        time_taken = end_time - start_time
        
        print(f"🎉 **SOLUTION FOUND** for the {grid_size}x{grid_size} grid!")
        display_grid(grid)
        
        save_solution_to_file(input_file_name, grid, time_taken)
        
        # Specific observation requirement for large grids
        if grid_size > 9:
             print(f"\n🔍 Observation: The time taken for the {grid_size}x{grid_size} problem ({time_taken:.4f}s) is a key metric for analyzing the performance scaling of the backtracking algorithm. Empty grids take the longest!")

    else:
        end_time = time.time()
        time_taken = end_time - start_time
        
        print(f"❌ **NO SOLUTION EXISTS** for the {grid_size}x{grid_size} grid.")
        print(f"⏱️ Total Execution Time: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main_solver()
