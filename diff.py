from colorama import Fore, Style

def longest_common_subsequence(chaine1: str, chaine2: str) -> str:
    "renvoie la plus longue sous chaine commune à chaine1 et chaine2"
    n = len(chaine1)
    m = len(chaine2)

    matrice_dyna = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if chaine1[i - 1] == chaine2[j - 1]:
                matrice_dyna[i][j] = matrice_dyna[i - 1][j - 1] + 1
            else:
                matrice_dyna[i][j] = max(matrice_dyna[i - 1][j], matrice_dyna[i][j - 1])

    #reconstruction de la plus grande sous-chaine commune
    i = n
    j = m
    resultat = ""
    while i > 0 and j  >0 :
        if chaine1[i-1] == chaine2[j-1]:
            resultat = chaine1[i-1] + resultat
            i -= 1
            j -= 1
        elif matrice_dyna[i - 1][j] > matrice_dyna[i][j - 1]:
            i -= 1
        else:
            j -=1
    return resultat

if __name__ == "__main__":
    with open("textA.txt", "r") as fichier:
        textA = fichier.read()

    with open("textB.txt", "r") as fichier1:
        textB = fichier1.read()

    #initialisation compteur de lignes textA et textB        
    line_a = 0
    line_b = 0

    #obtention de la plus longue sous chaine commune entre les deux fichiers textA et textB
    lcs = longest_common_subsequence(textA, textB)
    
    #décompositon des deux fichiers textA et textB en lignes
    trucA = textA.split('\n')
    trucB = textB.split('\n')

    # Parcours de la plus longue sous chaine commune
    for line in lcs.split('\n'):
        # Tant que c'est une ligne du textA qui n'est plus commune
        # C'est une suppression 
        while trucA[line_a] != line:
                print(f"{Fore.RED}- {trucA[line_a]} {Style.RESET_ALL}")
                line_a +=1

        # Tant que c'est une ligne du textB qui n'est plus commune
        # C'est une insertion
        while trucB[line_b] != line:
                print(f"{Fore.GREEN} + {trucB[line_b]} {Style.RESET_ALL}")
                line_b +=1
        # Si les deux lignes sont communes aucune modification on l'affiche en blanc
        if trucA[line_a] == trucB[line_b]:
            print(f"  {trucA[line_a]}")
            line_a += 1
            line_b += 1

# On affiche les lignes restantes de textA dans le cas ou il en resterait
while line_a < len(trucA):    
    print(f"{Fore.GREEN} - {trucA[line_a]} {Style.RESET_ALL}")
    line_a += 1

# On affiche les lignes restantes de textB dans le cas ou il en resterait
while line_b < len(trucB):  
    print(f"{Fore.GREEN}+ {trucB[line_b]} {Style.RESET_ALL}")
    line_b += 1
