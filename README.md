# flight_price
Site permettant de savoir quel est le moment le plus intéressant pour acheter son billet d'avion.  

Cette application réalisé à l'aide de framework **'Flask'** et est encapsulé dans un container qui est relier à une base de données **'MongoDB'**.  

## Les instructions d'utilisation :

### Les prérequis :

Pour pouvoir lancer l'application, sans rencontrer de soucis, il satsfaire certain prérequis.  
Tout d'abord vous devez avoir ***Git*** et ***Python*** installé sur votre machine.  
Vous devez aussi avoir **Docker**, logiciel de contenairisation, indispensable pour lancer l'application et la relier la base de donnée.

*Il se peut que vous rencontriez des problèmes au lancement de l'application (le container mongo qui crash au démarrage) c'est la raison pour laquel nous vous conseillons de ne pas utiliser 'Windows' mais plutôt préférer des OS Linux comme 'Ubuntu 20'.*

### Lancement de l'application :

Pour pouvoir lancer l'application, il faut commencer par cloner le projet à l'endroit que vous souhaitez à l'aide la commande suivante :  
```bash
git clone <lien_du_repo>
```  
Après avoir réalisé cette commande, vous devez vous positionner dans le fichier **Flask_app** à l'aide de la commande suivante :
```bash
cd flask_app
```

Lorsque vous vous situez dans ce dossier vous devrer executer la commande :
```bash
docker-compose up -d
```
*Il est possible que vous ayait une erreur de droit pour régler le problème executez la commande en temps de 'super user' avec le term ```sudo``` au début de la commande.*

Vous devez voir apparaitre un long chargement qui montrera l'avancement de la construction de l'application.

**Optinnel** Lorsque ce chargement est terminé je vous invite à executer la commande suivante à fin de verifier que l'application tourne correctement :
```bash
docker ps
```
Si vous voyez les deux containers actif comme montré si dessous :
```bash
CONTAINER ID   IMAGE           COMMAND                  CREATED         STATUS         PORTS                                           NAMES
************  flask_app_app   "python -u appli.py"     4 seconds ago   Up 3 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp       flask_app
************  mongo:latest    "docker-entrypoint.s…"   5 seconds ago   Up 4 seconds   0.0.0.0:27018->27017/tcp, :::27018->27017/tcp   mongo

```
Alors l'appication est bien en route. Dans le cas contraire un problème est survenu (ce qui est certainement le cas si vous êtes sur Windows), nous vous conseillons donc de nous contacter par mail, ou de tester sur Linux.

### Affichege de l'application :
A prèsent il ne nous reste plus cas ouvrir un navigateur (Chrome, Firefox...) et d'afficher le port **5000** si rien ne l'occupe déjà, avec l'adresse ```localhost:5000```.

## L'application

L'application est actuellement constitué de deux page différents. 

Une page d'accuile donnant une explication général ainsi que quelque information chiffré sur l'application :

![home page](/home_page.png)

Mais vous pouvez aussi vous rendre dans une page de comparaison  des vols récupérés, à l'aide du menu *burger* en haut à gauche, qui vous permettrons d'avoir des information plus specifique sur les prix des billets ainsi que les jours et les heures les plus interressantes pour les acheter.


![comparaison page](/comp_page.png)

Si vous avez des idées ou conseils pour améliorer ou ajouter du contenu à l'application n'hésitez pas à proposer des idées.


## Le Scrapping des données :

Pour le moment (et a notre grande tristesse) le scrapping n'est pas directement relier à la base de données de l'application, car **Docker** et **Selenium** ne sont pas très compatible. Nous avions trouvé une solution pour résoudre le problème, mais elle n'était pas viable à cause de l'endroit ou nous scrappions les données, le site de comparaison de billets [Kayak](https://kayak.com/). Nous avons donc du renoncer à cette solution pour le moment, mais nous cherchons activement une solution pour donner à l'application un aspect plus complet et interractif.

Pour le moment nous avons utiliser une library de *scheduling* en pyhton pour nous permettre de lancer notre *scrappeur* pendant une semaine complète à interval de 10 minutes, se qui nous à permis de receuillir plus de 8000 vols.

L'utilisation de la librairie à grandement diminué le champs des possible au niveau du scrapping. En effet, nous avions d'abord réalisé une fonction qui permettait de saisir : 

- L'Aéroprt de départ/arrivé
- Les dates de départ/arrivé

Mais à cause de la librairie, nous ne pouvions pas choisir les déstinations ainsi que les dates, c'est la raison pour laquel nous avons dessidé de vous trouverais deux script de scrapping : *scrapping.py* (qui est celui que nous avons utilisé avec le schedeler) et *back.py* (qui est celui qui qui permet de gerer les différents champs).

### Lancer le scrapping :

Pour ca, il faut d'abord avoir *MongoDB* d'installer en local sur votre machine. Pour récuperer la donnée sur le site de kayak et la pipe dans Mongo de façon automatique (toute les 10 minutes), il faudrat que vous executiez le script *schedul.py* de la facon suivante : 
```bash
python schedul.py
```
Vous aurez les logs de chaque execution du script. Il se peut que le script générent des erreur (leur cause et pour le moment inconnue mais nous travaillons toujours à leurs résolution), or si le script de s'arrête pas complétement laisser le tourné l'erreur ne se reproduira certainement pas à la prochaine éxecution.

