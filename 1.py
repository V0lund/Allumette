"""
########################################################################################################################
#######################################--Le jeu des allumettes 1--#####################################################
########################################################################################################################

Programmez le jeu des allumettes.
    Le jeu doit:
        * être jouable à deux joueurs humains. Il demandera le nom des deux joueurs;
        * choisira au hasard un des deux joueurs;
        * afficher le nombre d’allumettes restantes (au début, 20);
        * vérifier que le joueur ne tire qu’une à trois allumettes;
        * s’arrête quand un joueur a tiré la dernière allumette;
        * afficher un message indiquant quel joueur a perdu.
"""


def menu():
    """
    Aucun input/output. La fonction informe le joueur sur les règles du jeu.
    """
    print()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("**************************************** JEU D'ALLUMETTES**************************************************")
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("Le jeu des allumettes se joue à deux joueurs. Le principe est simple: 20 allumettes sont alignées. Chaque "
          "joueur a le droit de tirer 1, 2 ou 3 allumettes à la fois. Celui qui tire la dernière allumette a perdu.")
    print("Quelles sont les noms de les deux joueurs?")


def allum():
    """
    Aucun input/output. Procédure pour afficher le nombre d'allumettes.
    """
    for i in range(n_all):
        print(u'\u00b6', end=" ")
    print('\n')


def firstpl() -> int:
    """
    Procédure pour choisir le premier joueur.
    La fonction prendre aucune input mais return 1 si le gagneur et le 1er joueur ou 2 pour le 2eme.
    """
    import random  # La methode 'random' est utilise pour choisir un numero, entre 1 et 99 pour chaque jouer.
    p1 = 0
    p2 = 0
    while p1 == p2:
        p1 = random.randint(1, 99)
        p2 = random.randint(1, 99)
    if p2 > p1:
        return 2
    else:
        return 1


def plval(a) -> int:
    """
    Verifier si la valeur introduit par le joueur est correcte.
    param a: l'input c'est un entier.
    :rtype: integer
    """

    if n_all >= 4:              # évaluer le choix du joueur relatif a le numéro d'allumettes.
        while not(1 <= a <= 3):
            a = int(input('Choisissez une valeur entre 1 et 3. - '))
            a = a
    elif n_all == 3:
        while not (1 <= a <= 2):
            a = int(print('Choisissez une valeur entre 1 et 2. - '))
            a = a
    elif n_all == 2:
        while a != 1:
            a = int(input('Le 1 c\'est la seule valeur possible. - '))
            a = a
    elif n_all == 1:
        a = 1
    return a


if __name__ == '__main__':
    n_all = 20
    menu()
    player1 = input('Nom de 1er joueur: ')
    player2 = input('Nom de 2eme joueur: ')
    print()
    allum()
    if firstpl() == 2:  # Si la function retour 2: player1, player2 == player2, player1
        temp = player1
        player1 = player2
        player2 = temp
    print(f'Le jouer {player1} est le premier!')
    print()

    while n_all > 1:  # loop qui permettra de jouer le jeu jusqu'a la dernière allumette.
        plc1 = 0
        plc2 = 0
        if n_all - plc1 > 1:
            print(f'{player1} choix: ')
            plc1 = plval(plc1)
            n_all = n_all - plc1
            allum()
            print(f'On rest {n_all} allumette.')
        elif n_all - plc1 == 1:
            allum()
            print(f'{player1} a perdu!.')

        if n_all - plc2 > 1:
            print(f'{player2} choix: ')
            plc2 = plval(plc2)
            n_all = n_all - plc2
            allum()
            print(f'On rest {n_all} allumette.')
        elif n_all - plc2 == 1:
            allum()
            print(f'{player2} a perdu!.')
