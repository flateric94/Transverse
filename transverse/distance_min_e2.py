# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 18:09:36 2022

@author: tanvi
"""
import matrix_calpha_final as mc
import math
import copy

#pour éviter les croisements: méthode de dali (hexa) ou on met un curseur et à chaque fois on repare de ce curseur (cherche le min à partir de la)
def min_distance_ligne(matrix):
    #cette fonction permet de trouver la distance min entre un atome de seq 1 et un atome de seq 2
    #elle évite de choisir 2 fois le même atome
    seq1_size=len(matrix[0])-1 #sequence la plus grande
    seq2_size=len(matrix)-1 #la plus petite
    pairs=[] #stocks les numeros des atomes de la paires et la distance min entre les 2
    stockI=1 #pour se rappeler de la position de la meilleure paire 
    stockJ=1
    nbri=1
    nbrj=1
    counter=matrix[1][1] #pour comparer le min actuel aux autres distances
    for i in range(1,seq2_size+1): #parcourt les atomes de la seq la plus petite
        counter=matrix[i][1] #réinitialise counter
        stockI=matrix[i][0] #réinitialise sotckI
        stockJ=matrix[0][1] #réinitialise sotckJ
        nbri=i
        nbrj=1
        for j in range (1,seq1_size+1): #parcourt les atomes de la seq la plus grande
            if(counter>matrix[i][j]): #vérifie que cette distance est bien un nouveau min
                    counter=matrix[i][j] #nouveau min
                    stockJ=matrix[0][j] #nouvel atome à appreiller
                    nbrj=j
        pairs.append([stockI,stockJ,counter,nbri,nbrj]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
    return pairs

def min_distance_colonne(matrix):
    #cette fonction permet de trouver la distance min entre un atome de seq 1 et un atome de seq 2
    #elle évite de choisir 2 fois le même atome
    seq1_size=len(matrix[0])-1 #sequence la plus grande
    seq2_size=len(matrix)-1 #la plus petite
    pairs=[] #stocks les numeros des atomes de la paires et la distance min entre les 2
    stockI=1 #pour se rappeler de la position de la meilleure paire 
    stockJ=1
    nbri=1
    nbrj=1
    counter=matrix[1][1] #pour comparer le min actuel aux autres distances
    for i in range(1,seq1_size+1): #parcourt les atomes de la seq la plus petite
        counter=matrix[1][i] #réinitialise counter
        stockI=matrix[0][i] #réinitialise sotckI
        stockJ=matrix[0][1] #réinitialise sotckJ
        nbri=i
        nbrj=1
        for j in range (1,seq2_size+1): #parcourt les atomes de la seq la plus grande
            if(counter>matrix[j][i]): #vérifie que cette distance est bien un nouveau min
                    counter=matrix[j][i] #nouveau min
                    stockJ=matrix[j][0] #nouvel atome à appreiller
                    nbrj=j
        pairs.append([stockJ,stockI,counter,nbrj,nbri]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
    return pairs

def same_list(list1,list2):
    liste=copy.deepcopy(list1)
    #print(liste)
    size=len(list1)
    count=0
    for i in range(0,len(liste)):
        size=i-count
        if(liste[size] not in list2):
            del liste[size]
            count+=1
    return liste
    
def sort_list(liste):
    liste.sort(key= lambda x: x[2])
    return liste

def delete_liste_version1(liste): #supprime la distance si le i ou le j est inférieure aux indices i ou j précédents

    stockI=liste[0][3]
    stockJ=liste[0][4]
    size=len(liste)
    count=0
    for i in range (1,len(liste)-1):
        size = i - count
        if liste[size+1][3]<=liste[size][3] or liste[size+1][4]<=liste[size][4]:
            del liste[size+1]
            count+=1
    return liste

def delete(liste):
    list_i = []
    count=0
    size = len(liste)
    for i in range(0,len(liste)):
        size = i-count
        if liste[size][3] not in list_i:
            list_i.append(liste[size][3])
        else :
            del liste[size]
            count+=1
    list_j = []
    count = 0
    size = len(liste)
    for i in range(0, len(liste)):
        size = i - count
        if liste[size][4] not in list_j:
            list_j.append(liste[size][4])
        else:
            del liste[size]
            count += 1
    return liste

def color_matrice(liste,matrix):
    matrix_color=copy.deepcopy(matrix)
    for i in range (0,len(liste)):
        matrix_color[liste[i][[3]][liste[i][4]]=-1
    return matrix_color


def rmsd(pdb1,pdb2,chaineA,chaineB):
    rmsd=0
    matrix_distance,matrix_square_distance,matrix_round=mc.distance(pdb1,pdb2,chaineA,chaineB)
    #print(matrix_round)
    matrix = same_list(min_distance_ligne(matrix_distance),min_distance_colonne(matrix_distance))
    print(len(matrix))
    matrix =sort_list(matrix)
    matrix = delete(matrix)
    write_csv(color_matrice(matrix, matrix_round))
    #if(matrix1==matrix2[::-1] ): #si la lecture des 2 matrices renvoie les memes paires
    for i in range(0,len(matrix)):
        rmsd+=(matrix_square_distance[matrix[i][3]][matrix[i][4]])
    return math.sqrt(rmsd/len(matrix))

def write_csv(matrix_color):
    with open("matrix_to_compare.csv", "w") as file:
        writer=csv.writer(file)
        writer.writerows(matrix_color)
    file.close()

def main():

    #pdb1 = "/home/administrateur/Bureau/Essai.pdb"
    #pdb2 = "/home/administrateur/Bureau/Essai3.pdb"
    #matrix_distance,matrix_square_distance=mc.distance(pdb1,pdb2,"A","A")
    #print(matrix_distance)
    #print(min_distance_ligne(matrix_distance))
    #print(min_distance_colonne(matrix_distance))
    #print(same_list(min_distance_ligne(matrix_distance),min_distance_colonne(matrix_distance)))
    #list1=min_distance_ligne(matrix_distance)
    #list2=min_distance_colonne(matrix_distance)
    #list1[0][2]=2
    #list2[0][2]=2
    #print(same_list(min_distance_ligne(matrix_distance),min_distance_colonne(matrix_distance)))
    pdb1 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx.pdb"
    pdb2="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\1xwc vs 3trx\\1xwc_3trx_t.pdb"
    #print(sort_list(same_list(list1,list2)))
    print(rmsd(pdb1,pdb2,"A","A"))
main()
