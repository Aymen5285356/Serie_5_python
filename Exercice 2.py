L = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
somme = 0
for sous_liste in L:
    for nombre in sous_liste:
        somme += nombre
print(somme)