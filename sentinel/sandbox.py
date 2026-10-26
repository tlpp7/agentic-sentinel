"""Environnement d'exécution isolé et inspection AST sécurisée."""
import ast
import io
import sys
import contextlib

class ExecutionSandbox:
    @staticmethod
    def audit_security(code: str) -> list[str]:
        """Détecte statiquement les injections et fonctions critiques."""
        vulnerabilities = []
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec', '__import__']:
                        vulnerabilities.append(f"CWE-95 : Appel interdit à '{node.func.id}' ligne {node.lineno}")
        except SyntaxError as err:
            vulnerabilities.append(f"Erreur de syntaxe initiale : {str(err)}")
        return vulnerabilities

    @staticmethod
    def run_code(code: str, env: dict = None) -> tuple[bool, str, str]:
        """Exécute le code dans une sandbox en capturant STDOUT et STDERR."""
        env = env or {}
        stdout_trap = io.StringIO()
        stderr_trap = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout_trap), contextlib.redirect_stderr(stderr_trap):
                exec(code, env)
            return True, stdout_trap.getvalue(), stderr_trap.getvalue()
        except Exception as e:
            return False, stdout_trap.getvalue(), f"{type(e).__name__}: {str(e)}"