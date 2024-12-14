Documentation du Projet de Messagerie Sécurisée avec Django

Ce projet consiste en une application de messagerie sécurisée développée avec le framework Django. Les messages sont envoyés et stockés dans une base de données SQLite et sont chiffrés à l'aide de la bibliothèque cryptography. L'application utilise des clés de chiffrement Fernet pour assurer la confidentialité des messages échangés entre les utilisateurs.
Fonctionnalités principales :

    Chiffrement des Messages : Lorsqu'un utilisateur envoie un message, celui-ci est chiffré à l'aide d'une clé Fernet avant d'être stocké dans la base de données SQLite.
    Déchiffrement des Messages : Lorsque l'utilisateur consulte ses messages, ils sont déchiffrés à l'aide de la même clé Fernet.
    Gestion des Rooms : Les utilisateurs peuvent envoyer des messages dans différentes rooms (salles de discussion). Chaque room est associée à une clé de chiffrement unique.
    Authentification : Les utilisateurs doivent s'authentifier pour accéder à l'application et envoyer ou lire des messages. Le système utilise le mécanisme d'authentification intégré de Django.
    Stockage des Messages : Les messages sont sauvegardés dans une base de données SQLite, et chaque message est associé à une room spécifique.

Technologies Utilisées :

    Django : Framework web pour le développement de l'application.
    SQLite : Base de données légère utilisée pour stocker les messages et les informations des utilisateurs.
    Cryptography : Bibliothèque Python pour le chiffrement et le déchiffrement des messages à l'aide de clés Fernet.
    HTML, CSS, JavaScript : Technologies utilisées pour l'interface utilisateur.