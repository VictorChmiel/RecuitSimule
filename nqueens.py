import numpy as np
import random as rd
from math import exp


def etat_initial(n):
    E = np.zeros((n, n))
    for i in range(n):
        E[i][rd.randint(0, n - 1)] = 1
    return E


def pos_queens(m,n):
    pos=[]
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                pos.append((i, j))
    return pos


def cout(m, n):
    c = 0
    for e in pos_queens(m, n):
        # collisions sur la ligne
        for i in range (n):
            if i != e[0] and m[i,e[1]] == 1:
                c +=1
        # collisions sur la colonne
        for j in range(n):
            if j != e[1] and m[e[0], j] == 1:
                c += 1
        # collisions sur la diagonale descendante
        i = e[0] - 1
        j = e[1] - 1
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


def voisin(etat,n):
    vois = np.copy(etat)
    i = rd.randint(0,n-1)
    if vois[i][0] == 1 :
        vois[i][0] = 0
        vois[i][1] = 1
    elif vois[i][n - 1] == 1 :
        vois[i][n - 1] == 0
        vois[i][n - 2] == 1
    else :
        pos = -1
        for k in range(n):
            if vois[i][k] == 1 :
                pos = k
        if rd.randint(0,1):
            vois[i][pos] = 0
            vois[i][pos - 1] = 1
        else :
            vois[i][pos] = 0
            vois[i][pos + 1] = 1



    return vois

def recuit_simule(tlimite,n):
    etat_actuel = etat_initial(n)
    t = 1;
    while t <= tlimite:
        suivant = voisin(etat_actuel, n)
        delta = cout(suivant, n) - cout(etat_actuel, n)
        if (delta < 0):
            etat_actuel = suivant
        else:
            if (rd.random()<= exp(-delta*t)):
                etat_actuel=suivant
        t = t+1
    print(etat_actuel)
    print("cout = "+ str(cout(etat_actuel, n)))
    return cout(etat_actuel)


moy = 0
for k in range(100):
    print(k)
    moy += recuit_simule(100000, 8)
print("cout final moyen :" + str(moy/100))


