"""Tests unitaires automatisés pour le moteur Sentinel."""
import unittest
from sentinel.sandbox import ExecutionSandbox
from sentinel.core import AutonomousSentinelAgent

class TestSentinelCore(unittest.TestCase):
    def setUp(self):
        self.sandbox = ExecutionSandbox()
        self.agent = AutonomousSentinelAgent()

    def test_ast_interception_eval(self):
        """Vérifie l'interception de CWE-95 sans exécution."""
        flaws = self.sandbox.audit_security("eval('1 + 1')")
        self.assertTrue(any("CWE-95" in f for f in flaws))

    def test_sandbox_clean_code(self):
        """Vérifie l'exécution valide du code sain."""
        ok, stdout, stderr = self.sandbox.run_code("print('Sentinel OK')")
        self.assertTrue(ok)
        self.assertIn("Sentinel OK", stdout)

    def test_circuit_breaker_boundary(self):
        """Vérifie l'activation du coupe-circuit face à des boucles d'échec."""
        broken_attempts = ["raise RuntimeError('Erreur!')"] * 10
        logs = self.agent.solve("Test Interruption", broken_attempts)
        self.assertTrue(any("CIRCUIT-BREAKER" in line for line in logs))

if __name__ == "__main__":
    unittest.main()
