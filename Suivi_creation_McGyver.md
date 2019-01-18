# Choix

- **choix 1:** Découper un tuile de sol du fichier floor-tiles pour avoir un pavage uniforme 15 x 15 cubes de 20 pixels 
de coté.
- **choix 2:** Création d'un mur autour du plateu de jeux pour contenir le joueur sur la surface de jeu.
- **choix 3:** Générer aléatoirement le labyrinthe à chaque lancement du jeu (emplacement des obstacles). 

* **Difficultés:**
    - trouver comment faire rester le personnage dans l'aire de jeu (= écran)
    - trouver comment gérer les collisions avec les obstacles
    - création de boucle pour 2 variables x, y. for x in ... and y in ... (refus du y)  ==> décomposition en 2 boucles for successives
    - disposition aléatoire de blocks sur le plateau à l'initiation du jeu ==> utilisation de la fonction random.sample()
    - compréhension de la fonction .blit() ==> fusionne une image source vers une image/surface destination. Donc utilisé avec
    image.rect(), elle fusionne image avec la surface carrée issue d'elle.
    - pour les déplacements, trouver comment gérer le réaffichage de l'arrière plan sans régénérer le plateau entier (donc avec modification
    du parcours !)  ==> utilisation de la fonction pygame.Surface.copy qui crée une copie de la surface, que j'ai stocké
    dans une variable gloabale que j'ai rendu modifiable par la fonction qui génère les obstacles.
    - compréhension de la gestion des obstacles: difficultés à gérer la double condition pour autoriser les déplacements
    ==> essai-erreurs et coller à l'instruction et non à ce que je voudrais que le programme fasse !
    - positionnement aléatoire des objets sur le plateau ==> en cours

* **Découvertes en chemin:**
    - nécessité de préparer le plateau de jeu AVANT de lancer l'affichage car "piégé" dans boucle while
    => affichage avec while ne sert que pour gérer les interactions avec l'utilisateur (personnage, décision)
    => affichage initié par la commande pygame.display.set_mode()
    => la possibilité de créer des capture d'écran (!) via la fonction pygame.surface.copy
    => nécessité de dissocier le rectangle du personnage qui se déplace de l'image qui va lui être associé pour la
    représentation à l'écran. Pour les mouvements il faut s'occuper d'un seul rectangle qu'on va faire bouger et updater
    la position d'un appui d'une touche à une autre.

* **Audio**:

    - Musique d'ambiance composée par [K-Alpha](soundcloud.com/k-alpha)
    - Bibliothèque sonore de [Joseph SARDIN](https://lasonotheque.org)