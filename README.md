
# IPv4 Network Analyzer(Python)

## Présentation du Projet

Ce projet est un outil d'ingénierie réseau permettant d'automatiser le découpage d'un réseau IP en plusieurs sous-réseaux de taille fixe (**Fixed Length Subnet Mask - FLSM**).

Développé dans une approche **procédurale**, ce programme démontre la maîtrise des opérations binaires de bas niveau et de la logique de segmentation IP, des concepts fondamentaux enseignés en deuxième année de cursus informatique (L2).

## Fonctionnalités

* **Conversion Dynamique** : Transformation d'adresses IPv4 (notation décimale pointée) en entiers 32 bits et vice-versa via décalages de bits.
* **Planification FLSM** : Calcul automatique du nombre de bits à emprunter sur la partie hôte.
* **Analyse de Segment** : Pour chaque sous-réseau, le programme génère :
* L'adresse réseau.
* Le nouveau masque.
* L'adresse de broadcast (diffusion).
* Le nombre d'hôtes réels exploitables.


* **Gestion des Erreurs** : Validation des entrées utilisateur pour éviter les chevauchements ou les masques invalides.

## 🛠 Concepts Techniques Démontrés

* **Arithmétique Binaire** : Utilisation des opérateurs de décalage (`<<`, `>>`) et des masques binaires (`&`) pour extraire les octets.
* **Algorithmique Logarithmique** : Utilisation de $\log_2$ pour déterminer de manière optimale l'emprunt de bits.
* **Structures de Données** : Organisation des segments réseau dans des listes de dictionnaires pour une manipulation efficace.

## Structure du Projet

* `reseau_fonctions.py` : Le "moteur" contenant les fonctions mathématiques et binaires.
* `main.py` : L'interface utilisateur interactive pour les tests en direct.

## Installation et Utilisation

1. **Cloner le projet** :
```bash
git clone https://github.com/ostineashley-arch/IPv4-Network-Analyzer.git
cd IPv4-Network-Analyzer

```


2. **Lancer le simulateur** :
```bash
python main.py

```



## Exemple de Démonstration

**Entrée :**

* Réseau : `192.168.1.0`
* Masque : `/24`
* Besoin : `4 sous-réseaux`

**Analyse de l'IA :**

* Emprunt de **2 bits** ($2^2 = 4$).
* Nouveau masque : `/26`.
* Taille de bloc : **64 adresses**.

---

*Projet réalisé dans le cadre d'une évaluation académique visant à démontrer la maîtrise des concepts d'architecture réseau et de programmation système.*
