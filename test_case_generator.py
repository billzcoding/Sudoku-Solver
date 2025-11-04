import os

def create_empty_sudoku_file(grid_dimension, target_filename):
    """
    Generates a generic Sudoku puzzle file (N x N) with all cells set to 0 (empty).
    This is useful for observing the time complexity on large problem sizes.
    """
    try:
        # Check if the dimension is a perfect square (required for Sudoku)
        if math.isqrt(grid_dimension) ** 2 != grid_dimension:
            print(f"Warning: Sudoku dimension {grid_dimension} is not a perfect square. Subgrid checks might fail.")

        with open(target_filename, 'w') as f:
            # 1. Write the grid size (N) on the first line
            f.write(str(grid_dimension) + '\n')
            
            # 2. Define a row of '0's separated by spaces
            empty_row = ' '.join(['0'] * grid_dimension)
            
            # 3. Write N rows of empty cells
            for _ in range(grid_dimension):
                f.write(empty_row + '\n')
        
        print(f"Successfully created test file: '{target_filename}' ({grid_dimension}x{grid_dimension} empty grid).")
        print("Use this file name in 'sudoku_solver.py' to run your solver.")

    except Exception as e:
        print(f"An error occurred: {e}")

# --- Configuration for Generating a Large Test Case ---
# You can change this to 9, 16, or 25 to generate a grid of that size
TARGET_DIMENSION = 9 
TARGET_FILENAME = 'sudoku_9_empty.txt'

# Execute the generator
if __name__ == "__main__":
    import math
    create_empty_sudoku_file(TARGET_DIMENSION, TARGET_FILENAME)
