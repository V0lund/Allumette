"""

########################################################################################################################
#######################################--Le jeu des allumettes--########################################################
########################################################################################################################

Le jeu des allumettes 1
Programmez le jeu des allumettes.
    Le jeu doit:
        * être jouable à deux joueurs humains. Il demandera le nom des deux joueurs;
        * choisira au hasard un des deux joueurs;
        * afficher le nombre d’allumettes restantes (au début, 20);
        * vérifier que le joueur ne tire qu’une à trois allumettes;
        * s’arrête quand un joueur a tiré la dernière allumette;
        * afficher un message indiquant quel joueur a perdu.

Le jeu des allumettes 2
Modifiez le "jeu des allumettes 1" pour lui ajouter les fonctionnalités suivantes :
    * Le jeu peut maintenant être joué seul contre l’ordinateur ou à deux joueurs.
    * Le joueur indiquera le mode de jeu (seul/ deux joueurs).
    * En cas de jeu contre l’ordinateur, programmez une intelligence artificielle qui choisira au hasard
      une à trois allumettes lors de son tour de jeu.

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
    print("Pour jouer contre un autre jouer humain appuyez sur 1. "
          "Pour jouer contre l'ordinateur, appuyez sur 2.")


def allum():
    """
    Aucun input/output. Procédure pour afficher le nombre d'allumettes.
    """
    print(n_all)
    for i in range(n_all):
        print(u'\u00b6', end=" ")
    print('\n')


def choice_hu() -> str:
    """
    Procedure pour verification le choix du joueur.
    :return: a comme str
    """
    a = ""
    while not (a == "1" or a == "2"):
        a = input("Votre choix:")
    return a


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


def ordo_s():
    from random import randint
    a = 0
    if n_all >= 4:  # évaluer le choix du joueur relatif a le numéro d'allumettes.
        a = randint(1, 3)
    elif n_all == 3:
        a = randint(1, 2)
    else:
        a = 1
    return a
    pass


def plval(a) -> int:
    """
    Verifier si la valeur introduit par le joueur est correcte.
    param a: l'input c'est un entier.
    :rtype: integer
    """
    if n_all >= 4:              # évaluer le choix du joueur relatif a le numéro d'allumettes.
        while not(a == '1' or a == '2' or a == '3'):
            a = input('Choisissez une valeur entre 1 et 3. - ')
    elif n_all == 3:
        while not (a == '1' or a == '2'):
            a = input('Choisissez une valeur entre 1 et 2. - ')
    elif n_all == 2:
        while not (a == '1'):
            a = input('Le 1 c\'est la seule valeur possible. - ')
    elif n_all == 1:
        a = '1'
    return int(a)


if __name__ == '__main__':
    player1 = " "
    player2 = " "
    n_all = 20
    menu()
    ch = choice_hu()
    if ch == "1":
        print("Vous-avez choisi un jeu 1 vs 1.")
        player1 = input('Le nom du 1er joueur est: ')
        player2 = input('Le nom du 2eme joueur est: ')
        firstpl()
        if firstpl() == 2:  # Si la function retour 2: player1, player2 == player2, player1
            temp = player1
            player1 = player2
            player2 = temp
        print(f'Le jouer {player1} est le premier!')
        print()
        allum()

        plc1r = 0                                   # variables pour compter les nombres des a. restant pour le autre j.
        plc2r = 0

        while n_all > 1:                            # loop pour jouer jusqu'à la dernière allumette.
            plc1 = 0                                # var pour retenir le choix
            plc2 = 0
            print(f'{player1} choix: ')
            plc1 = plval(plc1)
            n_all = n_all - plc1
            plc2r = n_all
            allum()
            print(f'On rest {n_all} allumette.')

            print(f'{player2} choix: ')
            plc2 = plval(plc2)
            n_all = n_all - plc2
            plc1r = n_all
            allum()
            print(f'On rest {n_all} allumette.')

        if plc2r == 1:
            allum()
            print(f'{player2} a perdu!.')
        else:
            allum()
            print(f'{player1} a perdu!.')

    else:
        print("Vous-avez choisissez de joueur vers l'ordinateur.")
        player1 = "PC"
        player2 = input("Votre nom est? - ")
        firstpl()

        if firstpl() == 2:  # Si la function retour 2: player1, player2 == player2, player1
            temp = player1
            player1 = player2
            player2 = temp

        print(f'Le jouer {player1} est le premier!')
        print()
        allum()

        plc1r = 0
        plc2r = 0

        while n_all > 1:  # loop pour jouer jusqu'à la dernière allumette.
            pl1c = 0
            pc = 0

            print(f'{player1} choix: ')
            pl1c = plval(pl1c)
            n_all = n_all - pl1c
            plc2r = n_all
            allum()
            print(f'On rest {n_all} allumette.')

            print(f'PC choix -  ')
            pc = ordo_s()
            n_all = n_all - pc
            plc1r = n_all
            allum()
            print(f'On rest {n_all} allumette.')

        if plc2r == 1:
            allum()
            print(f'{player2} a perdu!.')
        else:
            allum()
            print(f'{player1} a perdu!.')
