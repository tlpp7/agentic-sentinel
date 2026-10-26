"""Interface Web prête pour démo / validation locale."""
import gradio as gr
from sentinel.core import AutonomousSentinelAgent

agent = AutonomousSentinelAgent()

def run_agent_demo(scenario):
    if scenario == "Nettoyage Data (Self-Healing)":
        code_v1 = "import pandas as pd\ndf = pd.DataFrame({'rev': ['10', 'NaN', '20'], 'cost': [5, 2, 8]})\nres = df['rev'] - df['cost']"
        code_v2 = "import pandas as pd\ndf = pd.DataFrame({'rev': ['10', 'NaN', '20'], 'cost': [5, 2, 8]})\ndf['rev'] = pd.to_numeric(df['rev'], errors='coerce').fillna(0)\ndf['margin'] = df['rev'] - df['cost']\nprint('Marge totale :', df['margin'].sum())"
        attempts = [code_v1, code_v2]
    else:
        code_vuln = "user_input = '__import__(\"os\").system(\"ls\")'\nresult = eval(user_input)"
        code_safe = "user_input = '10 + 20'\nprint('Calcul sécurisé :', eval(user_input, {'__builtins__': None}, {}))"
        attempts = [code_vuln, code_safe]

    logs = agent.solve(scenario, attempts)
    return "\n".join(logs)

demo = gr.Interface(
    fn=run_agent_demo,
    inputs=gr.Radio(["Nettoyage Data (Self-Healing)", "Sécurité DevSecOps (Auto-Patch)"], label="Scénario de test"),
    outputs=gr.Textbox(lines=18, label="Moniteur d'Exécution & Traces Internes"),
    title="🛡️ Agentic Sentinel : Plateforme Autonome Résiliente",
    description="Agent ReAct auto-correcteur avec Circuit-Breaker et Sandbox d'exécution isolée."
)

if __name__ == "__main__":
    demo.launch()