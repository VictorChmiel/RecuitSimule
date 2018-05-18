# Pb des n-reines
import random as rd
import math

import numpy as np


def echinit(n):
     E=np.zeros((n,n))
     for i in range(n):
         E[i][rd.randint(0,n-1)]=1
     return E


def posreines(m):
    pos=[]
    for i in range (np.size(m[0])):
        for j in range(np.size(m[0])):
            if m[i][j]==1:
                pos.append((i,j))
    return pos


def reglecol(m):
    n = np.size(m[0])
    c = 0
    for e in posreines(m) :
        # collisions sur la ligne
        for i in range (n):
            if i != e[0] and m[i,e[1]] == 1:
                c +=1
        # collisions sur la colonne
        for j in range(n):
            if j != e[1] and m[e[0], j] == 1:
                c += 1
        # collisions sur la diagonale descendante
        i = e[0] -1
        j = e[1] -1
        while i>=0 and j>=0 :
            if m[i,j] == 1 :
                c +=1
            i -=1
            j-=1

        i = e[0] + 1
        j = e[1] + 1
        while i < n and j < n:
            if m[i, j] == 1:
                c += 1
            i += 1
            j += 1
        # collisions sur la diagonale descendante
        i = e[0] - 1
        j = e[1] + 1
        while i >= 0 and j < n:
            if m[i, j] == 1:
                c += 1
            i -= 1
            j += 1

        i = e[0] + 1
        j = e[1] - 1
        while i < n and j >=0:
            if m[i, j] == 1:
                c += 1
            i += 1
            j -= 1
    return c


def echangeLigne(m, i, j):
    temp = np.copy(m[i])
    m[i] = m[j]
    m[j] = temp
    return 0


def echangeColonne(m, i, j):
    temp = np.copy(m[:,i])
    m[:,i] = m[:,j]
    m[:,j] = temp
    return 0

def suivant(m):
    m2=np.copy(m)
    n= np.size(m2[0])
    b=rd.randint(0,1)
    if b == 0:
        i = rd.randint(0,n-1)
        j = rd.randint(0,n-1)
        echangeLigne(m2,i,j)

    if b == 1:
        i = rd.randint(0, n - 1)
        j = rd.randint(0, n - 1)
        echangeColonne(m2,i,j)
    return m2

def suivant2(m):
    m2=np.copy(m)
    n= np.size(m2[0])
    l=posreines(m2)
    nl=np.size(l)
    queen = l[rd.randint(0,(nl-1)//2)]
    i=queen[0]
    j=queen[1]
    r=rd.randint(0,n-1)
    m2[r,j]=1
    m2[i,j]=0
    return m2

def main(n, tlimite):

    etat_actuel= echinit(n)
    for t in range(tlimite):
        if t%1000 == 0:
            print(t)
        suiv = suivant2(etat_actuel)
        delta = reglecol(suiv) - reglecol(etat_actuel)
        if delta < 0:
            etat_actuel=suiv
        else:
            if(rd.random()<math.exp(-delta*t)):
                etat_actuel=suiv
    print(etat_actuel)
    print(reglecol(etat_actuel))

    return 0

main(8,43320)














     



