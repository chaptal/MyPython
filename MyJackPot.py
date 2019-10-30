#JACKPOT SIMULATION ET BECOME BILLIARD PERSON
#GET WHAT YOU NEED AND MAKE YOUR DREAM POSSIBLE
#Le 22/07/2018 Par Oscar KALONJI
#Mise à jour Séparation de chiffre comme string afin de le recuperer 27/08/2018

#--------------------------------++++++++++++-------------------------------
L = ["1","2","3","4","5","6","7","8","9","10","11"]
N = 5
G = []

def factorielle(x):
    if x < 2:
        return 1
    else:
        return x * factorielle(x - 1)

def combinaisons(L, N, k):
    h = 0
    i = 0
    j = 0

    n = [0] * (N - 1)#ça veut dire?

    G = []
    s = ""

    if len(L) < N:
        return G
    elif N == 1:
        return L
    elif len(L) == N:
        while i < len(L):
            s = s + L[i]
            i = i + 1

        G.append(s)
    elif len(L) > N:
        l = factorielle(len(L) - 1)/(factorielle(N - 1)
             * factorielle((len(L) - 1) - (N - 1)));

        while i < l:
            s = L[len(L) - 1]+ ','

            while h < len(n):
                if j > 0 and j < len(n):
                    n[j] = n[j - 1] + 1

                s = s + L[n[h]]+ ','
                h = h + 1
                j = j + 1

            G.append(s)

            h = 0
            j = 0

            while j < len(n) and n[j] != j + k:
                j = j + 1

            if j > 0:
                n[j - 1] = n[j - 1] + 1

            i = i + 1

        L.pop()
        G = G + combinaisons(L, N, k - 1)

    return G
G = combinaisons(L, N, len(L) - N)
print(G)
