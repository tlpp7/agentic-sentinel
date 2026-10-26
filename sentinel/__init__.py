"""
Agentic Sentinel Package
~~~~~~~~~~~~~~~~~~~~~~~~
Système agentique résilient avec auto-correction ReAct et Circuit-Breaker.
"""

from .config import CONFIG, AgentConfig
from .sandbox import ExecutionSandbox
from .core import AutonomousSentinelAgent

__all__ = ["CONFIG", "AgentConfig", "ExecutionSandbox", "AutonomousSentinelAgent"]
__version__ = "1.0.0"