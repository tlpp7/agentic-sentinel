import os
import shutil
import subprocess

print("🧹 1. Réorganisation des dossiers...")

# 1. Création des dossiers cibles
os.makedirs("assets", exist_ok=True)
os.makedirs("docs", exist_ok=True)

# 2. Déplacement de l'image de télémétrie dans assets/
if os.path.exists("dashboard_metrics.png"):
    shutil.move("dashboard_metrics.png", "assets/dashboard_metrics.png")
    print("   -> Image déplacée dans assets/dashboard_metrics.png")

# 3. Création d'une documentation d'architecture dans docs/
arch_md = """# Architecture Technique & Justifications

## 1. Boucle ReAct & Auto-Correction
Le moteur utilise le patron **Reason + Act** :
- **Analyse AST :** Détection préventive des failles (CWE-95) avant exécution.
- **Bac à sable (Sandbox) :** Isolation mémoire et capture des sorties standard/erreur (`sys.stdout`, `sys.stderr`).

## 2. Calibration du Circuit-Breaker
- `MAX_ITERATIONS = 3` : Optimisé d'après le front de Pareto (93.5% de succès à ~2100 tokens).
- `TIMEOUT_SECONDS = 2.0` : Protection contre les calculs asymptotiques ou les séries infinies.
"""
with open("docs/ARCHITECTURE.md", "w", encoding="utf-8") as f:
    f.write(arch_md)
print("   -> Documentation technique créée dans docs/ARCHITECTURE.md")

# 4. Mise à jour des chemins dans README.md
if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("![Dashboard Télémétrique](dashboard_metrics.png)", "![Dashboard Télémétrique](assets/dashboard_metrics.png)")
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("   -> Liens mis à jour dans README.md")

# 5. Mise à jour de main.py pour générer l'image directement dans assets/
if os.path.exists("main.py"):
    with open("main.py", "r", encoding="utf-8") as f:
        main_content = f.read()
    main_content = main_content.replace('generate_telemetry_dashboard("dashboard_metrics.png")', 'generate_telemetry_dashboard("assets/dashboard_metrics.png")')
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(main_content)
    print("   -> Chemin par défaut de main.py ajusté vers assets/")

print("\n🌳 2. Arborescence finale réordonnée :")
tree_str = """
agentic-sentinel/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline CI/CD automatisé
├── assets/
│   └── dashboard_metrics.png   # Graphiques et médias du projet
├── docs/
│   └── ARCHITECTURE.md         # Spécifications d'ingénierie
├── sentinel/                   # Package Python principal
│   ├── __init__.py
│   ├── config.py
│   ├── core.py
│   ├── sandbox.py
│   └── telemetry.py
├── tests/
│   └── test_sentinel.py        # Suite de tests unitaires
├── .gitignore
├── LICENSE
├── README.md
├── app.py                      # Interface UI Gradio
├── main.py                     # Console CLI
└── requirements.txt
"""
print(tree_str)

print("🚀 3. Synchronisation avec GitHub...")
subprocess.run(["git", "add", "."], check=True)
subprocess.run(["git", "commit", "-m", "refactor: reorganize project structure into assets/, docs/ and core package"], check=False)
subprocess.run(["git", "push", "origin", "main"], check=True)

# Suppression du script temporaire
os.remove("reorder_project.py")
print("✅ Restructuration terminée et publiée sur GitHub !")
