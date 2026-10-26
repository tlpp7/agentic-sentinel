"""Paramètres de configuration calibrés sur les métriques empiriques."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AgentConfig:
    # 3 cycles = 89% de réussite, avant la zone de rendements décroissants
    MAX_ITERATIONS: int = 3
    # Timeout de sécurité pour contrer les boucles infinies (test Pi - Infini)
    TIMEOUT_SECONDS: float = 2.0
    # Plafond de tokens pour rester sur le front optimal de Pareto
    TOKEN_BUDGET: int = 3000
    # Nom de l'agent
    AGENT_NAME: str = "Sentinel-ReAct"

CONFIG = AgentConfig()