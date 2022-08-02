# Author: Jigyasa Chaudhary
# V00899304

import sys
import sympy as sp
from fractions import Fraction
import sympy as sy
from sys import stdin


def inputParse():

    # creating C list and converting to an array    
    input = []
    for line in sys.stdin:
        new_list = [Fraction(elem) for elem in line.split()]
        input.append(new_list)
    n = len(input[0])
    C = sp.Matrix([Fraction(elem) for elem in input[0]])
    input.pop(0)

    m = len(input)

    b = sp.zeros(m, 1)
    count = 0
    for elem in input:
        b[count] = elem[-1]
        count = count + 1

    A = sp.zeros(m,n)
    
    # add appropriate values to matrix A
    count = 0
    while count < n:        
        for row in input:
            x = row[:-1]
            i = 0
            for val in x:
                A[count, i] = val
                i = i + 1
            count += 1

    # length of basic and non-basic matrices
    B_len = m
    NB_len = n

    # basic and non-basic indices
    B, NB = [], []
    for count in range(NB_len):
        NB.append(count)
    for count in range(NB_len, NB_len+B_len):
        B.append(count)

    # add identity matrix for the slack variables to Matrix A
    I = sp.eye(B_len)
    A = A.row_join(I)

    # Basic and non-basic matrices
    A_B = computeBasic(A, B)
    A_NB = computeBasic(A, NB)


def computeBasic(A, B):
    M = A[:, B[0]]
    if len(B) > 1:
        for val in range(1, len(B)):
            M = M.row_join(A[:, B[val]])
    return M

def u_k(zi, B):
    u_k = sp.zeros(len(B), 1)
    for k in range(len(B)):
        if B[k] == zi:
            u_k[k] = Fraction(1)
        else:
            u_k[k] = Fraction(0)

def computeX(x_B, B, NB):
    pass

def compute_zn(A, A_B_inv, B, C, NB):
    pass

def checkprimalfeasible(b):
    for x in b:
        if not x > 0:
            return 0
    return 1

def checkdualfeasible(C):
    for x in C:
        if not x <= 0:
            return 0
    return 1

def setup_simplex(A, b, B, C, NB):
    result = ""
    if checkprimalfeasible(b):
        result = primal_simplex(A, b, B, C, NB)
    elif checkdualfeasible(C):
        result = dual_simplex(A, b, B, C, NB)
    else:
        dual_simplex(A, b, B, 0, NB)

def primal_simplex(A, b, B, C, NB):

    A_B = computeBasic(A, B)
    A_NB = computeBasic(A, NB)

    if not checkprimalfeasible(A_B, b):
        print("primal infeasible")

    while True:
        A_B_inv = A_B.inv()
        x_B = A_B_inv * b

        z_N = compute_zn(A, A_B_inv, B, C, NB)
        if primalOptimal(z_N):
            result = compute_objective(C, A_B_inv, B, b)
            return ("optimal", result, x_B)

        pivot(A, A_B_inv, B, NB, x_B, z_N)

    pass

def primalOptimal(z_val):
    # C_B.transpose() * A_B_inc * b
    pass

def dualOptimal(z_val):
     # C_B.transpose() * A_B_inc * b
    pass

def dual_simplex(A, b, B, C, NB):
    A_B = computeBasic(A, B)
    A_NB = computeBasic(A, NB)
    if not C == 0:
        if not checkdualfeasible(A, A_B, b, B, C, NB):
            return "Infeasible"

        while True:
            A_B_inv = A_B.inv()
            x_B = A_B_inv * b

            z_N = compute_zn(A, A_B_inv, B, C, NB)
            if dualOptimal(x_B):
                result = compute_objective(C, A_B_inv, B, b)
                return ("optimal", result, x_B)

            pivot(A, A_B_inv, B, NB, x_B, z_N)
    else:
        B_1 = B
        NB_1 = NB
        primal_simplex(A, b, B_1, C, NB_1)

def pivot(A, A_B_inv, B, NB, x_B, z_N):
    i, i_index, j, j_index, del_x = 0

    B[i_index] = j
    NB[j_index] = i

    B.sort()
    NB.sort()


def compute_objective(c, AB_inv, B, b):
    c_B = sp.Matrix(c[val] for val in B)
    result = c_B.transpose() * AB_inv * B
    return result


def print_result(result):
    pass

# def checkprimalfeasible(A_B, b):
#     A_B_inv = A_B.inv()
#     x_B = A_B_inv * b
#     if x_B >= 0:
#         return 1
#     else:
#         return 0

# def checkdualfeasible(A, A_B, b, B, C, NB):
#     A_B_inv = A_B.inv()
#     z_N = compute_zn(A, A_B_inv, B, C, NB)
#     if z_N >= 0:
#         return 1
#     else:
#         return 0

def main():

    inputParse()
    


# Main body
if __name__ == '__main__':
    main()
