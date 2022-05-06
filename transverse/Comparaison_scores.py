#import pandas as pd

#res = []
#data = pd.read_csv('fichier.csv')
#print(data)

#import numpy as np

#a = np.array([[1,4,2],[7,9,4],[0,6,2]])
#np.savetxt('myfile.csv', a, delimiter=',')

import Calcul_TM_score2 as CTM
import Calcul_GDT_TS as GTS
import Calcul_GDT_HA as GHA

pdb3fts="fichiers_pdb/3fts.pdb"
pdb3fh7="fichiers_pdb/3fh7.pdb"
pdbres1tm="ResultsSuperposition/3fh7 vs 3fts/par TM_Align/3fh7_vs_3fts_tm.pdb"
pdbres1dali="ResultsSuperposition/3fh7 vs 3fts/par DaliLite.v5/3fh7_vs_3fts_dali.pdb"
pdbres1mus="ResultsSuperposition/3fh7 vs 3fts/par MUSTANG_v3.2.3/3fh7_vs_3fts_mus.pdb"
pdbres1mm="ResultsSuperposition/3fh7 vs 3fts/par mmligner_1.0.2/3fts.pdb_superposed__1.pdb"

pdb1h08="fichiers_pdb/1h08.pdb"
pdb1aq1="fichiers_pdb/1aq1.pdb"
pdbres2tm="ResultsSuperposition/1aq1 vs 1h08/Tm_align/1aq1_1h08_t.pdb"
pdbres2dali="ResultsSuperposition/1aq1 vs 1h08/Dalli/1aq1_1h08_d.pdb"
pdbres2mus="ResultsSuperposition/1aq1 vs 1h08/Mustang/1aq1_1h08_mu.pdb"
pdbres2mm="ResultsSuperposition/1aq1 vs 1h08/mm_ligner/1h08.pdb_superposed__1.pdb"

pdb1e1v="fichiers_pdb/1e1v.pdb"
pdb1b38="fichiers_pdb/1b38.pdb"
pdbres3tm="ResultsSuperposition/1b38 vs 1e1v/par TM_Align/1b38_vs_1e1v_tmalign.pdb"
pdbres3dali="ResultsSuperposition/1b38 vs 1e1v/par DaliLite.v5/1b38_vs_1e1v_dali.pdb"
pdbres3mus="ResultsSuperposition/1b38 vs 1e1v/par MUSTANG_v3.2.3/1b38_vs_1e1v_mustang.pdb"
pdbres3mm="ResultsSuperposition/1b38 vs 1e1v/par mmligner_1.0.2/1e1v.pdb_superposed__1.pdb"

pdb3rgk="fichiers_pdb/3rgk.pdb"
pdb1jeb="fichiers_pdb/1jeb.pdb"
pdbres4tm="ResultsSuperposition/1jeb vs 3rgk/TM_Align/1jeb_3rgk_t.pdb"
pdbres4dali="ResultsSuperposition/1jeb vs 3rgk/Dalli/1jeb_3rgk_d.pdb"
#pdbres4mus="ResultsSuperposition/1jeb vs 3rgk/Mustang/"
pdbres4mm="ResultsSuperposition/1jeb vs 3rgk/mm_ligner/3rgk.pdb_superposed__1.pdb"

tms_tm = []
RMSDs_tm = []
GDTTSs_tm = []
GDTHAs_tm = []

tms_dali = []
RMSDs_dali = []
GDTTSs_dali = []
GDTHAs_dali = []

tms_mus = []
RMSDs_mus = []
GDTTSs_mus = []
GDTHAs_mus = []

tms_mm = []
RMSDs_mm = []
GDTTSs_mm = []
GDTHAs_mm = []

tms_tm.append(CTM.calcul_tm_score(pdb3fts,pdbres1tm))
tms_tm.append(CTM.calcul_tm_score(pdb1h08,pdbres2tm))
tms_tm.append(CTM.calcul_tm_score(pdb1e1v,pdbres3tm))
tms_tm.append(CTM.calcul_tm_score(pdb3rgk,pdbres4tm))
GDTTSs_tm.append(GTS.calcul_GDT_TS2(pdb3fts,pdbres1tm))
GDTTSs_tm.append(GTS.calcul_GDT_TS2(pdb1h08,pdbres2tm))
GDTTSs_tm.append(GTS.calcul_GDT_TS2(pdb1e1v,pdbres3tm))
GDTTSs_tm.append(GTS.calcul_GDT_TS2(pdb3rgk,pdbres4tm))
GDTHAs_tm.append(GHA.calcul_GDT_HA2(pdb3fts,pdbres1tm))
GDTHAs_tm.append(GHA.calcul_GDT_HA2(pdb1h08,pdbres2tm))
GDTHAs_tm.append(GHA.calcul_GDT_HA2(pdb1e1v,pdbres3tm))
GDTHAs_tm.append(GHA.calcul_GDT_HA2(pdb3rgk,pdbres4tm))

tms_dali.append(CTM.calcul_tm_score(pdb3fh7,pdbres1dali))
tms_dali.append(CTM.calcul_tm_score(pdb1aq1,pdbres2dali))
tms_dali.append(CTM.calcul_tm_score(pdb1b38,pdbres3dali))
tms_dali.append(CTM.calcul_tm_score(pdb1jeb,pdbres4dali))
GDTTSs_dali.append(GTS.calcul_GDT_TS2(pdb3fh7,pdbres1dali))
GDTTSs_dali.append(GTS.calcul_GDT_TS2(pdb1aq1,pdbres2dali))
GDTTSs_dali.append(GTS.calcul_GDT_TS2(pdb1b38,pdbres3dali))
GDTTSs_dali.append(GTS.calcul_GDT_TS2(pdb1jeb,pdbres4dali))
GDTHAs_dali.append(GHA.calcul_GDT_HA2(pdb3fh7,pdbres1dali))
GDTHAs_dali.append(GHA.calcul_GDT_HA2(pdb1aq1,pdbres2dali))
GDTHAs_dali.append(GHA.calcul_GDT_HA2(pdb1b38,pdbres3dali))
GDTHAs_dali.append(GHA.calcul_GDT_HA2(pdb1jeb,pdbres4dali))

tms_mus.append(CTM.calcul_tm_score(pdb3fh7,pdbres1mus))
tms_mus.append(CTM.calcul_tm_score(pdb1aq1,pdbres2mus))
tms_mus.append(CTM.calcul_tm_score(pdb1b38,pdbres3mus))
#tms_mus.append(CTM.calcul_tm_score(pdb1jeb,pdbres4tm))
GDTTSs_mus.append(GTS.calcul_GDT_TS2(pdb3fh7,pdbres1mus))
GDTTSs_mus.append(GTS.calcul_GDT_TS2(pdb1aq1,pdbres2mus))
GDTTSs_mus.append(GTS.calcul_GDT_TS2(pdb1b38,pdbres3mus))
#GDTTSs_mus.append(GTS.calcul_GDT_TS2(pdb1jeb,pdbres4tm))
GDTHAs_mus.append(GHA.calcul_GDT_HA2(pdb3fh7,pdbres1mus))
GDTHAs_mus.append(GHA.calcul_GDT_HA2(pdb1aq1,pdbres2mus))
GDTHAs_mus.append(GHA.calcul_GDT_HA2(pdb1b38,pdbres3mus))
#GDTHAs_mus.append(GHA.calcul_GDT_HA2(pdb1jeb,pdbres4tm))

tms_mm.append(CTM.calcul_tm_score(pdb3fh7,pdbres1mm))
tms_mm.append(CTM.calcul_tm_score(pdb1aq1,pdbres2mm))
tms_mm.append(CTM.calcul_tm_score(pdb1b38,pdbres3mm))
tms_mm.append(CTM.calcul_tm_score(pdb1jeb,pdbres4mm))
GDTTSs_mm.append(GTS.calcul_GDT_TS2(pdb3fh7,pdbres1mm))
GDTTSs_mm.append(GTS.calcul_GDT_TS2(pdb1aq1,pdbres2mm))
GDTTSs_mm.append(GTS.calcul_GDT_TS2(pdb1b38,pdbres3mm))
GDTTSs_mm.append(GTS.calcul_GDT_TS2(pdb1jeb,pdbres4mm))
GDTHAs_mm.append(GHA.calcul_GDT_HA2(pdb3fh7,pdbres1mm))
GDTHAs_mm.append(GHA.calcul_GDT_HA2(pdb1aq1,pdbres2mm))
GDTHAs_mm.append(GHA.calcul_GDT_HA2(pdb1b38,pdbres3mm))
GDTHAs_mm.append(GHA.calcul_GDT_HA2(pdb1jeb,pdbres4mm))

print("Resultats avec TM_Align")
print(tms_tm)
print(GDTTSs_tm)
print(GDTHAs_tm)

print("Resultats avec DaliLite")
print(tms_dali)
print(GDTTSs_dali)
print(GDTHAs_dali)

print("Resultats avec Mustang")
print(tms_mus)
print(GDTTSs_mus)
print(GDTHAs_mus)

print("Resultats avec MM_ligner")
print(tms_mm)
print(GDTTSs_mm)
print(GDTHAs_mm)

import csv

nom_colonnes = ['superposition','RMSD_Dali','RMSD_MMliner','RMSD_TMalign','RMSD_Mustang','TMscore_Dali','TMscore_MMliner','TMscore_TMalign','TMscore_Mustang','GDTTS_Dali','GDTTS_MMliner','GDTTS_TMalign','GDTTS_Mustang','GDTHA_Dali','GDTHA_MMliner','GDTHA_TMalign','GDTHA_Mustang']
fichier = open('Fichier_final.csv','w')
obj = csv.DictWriter(fichier, fieldnames=nom_colonnes)
obj.writeheader()
obj.writerow({'superposition': '3fh7/3fts', 'RMSD_Dali': 'null','RMSD_MMliner': 'null', 'RMSD_TMalign': 'null', 'RMSD_Mustang': 'null', 'TMscore_Dali': tms_dali[0], 'TMscore_MMliner': tms_mm[0], 'TMscore_TMalign': tms_tm[0],'TMscore_Mustang': tms_mus[0], 'GDTTS_Dali': GDTTSs_dali[0], 'GDTTS_MMliner': GDTTSs_mm[0], 'GDTTS_TMalign': GDTTSs_tm[0], 'GDTTS_Mustang': GDTTSs_mus[0], 'GDTHA_Dali': GDTHAs_dali[0], 'GDTHA_MMliner': GDTHAs_mm[0], 'GDTHA_TMalign': GDTHAs_tm[0], 'GDTHA_Mustang': GDTHAs_mus[0]})
obj.writerow({'superposition': '1aq1/1h08', 'RMSD_Dali': 'null','RMSD_MMliner': 'null', 'RMSD_TMalign': 'null', 'RMSD_Mustang': 'null', 'TMscore_Dali': tms_dali[1], 'TMscore_MMliner': tms_mm[1], 'TMscore_TMalign': tms_tm[1],'TMscore_Mustang': tms_mus[1], 'GDTTS_Dali': GDTTSs_dali[1], 'GDTTS_MMliner': GDTTSs_mm[1], 'GDTTS_TMalign': GDTTSs_tm[1], 'GDTTS_Mustang': GDTTSs_mus[1], 'GDTHA_Dali': GDTHAs_dali[1], 'GDTHA_MMliner': GDTHAs_mm[1], 'GDTHA_TMalign': GDTHAs_tm[1], 'GDTHA_Mustang': GDTHAs_mus[1]})
obj.writerow({'superposition': '1b38/1e1v', 'RMSD_Dali': 'null','RMSD_MMliner': 'null', 'RMSD_TMalign': 'null', 'RMSD_Mustang': 'null', 'TMscore_Dali': tms_dali[2], 'TMscore_MMliner': tms_mm[2], 'TMscore_TMalign': tms_tm[2],'TMscore_Mustang': tms_mus[2], 'GDTTS_Dali': GDTTSs_dali[2], 'GDTTS_MMliner': GDTTSs_mm[2], 'GDTTS_TMalign': GDTTSs_tm[2], 'GDTTS_Mustang': GDTTSs_mus[2], 'GDTHA_Dali': GDTHAs_dali[2], 'GDTHA_MMliner': GDTHAs_mm[2], 'GDTHA_TMalign': GDTHAs_tm[2], 'GDTHA_Mustang': GDTHAs_mus[2]})
obj.writerow({'superposition': '1jeb/3rgk', 'RMSD_Dali': 'null','RMSD_MMliner': 'null', 'RMSD_TMalign': 'null', 'RMSD_Mustang': 'null', 'TMscore_Dali': tms_dali[3], 'TMscore_MMliner': tms_mm[3], 'TMscore_TMalign': tms_tm[3],'TMscore_Mustang': 'null', 'GDTTS_Dali': GDTTSs_dali[3], 'GDTTS_MMliner': GDTTSs_mm[3], 'GDTTS_TMalign': GDTTSs_tm[3], 'GDTTS_Mustang': 'null', 'GDTHA_Dali': GDTHAs_dali[3], 'GDTHA_MMliner': GDTHAs_mm[3], 'GDTHA_TMalign': GDTHAs_tm[3], 'GDTHA_Mustang': 'null'})
