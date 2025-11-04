CS351-Sudoku-Solver: Constraint Satisfaction via Backtracking

This repository contains a generalized Sudoku solver designed to handle N x N grids (where N is a perfect square, e.g., 9x9, 16x16, 25x25) using a backtracking algorithm.

Project Description (5 Lines)

This project implements a core backtracking algorithm to solve generalized Sudoku puzzles.

The solver can handle board sizes defined by the input file's first line (e.g., N=16).

It performs full constraint checking for rows, columns, and subgrids (blocks).

Input is read from a .txt file, and the solution is automatically written to a new output file (<input>Solution.txt).

The solver records and outputs the total time taken to observe performance, especially on large 16x16 problems.

Files

File Name

Description (5 Lines)

sudoku_solver.py

This is the main solver containing the backtracking recursion.



It handles file reading to load the puzzle dimensions and data.



It implements the core is_valid function for constraint checking.



It times the solving process and prints the outcome to the console.



It writes the final solution grid and performance metrics to an output file.

test_case_generator.py

This utility file quickly creates large, empty N x N puzzle files (e.g., 25x25).



It is used primarily for performance testing and benchmarking the solver's limits.



The size and filename are easily configured within the file.



It writes the grid size and then N rows of '0's to the output file.
