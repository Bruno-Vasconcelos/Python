def quicksort(V):
    quicksort2(V, 0, len(V) - 1)


def quicksort2(V, menor, maior):
    if menor < maior:
        p = particao(V, menor, maior)
        quicksort2(V, menor, p - 1)
        quicksort2(V, p + 1, maior)


def achapivo(V, menor, maior):
    meio = (maior + menor) // 2
    pivo = maior
    if V[menor] < V[meio]:
        pivo = meio

    elif V[menor] < V[maior]:
        pivo = menor

    return pivo


def particao(V, menor, maior):
    indicepivo = achapivo(V, menor, maior)
    valorpivo = V[indicepivo]
    V[indicepivo], V[menor] = V[menor], V[indicepivo]
    borda = menor

    for i in range(menor, maior + 1):
        if V[i] < valorpivo:
            borda += 1
            V[i], V[borda] = V[borda], V[i];
    V[menor], V[borda] = V[borda], V[menor]

    return borda


V = [5, 2, 4, 5, 2, 1, 6, 8, 5, 34, 2, 3, 5, 7]

print("Vetor:", V)
quicksort(V)
print("Ordenado:", V)
