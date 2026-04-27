L1 = [1,2,3]
L2 = [4,5,6]
L3 = []
for i in range(len(L1)):
    ligne = []
    for j in range(len(L2)):
        ligne.append(L1[i] * L2[j])
    L3.append(ligne)
print(L3)