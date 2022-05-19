###### PROJET TRANSVERSE : Superposition de structures 3D par approches multiples #####
développé par CORTIAL Erix, FARUQUE Tanvir, HIERSO Carolynn, LO Maty, élèves ingénieurs à l'Ecole d'Ingénieur Denis Diderot (EIDD, Paris 7) 

# SOMMAIRE
DESCRIPTION DU PROJET
STATUT DU PROJET
INSTALLATION
EXECUTION DU PROGRAMME
ANALYSE DU FICHIER RESULTAT

# DESCRIPTION DU PROJET
Les structures tridimensionnelles (3D) des protéines portent l’ensemble de leurs fonctions essentielles à la vie.
Ces structures ont des repliements 3D qui peuvent se ressembler et il est donc classique de superposer des structures. Il existe donc un 
ensemble important d’outils pour superposer deux structures.
Les outils qui ont été choisis sont : 
- MUSTANG_v3.2.3
- mmligner_1.0.2
- DaliLite.v5
- TM_Align
L'outil developper permet à l'utilisateur l'utilisation des 4 logiciels qui devront êtres installer (voir section # INSTALLATION), et renverra une évaluation détaillée de chacun d'entre eux.

# STATUT DU PROJET 
Developpement fini. Cependant, le code ne permet pas l'ajout d'autres logiciels de superposition.

# INSTALLATION
NOTE IMPORTANTE : tous les logiciels qui devront êtres installé doivent impérativement êtres mis dans le dossier transverse\ pour veiller au bon fonctionnement du code. 

LES PROGRAMMES

- MUSTANG_v3.2.3
telechargement du code source par le lien :
https://lcb.infotech.monash.edu/mustang/mustang_v3.2.3.tgz
extraction de l'archive :
tar -zxvf mustang_v3.2.3.tgz
à l'aide du terminal, pour que le logiciel compile :
aller dans transverse/MUSTANG_v3.2.3/bin, puis taper "make".
Si un message d'erreur apparait pour la commande make, c'est que votre machine ne le comprend pas, taper alors : 
sudo apt-get install g++    
puis relancer make. Le bin contient maintenant l'executable qui fera marcher le code pour la suite.

- DaliLite.v5
telechargement du code source par le lien :
wget http://ekhidna2.biocenter.helsinki.fi/dali/DaliLite.v5.tar.gz
extraction de l'archive :
tar -zxvf DaliLite.v5.tar.gz
à l'aide du terminal, pour que le logiciel compile :
aller dans transverse/DaliLite.v5/bin, puis taper "make clean", puis "make".
Si message d'erreur sur fortran : mettre à jour en tapant :
sudo apt_get install gfortran

- mmligner_1.0.2
telechargement du code source par le lien : 
https://lcb.infotech.monash.edu/mmligner/files/mmligner_1.0.2.tar.gz
extraction de l'archive :
tar -xzf mmligner_1.0.2.tar.gz
à l'aide du terminal, pour que le logiciel compile :
aller dans transverse/mmligner_1.0.2/, puis taper "make".

- TM_Align
dans le terminal, taper :
sudo apt-get update
puis,
sudo apt-get install tm-align

Les 4 logiciels ont bien été installé dans le dossier transverse/

PYTHON3 

taper dans le terminal : sudo apt-get install python3.8.10

python3 a bien été installé.

# EXECUTION DU PROGRAMME 
Dans le terminal, executer le code lancement.py par :
python3 all_function.py [PDB FILE 1] [PDB FILE 2]
Une fois l'execution des programmes terminée, il est possible de consulter dans les dossiers de résultats associés à chaque logiciel le rendu des fichier de superposition, ainsi que le fichier de résultat final resumant le tout.



  
























