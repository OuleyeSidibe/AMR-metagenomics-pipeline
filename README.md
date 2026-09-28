# AMR Metagenomic Pipeline 🧬

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Docker Image](https://img.shields.io/badge/docker-sidibeouleye%2Famr--metagenomic--pipeline%3Av1.0-blue)](https://hub.docker.com/r/sidibeouleye/amr-metagenomic-pipeline)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Status](https://img.shields.io/badge/status-en%20cours%20(jours%201--2%2F5)-orange.svg)

> 🚧 **Projet en cours (jours 1-2 sur 5).** Le socle d'ingénierie logicielle est en place (module Python testé, image Docker publiée). Le workflow Nextflow, le traitement de données métagénomiques réelles et la CI/CD sont **à venir** (voir la [roadmap](#-roadmap-du-projet)).

Un projet bioinformatique conteneurisé, testé et reproductible pour la détection et l'analyse de gènes de résistance aux antimicrobiens (AMR) à partir de données métagénomiques.

Il applique des pratiques d'ingénierie logicielle (développement guidé par les tests, conteneurisation, gestion défensive des erreurs) aux contraintes des données de génomique microbienne.

---

## 🚀 Fonctionnalités actuelles

- **Détection défensive AMR (`amr_detector.py`) :** module Python qui parse, valide et filtre les hits de résistance (AMR), avec une gestion robuste des anomalies de données (fichiers corrompus, valeurs aberrantes).
- **Tests unitaires :** suite `pytest` avec mesure de couverture (`pytest-cov`) ; couverture de 100 % sur le module actuel (10 instructions).
- **Conteneurisation (`Dockerfile`) :** environnement d'exécution isolé et reproductible basé sur `python:3.10-slim`, sans dépendance à l'hôte.
- **Registre Docker Hub :** image `v1.0` publiée sur Docker Hub (`sidibeouleye/amr-metagenomic-pipeline:v1.0`).
- **Traçabilité des métadonnées :** schémas de métadonnées et suivi des versions du code et des données documentés dans `docs/METADATA.md`, en s'inspirant des principes FAIR.

## ⚠️ Limites actuelles

- Le dépôt ne traite pas encore de fichiers FASTQ/BAM : le module travaille sur des tables de hits AMR déjà produites.
- Pas encore d'orchestration de workflow (Nextflow prévu) ni d'intégration continue (GitHub Actions prévu).
- Le badge de couverture sera ajouté une fois la CI en place, pour qu'il reflète une exécution réelle.

---

## 📁 Architecture du dépôt

```text
amr-metagenomic-pipeline/
├── src/
│   ├── __init__.py           # Package Python amr_pipeline
│   └── amr_detector.py       # Logique d'analyse des hits AMR
├── tests/
│   ├── __init__.py
│   └── test_amr_detector.py  # Tests unitaires et cas aux limites (pytest)
├── docs/
│   └── METADATA.md           # Spécifications de traçabilité des métadonnées
├── .dockerignore             # Exclusions pour l'optimisation du build Docker
├── Dockerfile                # Recette de conteneurisation
├── pyproject.toml            # Configuration du package Python (PEP 517/518)
├── requirements.txt          # Dépendances d'exécution et de test
└── README.md
```

---

## 🛠️ Installation et exécution

### Option 1 : exécution via Docker (recommandé)

Aucune installation préalable de Python, pytest ou d'autres dépendances n'est nécessaire.

```bash
# 1. Récupérer l'image depuis Docker Hub
docker pull sidibeouleye/amr-metagenomic-pipeline:v1.0

# 2. Exécuter le conteneur (lance la suite de tests)
docker run --rm sidibeouleye/amr-metagenomic-pipeline:v1.0
```

### Option 2 : environnement de développement local

Pour modifier le code source ou ajouter des fonctionnalités.

**1. Cloner le dépôt**

```bash
git clone https://github.com/OuleyeSidibe/AMR-metagenomics-pipeline.git
cd AMR-metagenomics-pipeline
```

**2. Installer les dépendances**

```bash
# Paquets requis
pip install -r requirements.txt

# Paquet local en mode éditable
pip install -e .
```

**3. Lancer les tests unitaires**

```bash
python -m pytest --cov=src tests/
```

Résultat attendu :

```text
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
```

---

## ⚙️ Détails de la conteneurisation

- **Image légère :** base officielle `python:3.10-slim`.
- **Couches allégées :** suppression des caches apt et pip (`--no-cache-dir`) pour réduire la taille de l'image.
- **Résolution des modules :** variable `PYTHONPATH=/app` pour que les modules internes soient trouvés indépendamment des chemins de l'hôte.

---

## 📝 Roadmap du projet

| Jalon | Contenu | Statut | Date |
|---|---|---|---|
| Jour 1 | Architecture logicielle, programmation défensive, tests unitaires (100 % de couverture) | ✅ Terminé | [JJ/MM/AAAA] |
| Jour 2 | Conteneurisation Docker, optimisation du build, publication sur Docker Hub | ✅ Terminé | [JJ/MM/AAAA] |
| Jour 3 | Orchestration multi-étapes avec Nextflow (DSL2) et intégration Docker | ⏳ À venir | [JJ/MM/AAAA] |
| Jour 4 | Traitement de données métagénomiques (FASTQ/BAM) et parallélisation | ⏳ À venir | [JJ/MM/AAAA] |
| Jour 5 | CI/CD avec GitHub Actions (lint, tests, build et push Docker) et badge de couverture réel | ⏳ À venir | [JJ/MM/AAAA] |

---

## 👤 Auteur

**Dr. Ouleye Sidibé** : Bioinformatics Engineer / Microbial Genomics Specialist

- GitHub : [@OuleyeSidibe](https://github.com/OuleyeSidibe)
- Docker Hub : [sidibeouleye](https://hub.docker.com/u/sidibeouleye)
