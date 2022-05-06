import os
import sys
import shutil
import Bio
from Bio.PDB import PDBParser
from Bio.PDB.PDBExceptions import PDBConstructionWarning
import warnings

for i in range(5):
    print(sys.argv[i])

# generer les 2 fichiers pdb avec des input files,
print("repertoire actuel : "+os.getcwd())
user_input1 = sys.argv[1]
chaine_1 = sys.argv[2] 
assert os.path.exists(user_input1), "Ce chemin n'existe pas"
pdb_tocompare = open(user_input1, 'r+')

user_input2 = sys.argv[3]
chaine_2 = sys.argv[4]
assert os.path.exists(user_input2), "Ce chemin n'existe pas"
pdb_comparing = open(user_input2, 'r+')


# verifier que le fichier est sous le bon format
root1, extension1 = os.path.splitext(os.path.basename(user_input1))
root2, extension2 = os.path.splitext(os.path.basename(user_input2))
if (extension1 != '.pdb' or extension2 != '.pdb'):
    print('ERROR : Ce ne sont pas des fichiers au format .pdb')
    pdb_tocompare.close()
    pdb_comparing.close()
    sys.exit()

  
# verifier que les fichiers PDB sont rédigés sans erreurs
parser = PDBParser()
prot1_id = root1
prot2_id = root2
prot1_file = user_input1
prot2_file = user_input2
structure1 = parser.get_structure(prot1_id, prot1_file)
structure2 = parser.get_structure(prot2_id, prot2_file)

"""
with warnings.catch_warnings():
    if warnings.filterwarnings("ignore", category=PDBConstructionWarning):
        try:
            structure1 = parser.get_structure(prot1_id, prot1_file)
        except PDBConstructionWarning as message :
            print("erreur rencontrée lors de l'ouverture du fichier nomme "+prot1_id+" : verifié si des champs sont manquants")
            pdb_tocompare.close()
            pdb_comparing.close()
            sys.exit()
        try:
            structure2 = parser.get_structure(prot2_id, prot2_file)
        except PDBConstructionWarning as message :
            print("erreur rencontrée lors de l'ouverture du fichier nomme "+prot2_id+" : verifié si des champs sont manquants")
            pdb_tocompare.close()
            pdb_comparing.close()
            sys.exit()
"""

warnings.filterwarnings("ignore")
try:
    structure1 = parser.get_structure(prot1_id, prot1_file)
except Bio.PDB.PDBExceptions.PDBConstructionWarning or ResourceWarning:
    print("erreur rencontrée lors de l'ouverture du fichier nomme "+prot1_id+" : verifié si des champs sont manquants")
    pdb_tocompare.close()
    pdb_comparing.close()
    sys.exit()

try :
    structure2 = parser.get_structure(prot2_id, prot2_file)
except Bio.PDB.PDBExceptions.PDBConstructionWarning or ResourceWarning:
    print("erreur rencontrée lors de l'ouverture du fichier nomme "+prot2_id+" : verifié si des champs sont manquants")
    pdb_tocompare.close()
    pdb_comparing.close()
    sys.exit()

# les lancers (simultanement) dans tout les logiciels.

path = os.getcwd()

### MUSTANG 
os.chdir("./MUSTANG_v3.2.3")
chemin = os.getcwd()
nom_result_mustang = input("Nommez votre fichier de resultat (MUSTANG_v3.2.3) : ")
cmd = './bin/mustang-3.2.3 -i '+user_input2+' '+user_input1+' -r ON -o '+nom_result_mustang
os.system(cmd)

# recuperer les resultats de la superposition dans un dossier prévu pour :

shutil.move(chemin+'/'+nom_result_mustang+".pdb", path+"/Resultats/Resultat_Mustang/"+nom_result_mustang+".pdb")
shutil.move(chemin+'/'+nom_result_mustang+".rms_rot", path+"/Resultats/Resultat_Mustang/"+nom_result_mustang+".rms_rot")
os.remove(chemin+'/'+nom_result_mustang+".html")


### DALILITE
os.chdir("./..")
os.chdir("./DaliLite.v5/bin/") 
chemin = os.getcwd()
nom_result_dali = input("Nommez votre fichier de resultat (DaliLite.v5) : ")
cmd1 = './import.pl --pdbfile '+user_input1+' --pdbid '+root1+' [ --dat ./DAT ]'
cmd2 = './import.pl --pdbfile '+user_input2+' --pdbid '+root2+' [ --dat ./DAT ]'
cmd3 = './dali.pl --cd1 '+root1+chaine_1+' --cd2 '+root2+chaine_2+' --dat1 ./DAT --dat2 ./DAT'
cmd4 =  './applymatrix.pl '+user_input2+' < '+root1+chaine_1+'.txt > '+nom_result_dali+'.pdb'
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)
os.system(cmd4)

# recuperer les resultats de la superposition dans un dossier prévu pour :

shutil.move(chemin+'/'+nom_result_dali+".pdb", path+"/Resultats/Resultat_DaliLite/"+nom_result_dali+".pdb")
shutil.move(chemin+'/'+root1+chaine_1+'.txt', path+"/Resultats/Resultat_DaliLite/"+root1+chaine_1+'.txt')

### MMLINER
os.chdir("./../..")
os.chdir("./mmligner_1.0.2/bin/")
chemin = os.getcwd()

#cmd = "./mmligner "+user_input1+":"+str(chaine_1)+" "+user_input2+":"+str(chaine_2)+" --superpose "
cmd = "./mmligner "+user_input2+" "+user_input1+" --superpose "
os.system(cmd) 

# recuperer les resultats de la superposition dans un dossier prévu pour :

shutil.move(chemin+'/'+root1+".pdb_superposed__1.pdb", path+"/Resultats/Resultat_mmLigner/"+root1+".pdb_superposed__1.pdb")

### TM_Align

os.chdir("./../..")
os.chdir("./TM_Align")
chemin = os.getcwd()
nom_result_tm = input("Nommez votre fichier de resultat (TM_Align) : ")
cmd = "TMalign "+user_input1+" "+user_input2+" -o "+nom_result_tm+" > "+nom_result_tm+".txt"
os.system(cmd)
# recuperer les resultats de la superposition dans un dossier prévu pour :

shutil.move(chemin+'/'+nom_result_tm+'.pdb', path+"/Resultats/Resultat_TMalign/"+nom_result_tm+".pdb")
shutil.move(chemin+'/'+nom_result_tm+'.txt', path+"/Resultats/Resultat_TMalign/"+nom_result_tm+".txt")

print("\n###### RESULTAT SUPERPOSITION "+root1+" "+root2+" ######")
print("Résumé des fichiers de sorties :")
print(" - dans Resultats/Resultat_Mustang/")
print("    "+nom_result_mustang+".pdb")
print("    "+nom_result_mustang+".rms_rot")  
print(" - dans Resultats/Resultat_DaliLite/")
print("    "+nom_result_dali+".pdb")
print("    "+root1+chaine_1+'.txt')  
print(" - dans Resultats/Resultat_mmLigner/")
print("    "+root2+".pdb_superposed__1.pdb")
print(" - dans Resultats/Resultat_TMalign/")
print("    "+nom_result_tm+'.pdb')
print("    "+nom_result_tm+'.txt') 
print("Pour effectuer une nouvelle superposition, relancer le programme")


# On ferme les fichiers .pdb :
pdb_tocompare.close()
pdb_comparing.close()
