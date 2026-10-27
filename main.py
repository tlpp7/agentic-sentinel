"""Interface en Ligne de Commande (CLI) pour Agentic Sentinel."""
import argparse
import sys
from sentinel.core import AutonomousSentinelAgent
from sentinel.telemetry import generate_telemetry_dashboard

def main():
    parser = argparse.ArgumentParser(description="🛡️ Console CLI d'Agentic Sentinel")
    parser.add_argument("--mode", choices=["data", "security", "telemetry"], default="data",
                        help="Mode d'exécution : data (analyse ETL), security (audit code) ou telemetry (graphiques)")
    
    args = parser.parse_args()
    agent = AutonomousSentinelAgent()

    if args.mode == "data":
        print("🚀 Lancement du mode Data Healing...")
        attempts = [
            "import pandas as pd\ndf = pd.DataFrame({'val': ['10', 'bad']})\nres = df['val'] - 5",
            "import pandas as pd\ndf = pd.DataFrame({'val': ['10', 'bad']})\ndf['val'] = pd.to_numeric(df['val'], errors='coerce').fillna(0)\nprint('Somme certifiée :', (df['val'] + 5).sum())"
        ]
        logs = agent.solve("Pipeline Données Corrompues", attempts)
        print("\n".join(logs))

    elif args.mode == "security":
        print("🔍 Lancement du mode Audit de Sécurité...")
        attempts = [
            "code_danger = '__import__(\"os\").system(\"echo Hacked\")'\neval(code_danger)",
            "safe_val = '10 + 20'\nprint('Calcul certifié :', eval(safe_val, {'__builtins__': None}, {}))"
        ]
        logs = agent.solve("Audit & Auto-Patch CWE-95", attempts)
        print("\n".join(logs))

    elif args.mode == "telemetry":
        print("📈 Génération des courbes de performance...")
        generate_telemetry_dashboard("assets/dashboard_metrics.png")

if __name__ == "__main__":
    main()