import math

def ip_vers_entier(ip):
    """Convertit une chaîne IP en un entier 32 bits."""
    octets = list(map(int, ip.split('.')))
    return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]

def entier_vers_ip(n):
    """Convertit un entier 32 bits en chaîne IP."""
    return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"

def calculer_flsm(ip_base, masque_base, nb_sous_reseaux):
    """Calcule les segments réseau de taille fixe."""
    # Bits à emprunter : 2^n >= nb_sous_reseaux
    bits_empruntes = math.ceil(math.log2(nb_sous_reseaux))
    nouveau_masque = masque_base + bits_empruntes
    
    # Taille du bloc (saut)
    taille_bloc = 2 ** (32 - nouveau_masque)
    
    resultats = []
    ip_actuelle = ip_vers_entier(ip_base)
    
    for i in range(nb_sous_reseaux):
        addr_reseau = entier_vers_ip(ip_actuelle)
        broadcast = entier_vers_ip(ip_actuelle + taille_bloc - 1)
        hotes_utilisables = taille_bloc - 2
        
        resultats.append({
            "id": i + 1,
            "reseau": addr_reseau,
            "masque": nouveau_masque,
            "broadcast": broadcast,
            "hotes": hotes_utilisables
        })
        ip_actuelle += taille_bloc
        
    return resultats