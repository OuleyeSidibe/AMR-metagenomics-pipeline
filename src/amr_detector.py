""" Module d'analyse et de filtrage des gènes de résistances aux antibiotiques (AMR) """

""" Filtre une liste de gène de résistance détecté selon un seuil minimal d'identité
    
        Args : 
            - hits : liste de dictionnaires représentant chaque detection (ex : [{'gene': 'blaTEM-1', 'identity': 95.0 }]) 
            - min_identity : %id min requis (val par défaut : 90%)
        
        returns : 
            Liste filtré contenant uniquemment les gènes avec une id >= seuil id requis
            
        Raises : 
            ValueERROR : Levée si le seuil d'identité fourni est hors de l'intervalle [0, 100] """

# Validation de la qualité des données d'entrées


# Importations des annotations de types Python pour expliciter ce que prennent et renvoient les fonctions
from typing import Dict, List


# Filtre des AMR
def filter_amr_hits(
    hits: List[Dict[str, float]], min_identity: float = 90.0
) -> List[Dict[str, float]]:

    ## Si le seuil min drid fixé par l'utilisateur n'est pas un % valide compris entre 0 et 100, on stoppe le programme
    if not (0 <= min_identity <= 100):
        ## On léve une exception claire pour empêcher les erreurs silencieuses ou résusltas corrompus
        raise ValueError("Le seuil min_identity doit être compris entre 0 et 100.")

    # Liste des gènes retenus
    filtered_results = []

    # Boucle d'inspection des gènes
    for hit in hits:

        #  Extraction du pourcentage d'identité du gène (valeur 0.0 par défaut si la clé n'existe pas)
        identity_val = hit.get("identity", 0.0)

        # Verification de la condition métrologique : l'id du géne est-elle supérieure ou égale au seuil ?
        if identity_val >= min_identity:
            filtered_results.append(hit)

    return filtered_results
