'''
leia do teclado as dimensões de um retângulo (base e altura),
calcular e escrever a área do retângulo.
(Valores inválidos: 0 e números negativos).

'''


class Retangulo:
    """
    Cria um retangulo com base e altura informada pelo usuario
    """
    def __init__(self):
        self.base = -1
        self.altura = -1

    def set_base(self):
        """
        Solicita valor float da base e altura de um retangulo
        """
        while self.base <= 0:
            self.base = float(input('Insira um valor para a base do retangulo: \n'))
            if self.base <= 0:
                print('Valor inválido, não use 0 e números negativos.')

        while self.altura <= 0:
            self.altura = float(input('Insira um valor para a altura do retangulo: \n'))
            if self.altura <= 0:
                print('Valor inválido, não use 0 e números negativos.')

    def get_base(self):
        return self.base

    def get_altura(self):
        return self.altura

    def calcular_area(self):
        """
        Calcula o valor da area de um retangulo
        :return: Base X Altura
        """
        area = self.base * self.altura
        return area


r = Retangulo()
r.set_base()
print(f'Area do retangulo é {r.calcular_area()}.')
