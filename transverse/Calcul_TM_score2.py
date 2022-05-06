import numpy as np
from math import *
import matrix_calpha_final as mc
import distance_min as dist

def Read_tm_score(fichier_a_ouvrir): #pos_ligne_rmsd=ligne ou se situe le rmsd,pos_ligne_nbr=ligne ou se situe le nbr de résidus superposés,pos_rmsd: position du rmsd dans la ligne,pos_N: position de N dans la ligne
    #Cette fonction permet d'extraire le tm-score, le nombre de résidus N comparés du fichier txt output, et le nombre de résidus du fichier pdb1
    with open (fichier_a_ouvrir) as file: #ouvre le fichier
    	data_tmscore = file.readlines()[17] #récuperer la ligne ou se trouve le tm-score par rapport au premier pdb
    	with open (fichier_a_ouvrir) as file:
    		data_Laligne = file.readlines()[13] #récuperer la ligne ou se trouve le nombre de résidus alignés
    		with open (fichier_a_ouvrir) as file:
    			data_Lcible = file.readlines()[16] #récuperer la ligne ou se trouve le nbre de résidus de la protéine cible
    			tab1=data_tmscore.replace(","," ").split()
    			tab2=data_Laligne.replace(","," ").split()
    			tab3=data_Lcible.replace(","," ").split()
    			tm_score=tab1[1] #recupere le tm-score
    			Laligne=tab2[3] #recupere le nb de résidus alignés
    			Lcible=tab3[2] #recupere le nb de résidus dans la protéine cible
    			return tm_score,Laligne,Lcible

def lire_pdb(fichier_pdb):
    #cette fonction permet d'extraire du fichier PDB les atomes et leur coordonnées 
    content=[] #liste qui contiendra des listes d'atomes avec leur coordonnées
    with open (fichier_pdb) as file: #ouvre le fichier
        ligne="debut" #ligne permet de sauvegarder une ligne du fichier 
        while ((ligne[0:4]!="ATOM") & (ligne != "")): #tant que le début de la ligne n'est pas ATOM 
        #on passe à la ligne suivante (ou vide)
            ligne = file.readline()#passe à la ligne suivante
        while((ligne[0:4]=="ATOM") & (ligne != "")): #ici le début de la ligne est ATOM: on ne parcourt plus le fichier des que les atomes ont été tous parcourus
            tab=ligne.split() #création d'un tableau avec les éléments de la ligne
            content.append(tab) #ajoute a content le tableau issu de la nouvelle ligne
            ligne = file.readline() #passe à la ligne suivante
    return content #return le tableau avec les coordonnées


def calcul_tm_score(fichier_pdb2,fichier_output):
    matrix_distance,matrix_square_distance=mc.distance(fichier_pdb2,fichier_output,"A","A")
    matrix1=dist.min_distance_l_r(matrix_distance)
    matrix2=dist.min_distance_r_l(matrix_distance)
    #tm_score,Lcible,Laligne=Read_tm_score(fichier_output)
    Lcible=len(matrix_distance[0])-1
    d0 = (1.24*(int(Lcible) - 15)**(1/3))-1.8
    s=0
    if(matrix1==matrix2[::-1] ): #si la lecture des 2 matrices renvoie les memes paires
        for i in range(0,len(matrix1)):
            di=matrix1[i][2]
            s += 1/(1+(di/d0)**2)
        s = s/int(Lcible)
    return s

def main():
	#fichier_pdb1 = "1e1v.pdb"
	#fichier_pdb2 = "TM.sup.pdb"
	#fichier_output = "align.txt"
	#print(calcul_tm_score(fichier_pdb1,fichier_pdb2,fichier_output))
    pdb2 = "fichiers_pdb/3fh7.pdb"
    pdb1="fichiers_pdb/3fts.pdb"
    pdb3="ResultsSuperposition/3fh7 vs 3fts/par TM_Align/3fh7_vs_3fts_tm.pdb"
    pdb4="fichiers_pdb/1b38.pdb"
    pdb5="TM.sup_all_atm.pdb"
    #print(calcul_tm_score(pdb1,pdb3))
    #print(calcul_tm_score(pdb2,pdb3))
    #print(calcul_tm_score(pdb4,pdb5))
    #print(calcul_tm_score(pdb2,pdb3))
    #print(calcul_tm_score(pdb4,pdb5))
    pdb6="fichiers_pdb/1aq1.pdb"
    pdb7="ResultsSuperposition/1aq1 vs 1h08/Tm_align/1aq1_1h08_t.pdb"
    pdb8="fichiers_pdb/1h08.pdb"
    pdb9="ResultsSuperposition/1aq1 vs 1h08/Tm_align/1aq1_1h08_t1.pdb"
    pdb10="fichiers_pdb/1jeb.pdb"
    pdb11="fichiers_pdb/3rgk.pdb"
    pdb12="ResultsSuperposition/1jeb vs 3rgk/TM_Align/1jeb_3rgk_t.pdb"
    #print(calcul_tm_score(pdb6,pdb9))
    #print(calcul_tm_score(pdb6,pdb7))
    #print(calcul_tm_score(pdb10,pdb12))
    #print(calcul_tm_score(pdb11,pdb12))
    #print(calcul_tm_score(pdb8,pdb7))
    #print(calcul_tm_score(pdb8,pdb9))
    #print(calcul_tm_score(pdb2,pdb3))

    #tms = []
    #tms.append(calcul_tm_score(pdb2,pdb3))
    #tms.append(calcul_tm_score(pdb4,pdb5))
    #print(tms)
main()