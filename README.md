# LPSolver

This repository creates an LP solver which reads a text-based representation of a linear program from standard input and outputs the result of solving the LP.

This is an incomplete implementation with the initialization and skeleton of simplex method via Linear algebra working.

The implementation works with Matrices and uses sympy for convenience.

## Basic idea behind the algorithm

The following skeleton was followed while working:

1. Read input from standard input
2. Setup initial matrices including A, b, B, NB, X
3. Computing the Basic and Non-Basic Matrix
4. Construction of vector u
5. Checking primal and dual feasibility
6. Setting up the simplex method and navigating to primal, dual or initially infeasible -> modified dual solutions
7. setup of the simplex methods
8. Computation of the objective value
9. Skeleton of primal and dual optimal values

Functionality to be implemented:
Run simplex on primal or dual based on initial feasibility

This skeleton was derived from Lecture-14

## To run code on file "fileName.txt"

python3 lp.py < fileName.txt
