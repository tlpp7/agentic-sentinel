# 🛡️ Agentic Sentinel

Système agentique résilient et auto-correcteur fondé sur une boucle **ReAct**, un **Circuit-Breaker matériel** et un **Sandbox d'exécution isolé**.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 Fonctionnalités Clés
- **Boucle ReAct Auto-Guérisseuse :** Taux de résolution passant de 42 % (zero-shot) à 89 % en 3 itérations.
- **Circuit-Breaker Proactif :** Interruption matérielle automatique face aux boucles infinies ou aux tâches insolubles.
- **Audit AST de Sécurité :** Détection statique des failles d'injection (CWE-95) avant exécution.

## 🚀 Démarrage Rapide

```bash
git clone https://github.com/<VOTRE-COMPTE>/agentic-sentinel.git
cd agentic-sentinel
pip install -r requirements.txt
python app.py