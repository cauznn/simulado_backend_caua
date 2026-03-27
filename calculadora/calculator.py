class Calculator:
    def add(self, a: float, b: float) -> float:
        """Metodo ja implementado para servir de exemplo."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtrai b de a e retorna o resultado."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplica a por b e retorna o resultado."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divide a por b e retorna o resultado.

        Lanca ZeroDivisionError se b for zero.
        """
        if b == 0:
            raise ZeroDivisionError("Divisao por zero nao permitida.")
        return a / b
