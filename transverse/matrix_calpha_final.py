# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:16:58 2022

@author: carolynn
"""
import math
import csv



def read_pdb(file_pdb, chaine):
    # cette fonction permet d'extraire du fichier PDB les atomes et leur coordonnées
    content = []  # liste qui contiendra des listes d'atomes avec leur coordonnées
    with open(file_pdb) as file:  # ouvre le fichier
        line = "debut"  # ligne permet de sauvegarder une ligne du fichier
        while (line[0:4] != "ATOM") and (line != ""):
            line = file.readline()  # passe à la ligne suivante
        while line[0:6] == "ATOM  " or line[0:6] == "HETATM" or line[
                                                                0:6] == "TER   ":  # tant que le début de la ligne n'est pas ATOM
            # on passe à la ligne suivante (ou vide)
            # ici le début de la ligne est ATOM: on ne parcourt plus le fichier des que les atomes ont été tous parcourus
            tab = line.split()
            if tab[0] == "ATOM":
                if tab[4] == chaine:
                    if tab[2] == 'CA':  # On conserve que les lignes qui contiennent des CA
                        content.append(tab)
            line = file.readline()

    return content  # return le tableau avec les coordonnées

def size_pdb(file_pdb, chaine): 
    # return Longueur d'une séquence
    with open(file_pdb) as file:  # ouvre le fichier
        line = "debut"  # ligne permet de sauvegarder une ligne du fichier
        while (line[0:5] != "DBREF") and (line != ""):
            line = file.readline()  # passe à la ligne suivante
        while line[0:5] == "DBREF":
            # on passe à la ligne suivante (ou vide)
            tab = line.split()
            if tab[2] == chaine:
               c=tab[4]
            line = file.readline()
        return c

def distance(file_1, file_2, chaineA, chaineB):
    pdb_1 = read_pdb(file_1, chaineA)
    pdb_2 = read_pdb(file_2, chaineB)
    matrix_distance = []
    matrix_square_distance = []
    matrix_distance_round = []
    # Le fichier de plus grande taille est en haut
    # Le fichier de plus petite taille est en bas
    maximun = max(len(pdb_1), len(pdb_2))
    temp = pdb_2.copy()
    if len(pdb_1) == maximun:
        pdb_2 = pdb_1.copy()
        pdb_1 = temp.copy()
    matrix_distance.append([])
    matrix_square_distance.append([])
    matrix_distance_round.append([])
    # On souhaite mettre les CA dans la première ligne de notre matrice
    matrix_distance[0].append('number_atomes')
    matrix_square_distance[0].append('number_atomes')
    matrix_distance_round[0].append('number_atomes')
    distance = 0  # initialisation du rmsd
    distance_square = 0
    for i in range(0, len(pdb_1)):  # Parcourir les tableaux (utilise les coordonnées de chaque atome)
        # Dans la première ligne de notre matrice, on a les numéro des CA du premier fichier

        matrix_distance[0].append(i)
        matrix_square_distance[0].append(i)
        matrix_distance_round[0].append(i)
        for j in range(0, len(pdb_2)):
            if i == 0:
                # Le premier élément des autres linges correspondent aux CA des la deuxième séquence
                matrix_distance.append([j])
                matrix_square_distance.append([j])
                matrix_distance_round.append([j])
            distance = math.sqrt((float(float(pdb_1[i][6]) - float(pdb_2[j][6]))) ** 2 + (
                float(float(pdb_1[i][7]) - float(pdb_2[j][7]))) ** 2 + (
                                     float(float(pdb_1[i][8]) - float(pdb_2[j][8]))) ** 2)
            if(distance<30):
                distance_round = round(distance)
            else:
                distance_round=30
            distance_square = (float(float(pdb_1[i][6]) - float(pdb_2[j][6]))) ** 2 + (
                float(float(pdb_1[i][7]) - float(pdb_2[j][7]))) ** 2 + (
                                  float(float(pdb_1[i][8]) - float(pdb_2[j][8]))) ** 2
            matrix_distance[j + 1].append(distance)
            matrix_distance_round[j + 1].append(distance_round)
            matrix_square_distance[j + 1].append(distance_square)

    return matrix_distance, matrix_square_distance, matrix_distance_round


def write(pdb1, pdb2, chaineA, chaineB,name_pdb):
    matrix, matrix_square,matrix_round = distance(pdb1, pdb2, chaineA, chaineB)
    with open(name_pdb+"_matrix_origin.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerows(matrix_round)
    file.close()

'''
def main():
    #pdb1 = "C:\\Users\\Carolynn\\Desktop\\EIDD\\2A\\Semestre2\\PT\\1fxi.pdb"
    #pdb2 = "C:\\Users\\Carolynn\\Desktop\\EIDD\\2A\\Semestre2\\PT\\sup_1.pdb"
    pdb1 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\Essai3.pdb"
    pdb2 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\Essai2.pdb"
    pdb1 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx.pdb"
    pdb2="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx_1xwc_d.pdb"
    # read_pdb(pdb1, "A")
    matrix, matrix_square, matrix_round = distance(pdb1, pdb2, "A", "A")
    print(matrix)


    # seq_1 = sequence(pdb1)
    # print(seq_1)
    # Pb indice string mettre des espaces
    # print(distance(pdb1,pdb1))


main()
'''
