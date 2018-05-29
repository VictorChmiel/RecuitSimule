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


def n_coll(m, n):
    s = 0
    for e in pos_queens(m, n):
        collision = False
        # collisions sur la ligne
        for i in range (n):
            if i != e[0] and m[i,e[1]] == 1:
                collision = True
        # collisions sur la colonne
        for j in range(n):
            if j != e[1] and m[e[0], j] == 1:
                collision = True
        # collisions sur la diagonale descendante
        i = e[0] - 1
        j = e[1] - 1
        while i>=0 and j>=0 :
            if m[i,j] == 1 :
                collision = True
            i -=1
            j-=1

        i = e[0] + 1
        j = e[1] + 1
        while i < n and j < n:
            if m[i, j] == 1:
                collision = True
            i += 1
            j += 1
        # collisions sur la diagonale descendante
        i = e[0] - 1
        j = e[1] + 1
        while i >= 0 and j < n:
            if m[i, j] == 1:
                collision = True
            i -= 1
            j += 1

        i = e[0] + 1
        j = e[1] - 1
        while i < n and j >=0:
            if m[i, j] == 1:
                collision = True
            i += 1
            j -= 1
        if collision:
            s += 1
    return s



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
    print("nombre de collisions = "+ str(n_coll(etat_actuel, n)))
    return n_coll(etat_actuel, n)


n_tot = 1000
moy = 0
nzero = 0
for k in range(n_tot):
    print(k)
    n_collision = recuit_simule(100, 11)
    moy += n_collision
    if n_collision == 0 :
        nzero += 1

print("nombre de collisions final en moyenne :" + str(moy/n_tot) + "  et " + str(nzero) + " résultats optimaux sur " + str(n_tot) + " simulations")


# 8 reines

# 10000 simulations

# T = 100
# nombre de collisions final en moyenne :4.352  et 6 résultats optimaux sur 1000 simulations

# T = 1000
# nombre de collisions final en moyenne :3.922  et 16 résultats optimaux sur 1000 simulations

# 1000 simulations

# 10 reines

# T = 100
# nombre de collisions final en moyenne :5.779  et 2 résultats optimaux sur 1000 simulations

# T = 1000
# nombre de collisions final en moyenne :4.829  et 8 résultats optimaux sur 1000 simulations

# Recherche du n maximal solvable pour T = 100 et 1000 simulations

# nombre de collisions final en moyenne :6.562  et 1 résultats optimaux sur 1000 simulations

