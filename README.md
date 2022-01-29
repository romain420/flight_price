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

Une page d'accuile donnat une explication général ainsi que quelque information chiffré sur l'application :


