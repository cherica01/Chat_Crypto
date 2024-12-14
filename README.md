💬 Django Chat Platform

Une plateforme de chat en temps réel construite avec Django, permettant aux utilisateurs de discuter dans différents salons, avec la possibilité de chiffrer et de déchiffrer leurs messages.
🛠️ Fonctionnalités

    Gestion des salons : Créez ou rejoignez des salons de discussion en utilisant un nom unique.
    Envoi et réception des messages : Les messages sont envoyés et reçus en temps réel.
    Chiffrement des messages : Les utilisateurs peuvent choisir de chiffrer leurs messages pour garantir la confidentialité.
    Déchiffrement des messages : Les messages chiffrés peuvent être déchiffrés avec une clé spécifique.

🚀 Installation
1. Cloner le projet

git clone https://github.com/votre-repository/django-chat-platform.git
cd django-chat-platform

2. Configurer l'environnement virtuel

python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate

3. Installer les dépendances

pip install -r requirements.txt

4. Configurer la base de données

Appliquez les migrations pour configurer la base de données SQLite (par défaut) :

python manage.py makemigrations
python manage.py migrate

5. Lancer le serveur

python manage.py runserver

Accédez à l'application à l'adresse http://127.0.0.1:8000.
🗂️ Structure du projet

    models.py : Définit les modèles Room et Message.
    views.py : Gère la logique d'application pour les salons, les messages et le chiffrement.
    templates/ : Contient les fichiers HTML pour l'interface utilisateur.
    urls.py : Définit les routes pour l'application.

🔑 Fonctionnalité de chiffrement
Comment chiffrer un message

    Entrez un message.
    Fournissez une clé de chiffrement dans le champ dédié.
    Le message sera automatiquement chiffré avant d’être envoyé.

Comment déchiffrer un message

    Entrez une clé de déchiffrement dans le champ dédié.
    Les messages chiffrés seront déchiffrés si la clé est correcte.

📦 Dépendances

    Django : Framework backend utilisé pour construire l'application.
    Cryptography : Bibliothèque pour le chiffrement et le déchiffrement des messages.

Installation des dépendances

Les dépendances sont incluses dans le fichier requirements.txt. Pour les installer :

pip install -r requirements.txt

✨ Améliorations futures

    Implémentation d'une authentification utilisateur (connexion/inscription).
    Ajout de notifications en temps réel avec WebSockets.
    Support pour les avatars et personnalisation des salons.

📄 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, de le modifier et de le distribuer. Consultez le fichier LICENSE pour plus d'informations.
🤝 Contribution

Les contributions sont les bienvenues !

    Forkez ce dépôt.
    Créez une branche pour vos modifications : git checkout -b feature-nom.
    Soumettez une pull request pour révision.

