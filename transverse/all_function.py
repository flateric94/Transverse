# -*- coding: utf-8 -*-
"""
Created on Sun May 15 17:16:05 2022

@author: tanvi
"""

import dist_min_pairwise as pair
import RMSD as dist1
import GDT_HA as GDT1
import GDT_TS as GDT2
import TM_score as TM
import csv
import matrix_calpha_final as mc
import script as sc

def group_metric(pdb1,pdb2,chaineA,chaineB):
    matrix_distance,matrix_square_distance,matrix_round,matrix=pair.best_pairwise(pdb1,pdb2,chaineA,chaineB)
    r=(dist1.rmsd(matrix_distance,matrix_square_distance,matrix_round,matrix))
    tm=(TM.calcul_tm_score(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix))
    ha=(GDT1.calcul_GDT_HA(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix))
    ts=(GDT2.calcul_GDT_TS(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix))
    print(r,tm,ha,ts)
    return round(r,2),round(tm,2),round(ha,2),round(ts,2)
    

def csv_final():
    headers=["pdb_superposition","RMSD_dali","nbr_residues_sup_dali","RMSD_dali_reC","diff_rmsd_dali","RMSD_tmAlign","nbr_residues_sup_tmAlign","RMSD_tmAlign_reC","diff_rmsd_tmAlign","RMSD_mmLigner","nbr_residues_sup_ligner","RMSD_mmLigner_reC","diff_rmsd_mmLigner","RMSD_Mustang","nbr_residues_sup_Mustang","RMSD_Mustang_reC","diff_rmsd_Mustang","TM_score_Dali","TM_score_tmAlign","TM_score_mmLigner","TM_score_Mustang","TM_score_to_compare","GDT_HA_Dali","GDT_HA_tmAlign","GDT_HA_mmLigner","GDT_HA_Mustang","GDT_TS_Dali","GDT_TS_tmAlign","GDT_TS_mmLigner","GDT_TS_Mustang"]
    with open(sc.path+"/Resultats/Result/Result_notre_base/total_result.csv", "w",newline='') as file:
         f_csv = csv.DictWriter(file, headers)
         f_csv.writeheader()
    file.close()

    
def add_result(name,pdb1,chaineA, pdb2dali, chaineBdali, txtDali, pdb2align, chaineBalign, txtAlign, pdb2liner, chaineBliner, txtLigner,pdb2mus, chaineBmus,txtMus):
    #Dali
    rdali,tmdali,hadali,tsdali=group_metric(pdb1, pdb2dali, chaineA, chaineBdali)
    Nbr_res_Dali, rmsd_Dali, DifferenceDali=dist1.comparison_RMSD(rdali,txtDali,3, 3, 3, 4)
    tabdali=["Dali",rmsd_Dali,Nbr_res_Dali,rdali,round(DifferenceDali,2),tmdali,"NA",hadali,tsdali]
    #Tm_Align
    ralign,tmalign,haalign,tsalign=group_metric(pdb1, pdb2align, chaineA, chaineBalign)
    Nbr_res_align, rmsd_align, Differencealign=dist1.comparison_RMSD(ralign,txtAlign,16, 16, 4, 2)
    tm_score,Laligne,Lcible=TM.Read_tm_score(txtAlign)
    tabalign=["TM_Align",rmsd_align,Nbr_res_align,ralign,round(Differencealign,2),tmalign,round(float(tm_score),2),haalign,tsalign]
    #mmLigner
    rliner,tmliner,haliner,tsliner=group_metric(pdb1, pdb2liner, chaineA, chaineBliner)
    Nbr_res_ligner, rmsd_ligner, Differenceligner=dist1.comparison_RMSD(rliner,txtLigner,2, 1, 2, 2)
    tabliner=["mmLigner",round(float(rmsd_ligner),2),Nbr_res_ligner,rliner,round(Differenceligner,2),tmliner,"NA",haliner,tsliner]
    #Mustang
    rmus,tmmus,hamus,tsmus=group_metric(pdb1, pdb2mus, chaineA, chaineBmus)
    Nbr_res_mustang, rmsd_mustang, Differencemustang=dist1.comparison_RMSD(rmus,txtMus,3, 7, 2, 0)
    tabmu=["Mustang",rmsd_mustang,"NA",rmus,round(Differencemustang,2),tmmus,"NA",hamus,tsmus]
    headers=["pdb_superposition","RMSD_dali","nbr_residues_sup_dali","RMSD_dali_reC","diff_rmsd_dali","RMSD_tmAlign","nbr_residues_sup_tmAlign","RMSD_tmAlign_reC","diff_rmsd_tmAlign","RMSD_mmLigner","nbr_residues_sup_ligner","RMSD_mmLigner_reC","diff_rmsd_mmLigner","RMSD_Mustang","nbr_residues_sup_Mustang","RMSD_Mustang_reC","diff_rmsd_Mustang","TM_score_Dali","TM_score_tmAlign","TM_score_mmLigner","TM_score_Mustang","TM_score_to_compare","GDT_HA_Dali","GDT_HA_tmAlign","GDT_HA_mmLigner","GDT_HA_Mustang","GDT_TS_Dali","GDT_TS_tmAlign","GDT_TS_mmLigner","GDT_TS_Mustang"]
    headersfichier=["Method","RMSD","nbr_residues_sup","RMSD_Recalculated","diff_2_rmsd","TM_score","TM_score_to_compare","GDT_HA","GDT_TS"]
    metric1=[{"pdb_superposition":name,"RMSD_dali":rmsd_Dali,"RMSD_dali_reC":rdali,"RMSD_tmAlign":rmsd_align,"RMSD_tmAlign_reC":ralign,"RMSD_mmLigner":rmsd_ligner,"RMSD_mmLigner_reC":rliner,"RMSD_Mustang":rmsd_mustang,"RMSD_Mustang_reC":rmus,"TM_score_Dali":tmdali,"TM_score_tmAlign":tmalign,"TM_score_mmLigner":tmliner,"TM_score_Mustang":tmmus,"TM_score_to_compare":tm_score,"GDT_HA_Dali":hadali,"GDT_HA_tmAlign":haalign,"GDT_HA_mmLigner":haliner,"GDT_HA_Mustang":hamus,"GDT_TS_Dali":tsdali,"GDT_TS_tmAlign":tsalign,"GDT_TS_mmLigner":tsliner,"GDT_TS_Mustang":tsmus,"nbr_residues_sup_dali":Nbr_res_Dali,"nbr_residues_sup_tmAlign":Nbr_res_align,"nbr_residues_sup_ligner":Nbr_res_ligner,"nbr_residues_sup_Mustang":"NA","diff_rmsd_dali":DifferenceDali,"diff_rmsd_tmAlign":Differencealign,"diff_rmsd_mmLigner":Differenceligner,"diff_rmsd_Mustang":Differencemustang}]
    with open(sc.path+"/Resultats/Result/Result_notre_base/total_result.csv", "a",newline='') as f:
        f_csv=csv.DictWriter(f, headers)
        f_csv.writerows(metric1)
    f.close()
    file = open(sc.path+"/Resultats/Result/Result_notre_base/"+name+".txt", "w")
    file.write("Superposition "+name+"\n\n")
    data=name.split("_") 
    file.write("Query: "+data[0]+" (reference)\t size: "+mc.size_pdb(pdb1,chaineA)+"\n")
    file.write("Target: "+data[1]+"\t\t size: "+mc.size_pdb(pdb2dali,chaineBdali)+"\n\n")
    for i in range (0,len(headersfichier)):
        if(i in {1,8}):
            file.write("\t")
        file.write(headersfichier[i]+"\t")
    file.write("\n")
    for i in range (0,len(tabdali)):
        if(i in {6,3}):
            file.write("\t")
        file.write(str(tabdali[i])+"\t\t")
    file.write("\n")
    for i in range (0,len(tabalign)):
        if(i in {6,3}):
            file.write("\t")
        if(i==0):
            file.write(str(tabalign[i])+"\t")
        else:
            file.write(str(tabalign[i])+"\t\t")
    file.write("\n")
    for i in range (0,len(tabliner)):
        if(i in {6,3}):
            file.write("\t")
        if(i==0):
            file.write(str(tabliner[i])+"\t")
        else:
            file.write(str(tabliner[i])+"\t\t")
    file.write("\n")
    for i in range (0,len(tabmu)):
        if(i in {6,3}):
            file.write("\t")
        if(i==0):
            file.write(str(tabmu[i])+"\t")
        else:
            file.write(str(tabmu[i])+"\t\t")
    file.close()
    
def main():
    """
    pdb1 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx.pdb"
    pdb2dali="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\dalitan\\sup1xwc.pdb"
    #pdb3 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\3fts.pdb"
    #pdb4="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Comparaison 3fts-3fh7\\via Dalilite\\sup2.pdb"
    pdb2mus="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx_1xwc_mu.pdb"
    pdb2align="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\1xwc vs 3trx\\1xwc_3trx_t.pdb"
    pdb2liner="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\1xwc.pdb_superposed__1.pdb"
    txtDali="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\dalitan\\3trxA.txt"
    txtAlign="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\1xwc vs 3trx\\1xwc_3trx_t.txt"
    txtligner="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\1xwc_3trx.txt"
    txtMus="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx_1xwc_mu.rms_rot"
    
    #group_metric(pdb1,pdb2dali,'A','A')
    '''Vérification des paires avec matrice couleur avant et après alignement:'''
    #dist1.createCSV(pdb1,pdb2,'A','A','3trx')
    '''Creation du csv et du fichier texte: '''
    #csv_final()
    #add_result("3trx_1xwc", pdb1, "A", pdb2dali, "A",txtDali, pdb2align, "A",txtAlign, pdb2liner, "A",txtligner, pdb2mus, "B",txtMus)
    """
    #csv_final()
    # Fichier intput de la query (qui n'a pas bougé)
    pdb_i = sc.user_input1
    # Nom du fichier recapitulatif résultat
    name=''+sc.root1+'_'+sc.root2
    # Chaine du fichier input query
    chaineA= str(sc.chaine_1)
    # Pdb ouput superposé
    pdb_dali = sc.path+"/Resultats/Resultat_DaliLite/"+sc.nom_result_dali+".pdb"
    pdb_mu = sc.path+"/Resultats/Resultat_Mustang/"+sc.nom_result_mustang+".pdb"
    pdb_tm = sc.path+"/Resultats/Resultat_TMalign/"+sc.nom_result_tm+".pdb"
    pdb_ml = sc.path+"/Resultats/Resultat_mmLigner/"+sc.root2+".pdb_superposed__1.pdb"
    # Chaine fichier output
    chaine_dali = "A"
    chaine_mu ="B"
    chaine_tm="A"
    chaine_ml ="A"
    # Fichier texte
    txt_dali = sc.path+"/Resultats/Resultat_DaliLite/"+sc.root1+sc.chaine_1+".txt"
    txt_mu = sc.path+"/Resultats/Resultat_Mustang/"+sc.nom_result_mustang+".rms_rot"
    txt_tm = sc.path+"/Resultats/Resultat_TMalign/"+sc.nom_result_tm+".txt"
    txt_ml = sc.path+"/Resultats/Resultat_mmLigner/"+sc.root1+".pdb_vs_"+sc.root2+".pdb__1.stats"
    add_result(name,pdb_i,chaineA,pdb_dali,chaine_dali,txt_dali,pdb_tm,chaine_tm,txt_tm,pdb_ml,chaine_ml,txt_ml,pdb_mu,chaine_mu,txt_mu)
    
main()
