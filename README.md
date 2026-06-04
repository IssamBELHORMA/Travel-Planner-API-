Travel Planner API
==================

Description
-----------
API minimale construite avec FastAPI pour :
- créer un compte utilisateur
- se connecter (JWT)
- demander un plan de voyage pour une ville (météo + activités)

Prérequis
---------
- Python 3.10+
- MySQL accessible (base `travel_planner` recommandée)
- Un fichier `.env` à la racine du projet avec les variables listées ci‑dessous

Variables d'environnement
-------------------------
Créez un fichier `.env` et définissez au minimum :

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=travel_planner
DB_PORT=3306
JWT_SECRET_KEY=change_me
OPENWEATHER_API_KEY=your_openweather_key

Base de données
---------------
SQL minimal pour créer la table `users` (déjà gérée automatiquement par SQLAlchemy sur démarrage) :

```sql
CREATE TABLE users (
  id VARCHAR(36) PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  created_at DATETIME NOT NULL
);
```

Table `activities` recommandée :

```sql
CREATE TABLE activities (
  id INT PRIMARY KEY AUTO_INCREMENT,
  city VARCHAR(100) NOT NULL,
  activity_name VARCHAR(255) NOT NULL,
  INDEX (city)
);
```

Il est utile d'ajouter des lignes pour `city = 'default'` afin d'avoir des activités fallback.

Installation
------------
1. Créez et activez un environnement virtuel :

```powershell
python -m venv venv
& venv\Scripts\Activate.ps1
```

2. Installez les dépendances :

```powershell
pip install -r requirements.txt
```

Exécution
---------
Lancer le serveur de développement :

```powershell
uvicorn app.main:app --reload
```

Tests rapides (exemples)
-----------------------
- Enregistrer un utilisateur :

```bash
curl -X POST http://localhost:8000/users \
  -H "Content-Type: application/json" \
  -d '{"email":"me@example.com","password":"pass"}'
```

- Se loguer et récupérer le token :

```bash
curl -s -X POST http://localhost:8000/login \
  -H "Content-Type: application/json" \
  -d '{"email":"me@example.com","password":"pass"}'
# la réponse contient {"access_token": "..."}
```

- Demander un plan (remplacez TOKEN par le token reçu) :

```bash
curl -X POST http://localhost:8000/plan \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"city":"paris"}'
```

Frontend
--------
Ouvrez le fichier `index.html` dans un navigateur (ou servez‑le) ; il envoie des requêtes à `http://localhost:8000` et attend `weather` + `activities` dans la réponse JSON.

Remarques et maintenance
------------------------
- Les données utilisateur sont maintenant stockées en MySQL via SQLAlchemy (`app/storage/db.py`).
- Le stockage CSV (`app/storage/csv_store.py`) est obsolète et peut être supprimé si vous n'en avez plus besoin.
- Assurez‑vous que `OPENWEATHER_API_KEY` est défini pour que la route `/plan` renvoie la météo.
- Si vous ajoutez des activités en base, enregistrez `city` en minuscules (ou adaptez la requête dans `app/storage/db.py`).

Initialiser la base et peupler `activities`
------------------------------------------
Le fichier `app/services/schema.sql` contient la création de la base `travel_planner`, les tables `users` et `activities`, ainsi qu'un lot d'inserts par défaut pour `activities` (dont `city = 'default'`). Le script utilise `INSERT IGNORE` et un index unique `(city, activity_name)` pour éviter les doublons.

Pour exécuter le script avec le client MySQL :

```bash
# depuis la racine du projet
mysql -u $DB_USER -p < app/services/schema.sql
```

Exemple concret (vous serez invité à saisir le mot de passe) :

```bash
mysql -u root -p < app/services/schema.sql
```

Si vous n'avez pas le client `mysql` installé, vous pouvez importer le fichier via votre outil d'administration (MySQL Workbench, phpMyAdmin, etc.).

Vérification rapide (depuis mysql) :

```sql
USE travel_planner;
SELECT COUNT(*) FROM activities;
SELECT activity_name FROM activities WHERE city = 'paris';
```

Support
-------
Pour toute question, ouvrez une issue ou contactez le mainteneur.
