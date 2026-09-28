# AMR Metagenomic Pipeline 🧬

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Docker Image](https://img.shields.io/badge/docker-sidibeouleye%2Famr--metagenomic--pipeline%3Av1.0-blue)](https://hub.docker.com/r/sidibeouleye/amr-metagenomic-pipeline)
[![Tests Coverage](https://img.shields.io/badge/pytest-100%25_coverage-brightgreen.svg)]()
[![Compliance](https://img.shields.io/badge/FAIR%2FGxP-Compliant-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un pipeline bioinformatique conteneurisé, testé et reproductible conçu pour la détection automatisée et l'analyse de gènes de résistance aux antimicrobiens (AMR) à partir de données métagénomiques.

Ce projet applique les rigueurs de l'ingénierie logicielle (TDD, conteneurisation, gestion défensive des erreurs) aux contraintes des données de génomique microbienne.

---

## 🚀 Fonctionnalités Principales

- **Détection défensive AMR (`amr_detector.py`) :** Module Python permettant de parser, valider et filtrer les hits de résistance (AMR) avec gestion robuste des anomalies de données (fichiers corrompus, valeurs aberrantes).
- **Assurance Qualité & Tests (TDD) :** Validation continue du code via `pytest` atteignant une **couverture de code de 100 %** (`pytest-cov`).
- **Conteneurisation ISO/GxP (`Dockerfile`) :** Environnement d'exécution totalement isolé et reproductible basé sur `python:3.10-slim`, exempt de dépendances hôtes.
- **Registre Cloud (Docker Hub) :** Image de production compilée et publiée sur Docker Hub (`sidibeouleye/amr-metagenomic-pipeline:v1.0`).
- **Traçabilité FAIR & GxP :** Documentation stricte des schémas de métadonnées et suivi des versions du code/données (`METADATA.md`).

---

## 📁 Architecture du Dépôt

```text
amr-metagenomic-pipeline/
├── src/
│   ├── __init__.py           # Package Python amr_pipeline
│   └── amr_detector.py       # Logique métier d'analyse des hits AMR
├── tests/
│   ├── __init__.py
│   └── test_amr_detector.py  # Tests unitaires et cas aux limites (pytest)
├── docs/
│   └── METADATA.md           # Spécifications de traçabilité FAIR/GxP
├── .dockerignore             # Exclusions pour l'optimisation du build Docker
├── Dockerfile                # Recette de conteneurisation de production
├── pyproject.toml            # Configuration du package Python (PEP 517/518)
├── requirements.txt          # Dépendances système et de test

🛠️ Installation et Exécution
Option 1 : Exécution directe via Docker (Recommandé)

Aucune installation préalable de Python, pytest ou dépendances locales n'est nécessaire. L'image télécharge et exécute automatiquement l'environnement de production.
Bash

# 1. Récupérer l'image validée depuis Docker Hub
docker pull sidibeouleye/amr-metagenomic-pipeline:v1.0

# 2. Exécuter le conteneur (lance la suite complète de tests)
docker run --rm sidibeouleye/amr-metagenomic-pipeline:v1.0

Option 2 : Environnement de développement local

Si vous souhaitez modifier le code source ou ajouter des fonctionnalités :
1. Prérequis & Clonnage
Bash

git clone [https://github.com/sidibeouleye/amr-metagenomic-pipeline.git](https://github.com/sidibeouleye/amr-metagenomic-pipeline.git)
cd amr-metagenomic-pipeline

2. Installation des dépendances
Bash

# Installation des paquets requis
pip install -r requirements.txt

# Installation du paquet local en mode éditable
pip install -e .

3. Exécution de la suite de tests unitaires
Bash

python -m pytest --cov=src tests/

Résultat attendu :
Plaintext

============================== test session starts ==============================
collected 2 items

tests/test_amr_detector.py ..                                            [100%]

---------- coverage: platform linux, python 3.10.x -----------
Name                  Stmts   Miss  Cover
-----------------------------------------
src/__init__.py           0      0   100%
src/amr_detector.py      10      0   100%
-----------------------------------------
TOTAL                    10      0   100%

=============================== 2 passed in 0.08s ===============================

⚙️ Détails Techniques de la Conteneurisation

L'image Docker a été conçue en respectant les standards industriels :

    Minimisation de la surface d'attaque : Utilisation de l'image officielle python:3.10-slim.

    Nettoyage des couches (Layers) : Suppression explicite des caches apt et pip (--no-cache-dir) pour réduire la taille globale de l'image.

    Sécurisation du runtime : Variable PYTHONPATH=/app injectée pour garantir la résolution native des modules internes sans dépendre de chemins relatifs hôtes.

📝 Roadmap du Projet 

    [x] Jour 1 : Architecture logicielle, programmation défensive et tests unitaires (100% coverage).

    [x] Jour 2 : Conteneurisation Docker, optimisation de build et déploiement Docker Hub.

    [ ] Jour 3 : Orchestration de workflow multi-étapes avec Nextflow (DSL2) & intégration Docker.

    [ ] Jour 4 : Traitement de données métagénomiques haute densité (FASTQ/BAM) et parallélisation.

    [ ] Jour 5 : Automatisation CI/CD via GitHub Actions (Linting, Test, Docker Build & Push).

👤 Auteur

Dr. Ouleye Sidibé — Bioinformatics Engineer / Microbial Genomics Specialist

    GitHub : @sidibeouleye

    Docker Hub : sidibeouleye
