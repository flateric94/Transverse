import numpy as np
from math import *
import matrix_calpha_final as mc
import distance_min as dist

def compter_nb_residus(fichier_pdb2,fichier_output,n):
    matrix_distance,matrix_square_distance=mc.distance(fichier_pdb2,fichier_output,"A","A")
    #print(matrix_distance)
    matrix1=dist.min_distance_l_r(matrix_distance)
    matrix2=dist.min_distance_r_l(matrix_distance)
    counter=0
    if(matrix1==matrix2[::-1] ): #si la lecture des 2 matrices renvoie les memes paires
        for i in range(0,len(matrix1)):
        	#print(matrix_distance[matrix1[i][3]][matrix1[i][4]])
        	if matrix_distance[matrix1[i][3]][matrix1[i][4]] <= n:
        		counter+=1
    #print(counter)
    return counter,len(matrix_distance)

def calcul_GDT_TS2(fichier_pdb2,fichier_output):
    nb_res1, size1 = compter_nb_residus(fichier_pdb2,fichier_output,1)
    GDT_P1 =  (nb_res1/size1)*100
    nb_res2,size2 = compter_nb_residus(fichier_pdb2,fichier_output,2)
    GDT_P2 =  (nb_res2/size2)*100
    nb_res4,size4 = compter_nb_residus(fichier_pdb2,fichier_output,4)
    GDT_P4 =  (nb_res4/size4)*100
    nb_res8, size8 = compter_nb_residus(fichier_pdb2,fichier_output,8)
    GDT_P8 =  (nb_res8/size8)*100
    res = (GDT_P1 + GDT_P2 + GDT_P4 + GDT_P8)/4
    return res

#def main():
    #pdb1 = "3fts.pdb"
    #pdb2 = "3fh7.pdb"
    #fichier_output = "TM.sup_all_atm-2.pdb"

    #pdb1 = "1e1v.pdb"
    #pdb2 = "fichiers_pdb/1b38.pdb"
    #fichier_output = "TM.sup_all_atm.pdb"
    #pdb6="fichiers_pdb/1aq1.pdb"
    #pdb7="ResultsSuperposition/1aq1 vs 1h08/Tm_align/1aq1_1h08_t.pdb"
    #pdb8="fichiers_pdb/1h08.pdb"
    #pdb9="ResultsSuperposition/1aq1 vs 1h08/Tm_align/1aq1_1h08_t1.pdb"

    #compter_nb_residus(pdb2,fichier_output,1)
    #matrix_distance,matrix_square_distance=mc.distance(pdb2,fichier_output)
    #compter_nb_residus(matrix_distance,1)
   # print(dist.min_distance_l_r(matrix_distance))
    #print(dist.min_distance_r_l(matrix_distance))
    #print(matrix_distance)
    #GDT_P1=calcul_GDT_P1(pdb2,fichier_output)
    #GDT_P2=calcul_GDT_P2(pdb2,fichier_output)
    #GDT_P4=calcul_GDT_P4(pdb2,fichier_output)
    #GDT_P8=calcul_GDT_P8(pdb2,fichier_output)
    #print(calcul_GDT_TS(GDT_P1,GDT_P2,GDT_P4,GDT_P8))

    #GDT_P1=calcul_GDT_P1(pdb6,pdb9)
    #GDT_P2=calcul_GDT_P2(pdb6,pdb9)
    #GDT_P4=calcul_GDT_P4(pdb6,pdb9)
    #GDT_P8=calcul_GDT_P8(pdb6,pdb9)
    #print(calcul_GDT_TS(GDT_P1,GDT_P2,GDT_P4,GDT_P8))
    
#main()
