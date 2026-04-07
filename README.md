# Gestion de produits et facturation (Python / Django)

Ici vous trouverez:
- un script Python de manipulation de texte en console (exercice 1) ;
- une application web Django de gestion de produits et de facturation (exercice 2).

L’objectif est de montrer à la fois de la logique Python côté console et une application web structurée avec Django.

---

## Sommaire

- [Exercice 1 — Blocs de texte en console](#exercice-1--blocs-de-texte-en-console)
- [Exercice 2 — Application Django de gestion de produits et factures](#exercice-2--application-django-de-gestion-de-produits-et-factures)
  - [Installation](#installation)

---

## Exercice 1 – Blocs de texte en console

### Description

Un script Python qui affiche dans la console plusieurs blocs de texte encadrés, avec :

- une largeur maximale configurable (par défaut 100 caractères) ;
- tout le texte en minuscules ;
- des bordures `-` pour le haut/bas et `|` pour les côtés ;
- des blocs pouvant contenir une ou plusieurs lignes.

Les phrases sont stockées dans un dictionnaire, ce qui permet :
- de modifier facilement le texte ;
- de changer l’ordre d’affichage des blocs ;
- d’ajouter ou supprimer des lignes ;
- de garder certaines phrases dans le dictionnaire sans les afficher.

Certaines phrases présentes dans les données sont volontairement exclues de l’affichage final, même si elles sont définies dans le dictionnaire.


### Lancer le script

Depuis la racine du projet :

```bash
cd Exercice/ 1
python Exercice\ 1.py
```

---

## Exercice 2 – Application Django de gestion de produits et factures

### Description

Application web Django qui permet de :

- gérer un catalogue de produits ;
- créer des factures avec plusieurs produits et des quantités ;
- consulter le détail d’une facture avec total de produits et total à payer ;
- naviguer dans les listes via la pagination.


### Fonctionnalités principales

#### Gestion des produits

- Créer un produit
- Modifier un produit
- Supprimer un produit
- Afficher la liste des produits (avec pagination)

#### Facturation

- Créer une facture
- Sélectionner des produits pour la facture
- Définir la quantité de chaque produit
- Afficher le détail d’une facture :
  - liste des produits de la facture
  - nombre total de produits
  - total à payer

---

## Installation

### Prérequis

- Python 3.x
- `pip`
- `venv`

### Étapes

1. Cloner le dépôt :

```bash
git clone https://github.com/LexyRani/Python_Django_T.git
cd Python_Django_T
```

2. Créer et activer un environnement virtuel :

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
# ou
venv\Scripts\activate         # Windows
```

3. Installer les dépendances :

```bash
pip install django
```

4. Appliquer les migrations:

```bash
cd Exercice\ 2/WebAppDjango
python manage.py migrate
```

5. Lancer le serveur de développement :

```bash
python manage.py runserver
```

Depuis le dossier du projet Django (là où se trouve `manage.py`) :

  1. Lancer le serveur :

  ```bash
  python manage.py runserver
  ```

  2. Depuis un navigateur web, accéder à l’application :
     - `http://127.0.0.1:8000/`
