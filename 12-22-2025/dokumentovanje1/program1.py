class Calculator:
    """
    klasa kalkulator sadrzi metode osnovni aritmeticki operacija
    """
    def __init__(self, a, b):
        """
        konstruktor klase  Calculator
        
        :param self: objekat
        :param a: prvi operand
        :param b: drugi operand
        """
        self.a = a
        self.b = b

    def saberi(self):
        """
        metod za sabiranje
        
        :return:
            zbir
        :rtype: int
        """
        return self.a + self.b
    
    def oduzmi(self):
        return self.a - self.b
    
    def pomnozi(self):
        return self.a * self.b
    
    def podjeli(self):
        return self.a / self.b