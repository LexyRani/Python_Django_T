MAX_WIDTH = 100

def add_space(bloc):
    for tup in bloc.values():
        lenStr = min(len(tup[0]), MAX_WIDTH - 2)
        if tup[1] == True:
            print(f"|{' ' * (MAX_WIDTH - lenStr - 2)}{tup[0][:lenStr].lower()}|")

def main():
    bloc1 = {1: ("Le code propre facilite la maintenance", True)}
    bloc2 = {1: ("Tester souvent évite beaucoup d erreurs", True),
             2: ("Cette phrase ne doit pas s afficher", False)}
    bloc3 = {1: ("Cette phrase ne doit pas s afficher", True),
            2: ("Un bon code doit rester simple et clair", False),
            3: ("La simplicité améliore la qualité du code", True),
            4: ("Refactoriser améliore la compréhension", True)}
    dico = [bloc1,
            bloc2,
            bloc3]

    for element in dico:
        print("-" * MAX_WIDTH)
        add_space(element)
        print("-" * MAX_WIDTH)

if __name__ == "__main__":
    if MAX_WIDTH < 2:
        print("Error: Your MAX_WIDTH has to be more than 2")
        exit()
    main()
