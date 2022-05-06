# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:16:58 2022

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

def Calcul_RMSD(fichier_pdb1,fichier_pdb2): #pdb1 original target PDB file, pdb2 fichier avec coordonnées transformées
    #Calcul le rmsd en prenant en compte tous les atomes
    theorique=lire_pdb(fichier_pdb1) #creer le tableau de coordonées pour le 1er pdb
    rotation=lire_pdb(fichier_pdb2)#creer le tableau de coordonées pour le 2eme pdb
    rmsd=0 #initialisation du rmsd
    for i in range(0,len(theorique)): #Parcourir les tableaux (utilise les coordonnées de chaque atome)
        if(theorique[i][2]=="CA"):
            rmsd+=(float(theorique[i][6])-float(rotation[i][6]))**2+(float(theorique[i][7])-float(rotation[i][7]))**2+(float(theorique[i][8])-float(rotation[i][8]))**2
    rmsd=rmsd/len(theorique) 
    return math.sqrt(rmsd) #calcul et retourne RMSD

def comparaison_RMSD(fichier_pdb1,fichier_pdb2,fichier_a_ouvrir, pos_ligne_rmsd,pos_ligne_nbr, pos_rmsd, pos_N): 
    #pdb1 original target PDB file, pdb2 fichier avec coordonnées transformées,pos_ligne_rmsd=ligne ou se situe le rmsd,
    #pos_ligne_nbr=ligne ou se situe le nbr de résidus superposés,
    #pos_rmsd: position du rmsd dans la ligne,pos_N: position de N dans la ligne
    #Cette fonction sera la seule appelée: elle rassemble toutes les autres fonctions
    rmsd_reel=Calcul_RMSD(fichier_pdb1, fichier_pdb2)
    rmsd_logiciel,Nbr_res_logiciel=Read_rmsd(fichier_a_ouvrir, pos_ligne_rmsd,pos_ligne_nbr, pos_rmsd, pos_N)
    Difference=rmsd_reel-float(rmsd_logiciel) #difference entre le rmsd du logiciel et le notre= 0 si le même; 
    #<1 le logiciel donne un rmsd trop grand; >1 le logiciel donne un rmsd trop petit
    return Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference #renvoie le nombre de résidus utilisé par le logiciel pour calculer le rmsd, 
    #le rmsd calculé par le logiciel, le rmsd calculé par la fonction Calcul_RMSD et la différence entre ces 2 rmsd 
    

def create_fichier(Nom,logiciel,Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference):
    #Cette fonction ecrit les resultats des 4 logiciels dans un fichier
    fichier = open(Nom, "a")
    fichier.write("\t\tMéthode "+logiciel+"\nRésidus superposés par le logiciel: "+str(Nbr_res_logiciel)+"\nRMSD calculé par le logiciel "+str(rmsd_logiciel)+"\nRMSD recalculé: "+str(rmsd_reel)+"\nDiférence RMSD (si <0, RMSDlogiciel plus grand): "+str(Difference)+"\n")
    fichier.close()

def main():
    #Test des fonctions:
    #rmsd1, nbr_residu=Read_rmsd("1b38A.txt",3,3,3,4)
    #print("Le rmsd est "+rmsd1)
    #print("Le nombre de résidus comparé est "+nbr_residu)
    #print((lire_pdb("sup.pdb")))
    #print(Calcul_RMSD("1e1v.pdb","TM.sup_atm.pdb"))
    #Ecrit dans le fichier texte pour Dalilite 1e1v
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\1b38.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via Dalilite\\sup.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via Dalilite\\1e1vA.txt", 3, 3, 3, 4)
    create_fichier("Comparaison_1e1V_1b38.txt","Dalilite",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)
    #TM_Align
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\1b38.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via TM_Align\\TM.sup_all_atm.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via TM_Align\\align.txt", 16, 16, 4, 2)
    create_fichier("Comparaison_1e1V_1b38.txt","TM_Align",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)
    #Mustang 
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\1b38.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via MUSTANG\\resultat_test-1e1v_1b38.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 1e1v-1b38\\Via MUSTANG\\resultat_test-1e1v_1b38.rms_rot", 3, 7, 2, 0)
    create_fichier("Comparaison_1e1V_1b38.txt","MUSTANG",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)                          

    #Ecrit dans le fichier texte pour Dalilite 3fts
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\3fh7.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via Dalilite\\sup2.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via Dalilite\\3ftsA.txt", 3, 3, 3, 4)
    create_fichier("Comparaison_3fts_3fh7.txt","Dalilite",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)
    #TM_Align
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\3fh7.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via TM_Align\\TM.sup_all_atm.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via TM_Align\\align.txt", 16, 16, 4, 2)
    create_fichier("Comparaison_3fts_3fh7.txt","TM_Align",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)
    #Mustang 
    Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference = comparaison_RMSD("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\3fh7.pdb","C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via MUSTANG\\resultat_test-3fts_3fh7.pdb", "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\Via MUSTANG\\resultat_test-3fts_3fh7.rms_rot", 3, 7, 2, 0)
    create_fichier("Comparaison_3fts_3fh7.txt","MUSTANG",Nbr_res_logiciel, rmsd_logiciel, rmsd_reel, Difference)                          

main()


    