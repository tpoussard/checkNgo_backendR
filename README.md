# Projet fil rouge - Check&Go

## Description du projet :
Il s'agit de réaliser une application web de vérification du contenu de son sac de voyage. Cette application doit être accessible via un site web et via mobile en déconnecté. Le développement en mode itératif se décline en 4 premières versions:  

**V1 :** L'application propose une check liste permettant de vérifier que l'on a tout pristout ce qui est nécessaire pour son voyage. L'utilisateur peut alors "cocher"  ce qu'il a déjà pris et voir ce qui lui manque.
V1.+.+:
=> liste divisée en categories
=> login In / log Out

**V2 :** L'utilisateur peut proposer de nouveaux items qui seront validés par un administrateur. Il peut également modifier la liste pour son propre besoin.

**V3 :** L'application pose à l'utilisateur quelques (2 ou 3) question pour limiter la check liste à ce qui semble nécessaire. Ex : Allez-vous à l'étranger ? Y a t'il des moustiques là ou vous allez ? ...

**V4 :** D'autres check list peuvent être rajoutées comme:
* une liste de course ou
* une liste pour préparer une rando pédestre ou cycle
* une liste des choses à faire pour un mariage
...
## Installation
Ouvrir un terminal, se placer dans le dossier de destination et initialiser un dépot git :  
` git init `  
Cloner le projet :  
` git clone git@github.com:tpoussard/checkNgo_backend_djangoR.git `  
Se placer dans le dossier :  
` cd checkNgo_backend_djangoR/ `  
Créer un environnement virtuel pour installer les dépendances propres au projet de façon isolée :  
`virtualenv -p python3 venv`  et l'activer : `source venv/bin/activate`  
Se placer dans le dossier principal du projet:  
`cd checkngo/`  
Créer un superutilisateur pour avoir accès au fonctionnalités d'administration :  
`python manage.py createsuperuser`  
Lancer le serveur local et suivre le lien depuis le terminal pour accéder à l'interface administrateur:  
`python manage.py runserver`
## Modification du modèle de base de données
Supprimer la base de données déjà présentes 
Initialiser la base de données :
`python manage.py migrate`,  
puis recréer un superutilisateur comme indiqué précédemment.  
Si les models ont été modifiés, lancer la commande :  
`python manage.py makemigrations`  
