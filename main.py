from reseau_fonctions import calculer_flsm

def executer_simulateur():
    print("=== CALCULATEUR IPV4 ===")
    
    # Entrées manuelles
    ip_base = input("Entrez l'IP du réseau (ex: 192.168.1.0) : ")
    masque = int(input("Entrez le masque actuel (ex: 24) : "))
    nb_sous_reseaux = int(input("Nombre de sous-réseaux souhaités : "))

    # Calcul
    liste_reseaux = calculer_flsm(ip_base, masque, nb_sous_reseaux)

    # Affichage
    print(f"\n{'ID':<3} | {'Réseau':<15} | {'Masque':<4} | {'Broadcast':<15} | {'Hôtes'}")
    print("-" * 65)
    for r in liste_reseaux:
        print(f"{r['id']:<3} | {r['reseau']:<15} | /{r['masque']:<3} | {r['broadcast']:<15} | {r['hotes']}")

if __name__ == "__main__":
    executer_simulateur()