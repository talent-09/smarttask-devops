# SmartTask DevOps

Application SmartTask conteneurisée (backend Python, frontend, base MySQL) avec pipeline CI/CD Jenkins et déploiement GitOps.

## Architecture
- `backend/` — API backend (Python)
- `frontend/` — Interface web (HTML/CSS/JS)
- `mysql/` — Base de données et script d'initialisation
- `docker-compose.yml` — Orchestration des services en local

## Branches
- `Dev` — Environnement de développement/intégration
- `Prod` — Environnement de production

## CI/CD
Chaque branche dispose de son propre `Jenkinsfile` définissant le pipeline (build, tests, déploiement).

## Démarrage local
```bash
docker compose up --build
```
