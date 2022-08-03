# Author: Jigyasa Chaudhary
# V00899304

import sys
import numpy as np
from numpy import linalg as LA
from numpy.linalg import inv
from fractions import Fraction
from pprint import pprint

from sympy import false, true

def parseInput():
    input = []
    for line in sys.stdin:
        new_list = [Fraction(elem) for elem in line.split()]
        input.append(new_list)
    n = len(input[0])
    
    # input[] is a list currently
    # pprint(input)

    c = [Fraction(elem) for elem in input[0]]
    input.pop(0)

    m = len(input)

    b = np.zeros((m)) + Fraction()
    count = 0
    for elem in input:
        b[count] = elem[-1]
        count = count + 1

    A = np.zeros((m,n)) + Fraction()
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
    I = np.identity(m)
    # pprint(I)
    A = A.reshape(m,n)
    A = np.hstack((A, I))

    N = [i for i in range(n)]
    B = [n+i for i in range(m)]
    
    # print("m = ", m)
    # print("n = ", n)
    # print("b = ", b)
    # print("A = ")
    # pprint(A)
    print("c = ", c)
    print("N = ", N)
    print("B = ", B)
    # print("AB = ", AB)
    # print("AN = ", AN)
    
    simplex(A, b, c, B, N, x, m, n)

    pass

def checkPrimalFeasible(b):
    for i in b:
        if i < 0:
            return false
    return true

def checkDualFeasible(c):
    for i in c:
        if c > 0:
            return false
    return true

def PrimalSimplex(A, b, c, B, N, x, m, n):

    AB = getA(A, B, m)
    AB = np.asmatrix(AB)
    print(inv(AB))
    pprint(b)
    
    xb = np.dot(inv(AB), b)

    # if not verifyBasis(xb):
    #     raise Exception("Initial basis not feasible")   
    
    # cb = get_cb(c, B)
    # cn = get_cn(c, N)

    # while(true):
    #     # compute objective value
    #     zn = computeObjectiveCoeff(A, B, N, cb, cn, m)
        
    #     if(checkOptimal(zn)):
    #         Z = computeObjective(cb, A, B, b, m)
    #         return Z
        
    #     ev = -1
    #     lv = -1
    #     # choose an entering variable: Blands rule
    #     for i, val in enumerate(zn):
    #         if val < 0:
    #             ev = i
    #     # choose a leaving variable
    #     del_xb = np.dot(inv(AB), getcol(A, ev))    
    
    # # choose leaving variable
    # for i in zb:
    #     pass
        
    pass

def DualSimplex(A, b, c, B, N, x, m, n):
    pass

def getA(A, B, m):
    # pprint(B)
    # pprint(A)
    M = np.empty((len(B), m)) + Fraction()
    
    if len(B) > 1:
        for col in range(len(B)):
            for i, val in enumerate(A[:, B[col]]):
                M[col, i] = val
            
    # pprint(M)
    return M

def getcol(A, ev):
    M = np.empty(len(A)) + Fraction()
    
    for col in A:
        for i, val in enumerate(A[:, B[col]]):
            M[col, i] = val

            
def getX(cb, B, N):
    pass

def get_cb(c, B):
    pass

def get_cn(c, N):
    pass

def verifyBasis(xb):
    for val in xb:
        if val < 0:
            return false
    return true

def computeObjective(cb, A, B, b, m):
    AB = getA(A, B, m)
    Z = np.dot(cb.transpose(), np.dot(inv(AB), b))
    return Z

def computeObjectiveCoeff(A, B, N, cb, cn, m):
    AB = getA(A, B, m)
    AN = getA(A, N, m)
    A = np.dot(inv(AB), AN)
    C = np.dot(A.transpose(), cb)
    RC = C - cn
    return RC

def checkOptimal(Z):
    for i in Z:
        if i < 0:
            return false
    return true

def simplex(A, b, c, B, N, x, m, n):
    if checkPrimalFeasible(b):
        # primal simplex
        return PrimalSimplex(A, b, c, B, N, x, m, n)
    elif checkDualFeasible(c):
        return DualSimplex(A, b, c, B, N, x, m, n)
    else:
        B_a, N_a = DualSimplex(A, b, 0, B, N, x, m, n)
        return PrimalSimplex(A, b, c, B_a, N_a, x, m, n)

def main():
    parseInput()
    
# Main body
if __name__ == '__main__':
    main()