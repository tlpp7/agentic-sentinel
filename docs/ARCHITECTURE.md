# Architecture Technique & Justifications

## 1. Boucle ReAct & Auto-Correction
Le moteur utilise le patron **Reason + Act** :
- **Analyse AST :** Détection préventive des failles (CWE-95) avant exécution.
- **Bac à sable (Sandbox) :** Isolation mémoire et capture des sorties standard/erreur (`sys.stdout`, `sys.stderr`).

## 2. Calibration du Circuit-Breaker
- `MAX_ITERATIONS = 3` : Optimisé d'après le front de Pareto (93.5% de succès à ~2100 tokens).
- `TIMEOUT_SECONDS = 2.0` : Protection contre les calculs asymptotiques ou les séries infinies.
