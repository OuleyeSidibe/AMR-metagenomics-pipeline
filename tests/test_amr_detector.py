""" Tests unitaires automatisés pour le module amr_detctor.py ( éxecutés via pytest)."""

# Import de la bibliothéque de gestion des exceptions pour vérifier les cas d'erreur
import pytest

# Import de la fonction métier à tester depuis le dossier src
from src.amr_detector import filter_amr_hits


""" Test du cas nominal : vérifie que le filtrage par identity fonctionne normallement """


def test_filter_amr_hits_nominal_case():

    # 1 PREPARATION DES DONNEES DE TEST (FIXTURE / MOCK)

    ## Création de jeu de données  factice représentatif d'un résultat d'alignement BLAST / ResFinder
    sample_data = [
        {"gene": "blaTEM-1", "identity": 98.5, "coverage": 100.0},  # Doit être conservé
        {"gene": "tet(A)", "identity": 85.0, "coverage": 90.0},  # Doit être rejeté
        {"gene": "aac(6)-Ib", "identity": 91.2, "coverage": 95.0},  # Doit être conservé
    ]

    # 2 EXECUTION DE LA FONCTION A TESTER

    ## Appel de la fonction avec un seuil id à 90%
    results = filter_amr_hits(sample_data, min_identity=90.0)

    # 3 ERIFICATION (ASSERTIONS)

    ## Vérification 1 : On doit obtenir 2 gènes filtés sur 3 initiaux
    assert len(results) == 2
    ## vérification 2 : les deux génes doivnet être les gènes : bla-TEM-1 et aac(6)-Ib
    assert results[0]["gene"] == "blaTEM-1"
    assert results[1]["gene"] == "aac(6)-Ib"


""" Test de sécurité: vérifie qu'une exeption valueERROR est bien levée si le seuil est invalide. """


def test_filter_amr_hits_invalid_threshold():

    # Données de test minimales
    sample_data = [{"gene": "blaTEM-1", "identity": 98.5}]

    # Indiquer à 'pytest' qu'une execution ValueERROR DOIT se produire lors de l'execution du bloc
    with pytest.raises(ValueError):
        # Appel avec un seuil d'identité invalide (150%) qui doit déclencher le mécanisme de sécurité
        filter_amr_hits(sample_data, min_identity=150.0)
