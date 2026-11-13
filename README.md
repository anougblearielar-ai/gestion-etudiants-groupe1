# Gestion des étudiants — Groupe 1

## Lancer en local

Depuis la racine du projet :

```powershell
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Ouvre ensuite <http://127.0.0.1:8000/>. La racine redirige vers la liste des étudiants.
Active d’abord l’environnement Python du projet dans le terminal. Les paramètres locaux
utilisent SQLite et activent le mode développement par défaut. Un fichier `.env` à la
racine est chargé automatiquement.

## Déployer sur Render

- **Build command** : `pip install -r requirements.txt && bash build.sh`
- **Start command** : `gunicorn config.wsgi:application`
- Définir `SECRET_KEY` et `DATABASE_URL` dans les variables d’environnement du service.

Quand Render fournit `RENDER_EXTERNAL_HOSTNAME`, `DEBUG` est désactivé par défaut et les
réglages HTTPS sont activés. Ne définis `DEBUG=True` que pour le développement local.
