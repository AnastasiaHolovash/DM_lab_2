import random

def a_father_b(A, B, mens, women):
    paset = set()
    for i in A:
        if i in mens:
            paset.add(i)
    childset = set(B)
    S = []
    for i in range(min(len(paset), len(childset))):
        m = random.choice(list(paset))
        w = random.choice(list(childset))
        S.append([m, w])
        paset.remove(m)
        childset.remove(w)
    return S


def a_father_in_law_b(A, B, mens):
    mensetA = set()
    for i in A:
        if i in mens:
            mensetA.add(i)
    mensetB = set()
    for i in B:
        if i in mens:
            mensetB.add(i)
    R = []
    for i in range(min(len(mensetA), len(mensetB))):
        m1 = random.choice(list(mensetA))
        m2 = random.choice(list(mensetB))
        if m1 != m2:
            R.append([m1, m2])
        mensetA.remove(m1)
        mensetB.remove(m2)
    return R


def a_universal_father_in_law_b(A, B, mens):
    mensetA = set()
    for i in A:
        if i in mens:
            mensetA.add(i)
    mensetB = set()
    for i in B:
        if i in mens:
            mensetB.add(i)
    Ur = []
    for m1 in mensetA:
        for m2 in mensetB:
            if m1 != m2:
                Ur.append([m1, m2])
    return Ur

def unionn(s, r):
    U = []
    for i in s:
        U.append(i)
    for i in r:
        if i not in U:
            U.append(i)
    return U

def intersectionn(s, r):
    I = []
    for i in s:
        if i in r:
            I.append(i)
    return I

def differ(r, s):
    D = []
    for i in r:
        if i not in s:
            D.append(i)
    return D

def transposed(s):
    T = []
    for i in range(len(s)):
        T.append([s[i][1], s[i][0]])
    return T

