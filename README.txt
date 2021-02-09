Projet comptabot.

Le projet :

Version Simple : 

Celui-ci ce veut être un outils que peut utiliser n'importe qui pour faire sa comptabilités.
En premier temps il sera destinés au gérant de SCI famillial.

Le projet tournera sous une base mongodb pour le stockage des saisies, et idealement l'image du document.
Le projet necessitera un traitement, l'assignation des saisies clients devront etre convertie par rapport a un plan comptable general.

Pour cela une reconaissance des termes utilisés sera necessaire,

Version complexe : 

Idealement a terme, une reconaissance d'image idealement pour une affectation par rapport au terme directe.


Bonus : 

Un tchatbot qui ira scrappe les sites officiels pour obtenir une reponse plus rapidement.


Le projet est libre de droit, sur la base participative.

Avenant 26/05/2020 : 

Les fonctions suivantes serront mis en avant : 

- Tchatbot :
    qui présente des données sommaire (MONGODB), 
    qui suggère un compte comptable ( données PCG),
    Gestionnaire de sentiments (reconaissance de terme smiley),
    
    Bonus :
        analyse de la phrase (sentiment FR)
        qui repond au question courante fiscale et social (Scraping)
    Facultatif :
        fonction de mise a jours du PCG, avec implementation directe, enrichissement
        fonction d'utilisation d'un PCG personnalisé



Fonctions : 

Présentation des fonctions attendu et mis en attente: 
    - Compte de résultat (AC - VT)
    - Bilan (en attente, integration des OD)
fonction clé :
    - Comptabilisation ! : Match toutes les écritures de la base de données pour l'établissement des comptes et des bilans de manière comptable.
    - Sortie d'un compte de resultat simplifié
    - Sortie d'un bilan simplifié

Fonctions should :
    - Reconaissance d'image partiel
    - Gestion et cloture des exercices
    - sugestion en directe sur PCG utilise par rapport a l'objet saisie.
