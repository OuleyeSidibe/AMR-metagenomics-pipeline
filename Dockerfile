# 1. Image de base Linux minimale pré-équipée de Python 3.10
FROM python:3.10-slim

# 2. Empêche Python de créer des fichiers .pyc et force l'affichage direct des logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# 3. Répertoire de travail interne
WORKDIR /app

# 4. Installation des outils système
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 5. Copie explicite du fichier de dépendances
COPY requirements.txt pyproject.toml ./

# 6. Installation forcée et globale de pytest, pytest-cov et des dépendances
RUN python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir -r requirements.txt

# 7. Copie du code source et des tests dans le conteneur
COPY src/ ./src/
COPY tests/ ./tests/

# 8. Commande de lancement automatique des tests
CMD ["python", "-m", "pytest", "--cov=src", "tests/"]