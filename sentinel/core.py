"""Moteur de raisonnement autonome et gestion des boucles d'auto-guérison."""
import time
from .config import CONFIG
from .sandbox import ExecutionSandbox

class AutonomousSentinelAgent:
    def __init__(self):
        self.config = CONFIG
        self.sandbox = ExecutionSandbox()

    def solve(self, task_name: str, code_attempts: list[str]) -> list[str]:
        logs = [f"🎯 [MISSION] : {task_name}"]
        start_time = time.time()

        for step, candidate_code in enumerate(code_attempts, start=1):
            # Circuit-Breaker 1 : Limite d'itérations
            if step > self.config.MAX_ITERATIONS:
                logs.append("🛑 [CIRCUIT-BREAKER] Nombre maximal d'itérations atteint. Arrêt préventif.")
                break

            # Circuit-Breaker 2 : Timeout matériel
            if (time.time() - start_time) > self.config.TIMEOUT_SECONDS:
                logs.append("⚡ [CIRCUIT-BREAKER] Timeout temporel dépassé. Arrêt forcé.")
                break

            logs.append(f"\n--- Cycle #{step}/{self.config.MAX_ITERATIONS} ---")
            
            # Audit de sécurité
            flaws = self.sandbox.audit_security(candidate_code)
            if flaws:
                logs.append(f"🚨 [SÉCURITÉ] Vulnérabilités détectées : {', '.join(flaws)}")
                logs.append("🔄 [RETRY] Génération d'une version patchée requise.")
                continue

            # Exécution Sandbox
            success, stdout, stderr = self.sandbox.run_code(candidate_code)
            if success and not stderr:
                logs.append("✅ [SUCCÈS] Code validé par la sandbox.")
                logs.append(f"Sortie : {stdout.strip()}")
                return logs
            else:
                logs.append(f"❌ [ERREUR D'EXÉCUTION] : {stderr or 'Erreur indéterminée'}")
                logs.append("🔄 [DEBUG] Déclenchement de l'auto-correction...")

        logs.append("⚠️ [STATUT] Tâche non résolue dans le budget imparti.")
        return logs