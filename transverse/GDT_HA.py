# -*- coding: utf-8 -*-

import matrix_calpha_final as mc


def count_nb_residus(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix,n):
    counter=0
    for i in range(0,len(matrix)):
        if matrix_distance[matrix[i][3]][matrix[i][4]] <= n:
        	counter+=1
    return counter,int(mc.size_pdb(pdb1,chaineA))

def calcul_GDT_P05(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    nb_res, size = count_nb_residus(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix,0.5)
    return (nb_res/size)*100

def calcul_GDT_P1(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    nb_res,size = count_nb_residus(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix,1)
    return (nb_res/size)*100

def calcul_GDT_P2(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    nb_res,size = count_nb_residus(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix,2)
    return (nb_res/size)*100

def calcul_GDT_P4(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    nb_res, size = count_nb_residus(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix,4)
    return (nb_res/size)*100

def calcul_GDT_HA(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    GDT_P05=calcul_GDT_P05(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix)
    GDT_P1=calcul_GDT_P1(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix)
    GDT_P2=calcul_GDT_P2(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix)
    GDT_P4=calcul_GDT_P4(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix)
    res = (GDT_P05 + GDT_P1 + GDT_P2 + GDT_P4)/4
    return res
