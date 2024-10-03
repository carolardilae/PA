class Suma:
    def operar(self, num1, num2):
        return num1 + num2

class Resta:
    def operar(self, num1, num2):
        return num1 - num2

class Multiplicacion:
    def operar(self, num1, num2):
        return num1 * num2

class Division:
    def operar(self, num1, num2):
        if num2 == 0:
            return "error"
        return num1 / num2

class Exponencial:
    def operar(self, base, exponente):
        return base ** exponente
