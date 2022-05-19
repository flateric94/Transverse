# -*- coding: utf-8 -*-
"""
Created on Tue May  3 20:46:34 2022

@author: tanvi
"""


import math


def Read_rmsd(fichier_a_ouvrir,pos_ligne_rmsd,pos_ligne_nbr,pos_rmsd,pos_N): #pos_ligne_rmsd=ligne ou se situe le rmsd,pos_ligne_nbr=ligne ou se situe le nbr de résidus superposés,pos_rmsd: position du rmsd dans la ligne,pos_N: position de N dans la ligne
    #Cette fonction permet d'extraire le rmsd et le nombre de résidus N comparés du fichier txt output
    with open (fichier_a_ouvrir) as file: #ouvre le fichier
        data_rmsd = file.readlines()[pos_ligne_rmsd] #récuperer la ligne ou se trouve le rmsd et le nombre N
    with open (fichier_a_ouvrir) as file:    
        data_nbr = file.readlines()[pos_ligne_nbr]
    tab1=data_rmsd.replace(","," ").split() # #création d'un tableau avec les éléments de la ligne (enlève les ",")
    tab2=data_nbr.replace(","," ").split()
    rmsd=tab1[pos_rmsd] #recupere le rmsd qui est en nieme positiion dans la ligne
    nbr_residu=tab2[pos_N] ##recupere N qui est en pieme positiion dans la ligne
    return rmsd, nbr_residu #retourne rmsd pratique et N


def rmsd(matrix_distance,matrix_square_distance,matrix_round,matrix):
    rmsd=0
    for i in range(0,len(matrix)):
        rmsd+=(matrix_square_distance[matrix[i][3]][matrix[i][4]])
    return math.sqrt(rmsd/len(matrix))

def comparison_RMSD(rmsd_recal,fichier_a_ouvrir, pos_ligne_rmsd,pos_ligne_nbr, pos_rmsd, pos_N): 
    #,pos_ligne_rmsd=ligne ou se situe le rmsd,
    #pos_ligne_nbr=ligne ou se situe le nbr de résidus superposés,
    #pos_rmsd: position du rmsd dans la ligne,pos_N: position de N dans la ligne
    #Cette fonction sera la seule appelée: elle rassemble toutes les autres fonctions
    rmsd_logiciel,Nbr_res_logiciel=Read_rmsd(fichier_a_ouvrir, pos_ligne_rmsd,pos_ligne_nbr, pos_rmsd, pos_N)
    Difference=abs(rmsd_recal-float(rmsd_logiciel))#difference entre le rmsd du logiciel et le notre= 0 si le même; 
    #<1 le logiciel donne un rmsd trop grand; >1 le logiciel donne un rmsd trop petit
    return Nbr_res_logiciel, rmsd_logiciel, Difference #renvoie le nombre de résidus utilisé par le logiciel pour calculer le rmsd, 
    #le rmsd calculé par le logiciel, le rmsd calculé par la fonction Calcul_RMSD et la différence entre ces 2 rmsd 
