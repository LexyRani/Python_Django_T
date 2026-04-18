MAX_WIDTH = 100

def format_ligne(texte):
    longueur = min(len(texte), MAX_WIDTH - 2)
    return f"|{' ' * (MAX_WIDTH - longueur - 2)}{texte[:longueur].lower()}|"

def display_bloc(bloc):
    for texte, visible in bloc.values():
        if visible:
            print(format_ligne(texte))

def main():
    dico = {
        "bloc1":{1: ("Le code propre facilite la maintenance", True)},
        "bloc2":{1: ("Tester souvent évite beaucoup d erreurs", True),
             2: ("Cette phrase ne doit pas s afficher", False)},
        "bloc3": {1: ("Cette phrase ne doit pas s afficher", True),
            2: ("Un bon code doit rester simple et clair", False),
            3: ("La simplicité améliore la qualité du code", True),
            4: ("Refactoriser améliore la compréhension", True)}
    }

    for element in dico.values():
        print("-" * MAX_WIDTH)
        display_bloc(element)
        print("-" * MAX_WIDTH)

if __name__ == "__main__":
    if MAX_WIDTH < 2:
        print("Error: Your MAX_WIDTH has to be more than 2")
        exit()
    main()
