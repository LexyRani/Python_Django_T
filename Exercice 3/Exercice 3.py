def show_menu(plats):
    for nom, prix, dispo in plats.values():
        if dispo:
         print(f"{nom.lower()} - {prix}€")

def main():
    menu = {
        "entrées":{1: ("Salade César", 8, True),
                   2: ("Soupe du jour",6, False)},
        "plats":{1: ("Steak frites", 15, True),
             2: ("Poisson grillé", 14, True),
             3: ("Plat du chef", 18, False)},
        "dessert": {1: ("Tiramisu", 7, True),
            2: ("Glace", 5, True),
            3: ("Dessert mystère", 9, False)}
        }

    for i, (categorie, plats) in enumerate(menu.items()):
        if i > 0:
            print()
        print(f"--- {categorie} ---")
        show_menu(plats)

if __name__ == "__main__":
    main()
