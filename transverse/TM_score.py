
import matrix_calpha_final as mc


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

    
    
def calcul_tm_score(pdb1,chaineA,matrix_distance,matrix_square_distance,matrix_round,matrix):
    Lcible=mc.size_pdb(pdb1,chaineA)
    d0 = (1.24*(int(Lcible) - 15)**(1/3))-1.8
    s=0
    for i in range(0,len(matrix)):
        di=matrix[i][2]
        s += 1/(1+(di/d0)**2)
    s = s/int(Lcible)
    return s
