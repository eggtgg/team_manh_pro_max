import random
import numpy as np
from sympy import *



def matran(m,n) :
    rd = np.random.randint(0,10,(m,n))
    #print('ma tran = ',rd)
    return rd



def rank_matran(rd) :
    hang_ma_tran = np.linalg.matrix_rank(rd)
    #print('rank = ',hang_ma_tran)
    return hang_ma_tran




def bacthang(rd) :
    M = Matrix(rd)
    M_rref = M.rref()
    #print("hang ma tran = : {} ".format(M_rref))
    return M_rref[0]


m = int(input('nhap so hang = '))
n = int(input('nhap so cot = '))
a = matran(m,n)
print('ma tran ',a)
b = rank_matran(a)
print('rank = ',b)
r = bacthang(a)
print(r)