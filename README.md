# LPSolver

This repository creates an LP solver which reads a text-based representation of a linear program from standard input and outputs the result of solving the LP.

This is an incomplete implementation with the initialization and partial primalSimplex of simplex method via Linear algebra working.

The implementation works with Matrices and uses sympy for convenience.

## Basic idea behind the algorithm

The following skeleton was followed while working:

1. Read input from standard input (DONE)
2. Setup initial matrices including A, b, B, NB, X(DONE)
3. Computing the Basic and Non-Basic Matrix(DONE)
4. Construction of vector u (DONE)
5. Checking primal and dual feasibility (DONE)
6. Setting up the simplex method and navigating to primal, dual or initially infeasible -> modified dual solutions (DONE)
7. setup of the primal simplex method (DONE)
8. pivot for primal simplex method (IN PROGRESS)
9. dual simplex method
10. Computation of the objective value(DONE)

Functionality to be implemented:
Run simplex on primal or dual based on initial feasibility

This skeleton was derived from Lecture-14

## To run code on file "fileName.txt"

python3 lp.py < fileName.txt
