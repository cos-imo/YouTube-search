# YouTube search - A minimal Youtube search bar
![Static Badge](https://img.shields.io/badge/Backend-Python(Flask)-yellow)
![Static Badge](https://img.shields.io/badge/Frontend-HTML-orange)
![Static Badge](https://img.shields.io/badge/Frontend-Bootstrap-purple)
![Static Badge](https://img.shields.io/badge/D%C3%A9ploiement-uWSGI-blue)

## Présentation et Installation
### Présentation
Dans un monde de plus en plus connecté, servez-vous d'une barre de recherche "minimaliste" afin d'aller à l'essentiel et ne pas perdre de temps sur les suggestions.
Le présent projet et fait pour être installé et utilisé en local (! ne pas déployer! des failles existent!).
Dès lors qu'elle aura été implementée, une version "sûre" sera déployée sur [http://youtube-search.cosimoungaro.fr](http://youtube-search.cosimoungaro.fr)

### Installation
##### Téléchargement
###### Par SSH
```
git clone git@github.com:cos-imo/YouTube-search.git
```
###### Par HTTP
```
git clone https://github.com/cos-imo/YouTube-search.git
```

##### Activation de l'environnement virtuel
```
cd YouTube-search
source .venv/bin/activate
```

##### Installation des dépendances (optionnel)
**Attention** à être dans le dossier YouTube-search
```
pip install -r requirements.txt
```

##### Lancement
Depuis la racine du projet (dossier YouTube-search) exécuter:
```
flask run
```
Pour activer le débogueur:
```
flask run --debug
```
