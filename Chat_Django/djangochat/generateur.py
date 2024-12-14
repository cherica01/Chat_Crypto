from cryptography.fernet import Fernet

def generate_fernet_key():
    """
    Génère une clé de chiffrement Fernet valide.
    Retourne la clé sous forme de chaîne encodée en Base64.
    """
    key = Fernet.generate_key()  
    return key.decode()  

def main():
    print("=== Générateur de clés de chiffrement ===")
    while True:
        
        new_key = generate_fernet_key()
        print(f"Clé générée : {new_key}")

        
        choice = input("Voulez-vous générer une autre clé ? (o/n) : ").strip().lower()
        if choice != 'o':
            print("Au revoir !")
            break

if __name__ == "__main__":
    main()