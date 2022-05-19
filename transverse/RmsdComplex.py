import matrix_calpha_final as mc
import math
import copy


def matrix_score_l_r(matrix,ligne,colonne):
    #cette fonction permet de trouver la distance min entre un atome de seq 1 et un atome de seq 2
    #elle évite de choisir 2 fois le même atome
    
    matrix_color=copy.deepcopy(matrix)
    seq1_size=len(matrix[0])-1 #sequence la plus grande
    seq2_size=len(matrix)-1 #la plus petite
    pairs=[] #stocks les numeros des atomes de la paires et la distance min entre les 2
    j=colonne
    i=ligne
    preI=i
    preJ=j
    stockJ=matrix[0][j] #nouvel atome à appreiller
    stockI=matrix[i][0]
    counter=matrix[i][j] #pour comparer le min actuel aux autres distances
    count_tour=1
    while(i!=seq2_size or j!=seq1_size):
      if(i!=seq2_size and j!=seq1_size):
        counter=matrix[i+1][j+1] #réinitialise counter
        if(counter>matrix[i+1][j]): 
          counter=matrix[i+1][j] #nouveau min
          if(counter>matrix[i][j+1]):
            counter=matrix[i][j+1]  
            j+=1
            stockJ=matrix[0][j] #nouvel atome à appreiller
            stockI=matrix[i][0] #nouvel atome à appreiller
            count_tour=0
          else:
            i+=1
            stockJ=matrix[0][j] #nouvel atome à appreiller
            stockI=matrix[i][0] #nouvel atome à appreiller
            count_tour=1
        elif (counter>matrix[i][j+1]):
          counter=matrix[i][j+1]  
          j+=1
          stockJ=matrix[0][j] #nouvel atome à appreiller
          stockI=matrix[i][0] #nouvel atome à appreiller
          count_tour=1
        else:
          i+=1
          j+=1
          if(preI==i-1 and preJ==j-1 and count_tour==1):
              count_tour=0
              matrix_color[i-1][j-1]=-1
              pairs.append([stockI,stockJ,matrix[i-1][j-1],i-1,j-1]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
          stockJ=matrix[0][j] #nouvel atome à appreiller
          stockI=matrix[i][0] #nouvel atome à appreiller
          matrix_color[i][j]=-1
          count_tour=0
          pairs.append([stockI,stockJ,counter,i,j]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
      elif(i==seq2_size and j!=seq1_size):
        counter=matrix[i][j+1]  
        j+=1
        stockJ=matrix[0][j] #nouvel atome à appreiller
        stockI=matrix[i][0] #nouvel atome à appreiller
      else:
        counter=matrix[i+1][j]
        i+=1
        stockJ=matrix[0][j] #nouvel atome à appreiller
        stockI=matrix[i][0] #nouvel atome à appreiller
      preI=i
      preJ=j
    return pairs,matrix_color    

def matrix_score_r_l(matrix,ligne,colonne):
    #cette fonction permet de trouver la distance min entre un atome de seq 1 et un atome de seq 2
    #elle évite de choisir 2 fois le même atome
    matrix_color=copy.deepcopy(matrix)
    seq1_size=len(matrix[0])-1 #sequence la plus grande
    seq2_size=len(matrix)-1 #la plus petite
    pairs=[] #stocks les numeros des atomes de la paires et la distance min entre les 2
    stockJ=matrix[0][seq1_size] #nouvel atome à appreiller
    stockI=matrix[seq2_size][0]
    j=colonne
    i=ligne
    preI=i
    preJ=j
    counter=matrix[i][j] #pour comparer le min actuel aux autres distances
    count_tour=1
    while(i!=1 or j!=1):
      if(i!=1 and j!=1):
        counter=matrix[i-1][j-1] #réinitialise counter
        if(counter>matrix[i-1][j]): 
          counter=matrix[i-1][j] #nouveau min
          if(counter>matrix[i][j-1]):
            counter=matrix[i][j-1]  
            j-=1
            stockJ=matrix[0][j] #nouvel atome à appreiller
            stockI=matrix[i][0] #nouvel atome à appreiller
            count_tour=1
          else:
            i-=1
            stockJ=matrix[0][j] #nouvel atome à appreiller
            stockI=matrix[i][0] #nouvel atome à appreiller
            count_tour=1
        elif (counter>matrix[i][j-1]):
          counter=matrix[i][j-1]  
          j-=1
          stockJ=matrix[0][j] #nouvel atome à appreiller
          stockI=matrix[i][0] #nouvel atome à appreiller
          count_tour=1
        else:
          i-=1
          j-=1
          if(preI==i+1 and preJ==j+1 and count_tour==1):
              if(pairs!=[]):
                  last=pairs.pop()
                  matrix_color[last[3]][last[4]]=matrix[last[3]][last[4]]
              count_tour=0
              matrix_color[i+1][j+1]=-1
              pairs.append([stockI,stockJ,matrix[i+1][j+1],i+1,j+1]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
          stockJ=matrix[0][j] #nouvel atome à appreiller
          stockI=matrix[i][0] #nouvel atome à appreiller
          count_tour=0
          matrix_color[i][j]=-1
          pairs.append([stockI,stockJ,counter,i,j]) #ajoute les numeros des atomes de la paires et la distance min entre les 2
      elif(i==1 and j!=1):
        counter=matrix[i][j-1]  
        j-=1
        stockJ=matrix[0][j] #nouvel atome à appreiller
        stockI=matrix[i][0] #nouvel atome à appreiller
        count_tour=1
      else:
        counter=matrix[i-1][j]
        i-=1
        stockJ=matrix[0][j] #nouvel atome à appreiller
        stockI=matrix[i][0] #nouvel atome à appreiller
        count_tour=1
      preI=i
      preJ=j
    return pairs,matrix_color


def sum_distance (matrix):
    counter=0
    for i in range (0,len(matrix)):
        counter+=matrix[i][2]
    return counter 

def diag_long(matrix):
    counter=0
    max_counter=0
    for i in range (1,len(matrix)):
        if(matrix[i][3]-1==matrix[i-1][3] and matrix[i][4]-1==matrix[i-1][4]):
            counter+=1
        else:
            if(max_counter<counter):
                max_counter=counter
            counter=0
    return counter 
    
def best_pairs_l_r(matrix):
    seq1_size=len(matrix[0])-1
    seq2_size=len(matrix)-1 #la plus petite
    l1=[]
    bestPairs=[]
    color=[]
    bestColor=[]
    for i in range (seq2_size-seq2_size+1,seq2_size):
        for j in range (1,seq1_size):
            l1,color=matrix_score_l_r(matrix,i,j)
            #print(l1)
            if(len(l1)>len(bestPairs)):
                bestPairs=copy.deepcopy(l1)
                bestColor=copy.deepcopy(color)
            if(len(l1)==len(bestPairs)):
                if(diag_long(bestPairs)<diag_long(l1)):
                    bestPairs=copy.deepcopy(l1)
                    bestColor=copy.deepcopy(color)
                if(sum_distance(bestPairs)>sum_distance(l1) and diag_long(bestPairs)==diag_long(l1)):
                    bestPairs=copy.deepcopy(l1)
                    bestColor=copy.deepcopy(color)
    return bestPairs, bestColor

def best_pairs_r_l(matrix):
    seq1_size=len(matrix[0])-1
    seq2_size=len(matrix)-1 #la plus petite
    l1=[]
    bestPairs=[]
    color=[]
    bestColor=[]
    for i in range (seq2_size,1,-1):
        for j in range(seq1_size,0,-1):
            l1,color=matrix_score_r_l(matrix,i,j)
            #print(l1)
            if(len(l1)>len(bestPairs)):
                bestPairs=copy.deepcopy(l1)
                bestColor=copy.deepcopy(color)
            if(len(l1)==len(bestPairs)):
                if(diag_long(bestPairs)<diag_long(l1)):
                    bestPairs=copy.deepcopy(l1)
                    bestColor=copy.deepcopy(color)
                if(sum_distance(bestPairs)>sum_distance(l1) and diag_long(bestPairs)==diag_long(l1)):
                    bestPairs=copy.deepcopy(l1)
                    bestColor=copy.deepcopy(color)
    return bestPairs,bestColor
    
    
def write_csv(matrix_color):
    with open("matrix_to_compare.csv", "w") as file:
        writer=csv.writer(file)
        writer.writerows(matrix_color)
    file.close()
    
    
def rmsd(pdb1,pdb2,chaineA,chaineB):
    rmsd1=0
    rmsd2=0
    matrix_distance,matrix_square_distance,distance_count=mc.distance(pdb1,pdb2,chaineA,chaineB)
    #print(matrix_distance)
    matrix1,matrix_color1=best_pairs_l_r(matrix_distance)
    #print(matrix1)
    #print("rrrrrrrrrrrrrrrr")
    matrix2,matrix_color2=best_pairs_r_l(matrix_distance)
    #print(matrix)
    #if(matrix1==matrix2[::-1] ): #si la lecture des 2 matrices renvoie les memes paires
    for i in range(0,len(matrix1)):
        rmsd1+=(matrix_square_distance[matrix1[i][3]][matrix1[i][4]])
    rmsd1=math.sqrt(rmsd1/len(matrix1))
    for i in range(0,len(matrix2)):
        rmsd2+=(matrix_square_distance[matrix2[i][3]][matrix2[i][4]])
    rmsd2=math.sqrt(rmsd2/len(matrix2))
    return min(rmsd1,rmsd2)


def main():
    #matrix=[['x',11,12,13,14,15,16],[21,2,0,2,2,2,2],[22,3,1,2,0,2,2],[23,2,2,0,1,2,2],[24,2,0,2,2,2,2]]
    #matrix1=[['x',11,12,13,14,15,16],[21,0,2,2,2,2,2],[22,3,0,2,2,2,2],[23,2,2,0,1,2,2],[24,2,2,2,0,2,2]]
    pdb1 = "C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\3trx.pdb"
    pdb2="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\3trx vs 1xwc\\dalitan\\sup1xwc.pdb"
    pdb3="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\Essai2.pdb"
    pdb4="C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Dalilite\\3fts_3fh7\\sup2.pdb"
    print(rmsd(pdb1,pdb2,"A","A"))
    
   # print(r.lire_pdb("C:\\Users\\tanvi\\Documents\\EIDD\\Projet_transverse\\Fichier_pdb\\1b38.pdb"))
   # print(min_distance_complexe(matrix))
    
main()
