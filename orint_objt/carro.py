""" Cria classe carro que posseui dois atributos compostos por outras duas classes:
1-Motor: vai controlar a velocidade
a) atributo de dado de velocidade > Vo = 0
b) metodo acelerar > incrementa a velocidade em 1
c) metodo freiar > decrementa a velocidade em 2
2-Direção: controle do carro
a) atributo de valor de direção possivel: norte, sul, leste, oeste > do = norte          N
b) metodo girar_direita                                                                O   L
c) metodo girar_esquerda                                                                 S
"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1
                                                             # COMO EU FIZ FREAR()
    def frear(self):                                         # def frear(self):
        self.velocidade -= 2                                 #    if self.velocidade > 1:
        self.velocidade = max(0, self.velocidade)            #       self.velocidade-=2
                                                             #    elif self.velocidade == 1:
                                                             #        self.velocidade -= 1
                                                             #    else:
                                                             #        self.velocidade = 0

NORTE = 'N'  # Variaveis em caixa alta indicam que não devem ser mudadas
LESTE = 'L'  # criar variaveis fornece o alto complite(CRTL + ESPAÇO)
SUL = 'S'  # selecionar texto e CRTL + SHIFT + 'u' muda a caixa do texto
OESTE = 'O'
class Direcao:
    direita = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    esquerda = {NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL}
    def __init__(self):
        self.direcao = NORTE
    def girar_direita(self):
        self.direcao = self.direita[self.direcao]
    def girar_esquerda(self):
        self.direcao = self.esquerda[self.direcao]
class Carro:
    def __init__(self, direcao, mortor):    # ALT + ENTER cria atributos
        self.mortor = mortor
        self.direcao = direcao
    def velocidade(self):
        return self.velocidade
    def acelerar(self):
        return self.acelerar()
    def frear(self):
        return self.frear()
motor = Motor()
bmw = Motor()
gol = Direcao()
print(bmw.velocidade)
bmw.acelerar()
print(bmw.velocidade)
bmw.frear()
print(bmw.velocidade)
bmw.acelerar()
bmw.acelerar()
print(bmw.velocidade)
bmw.frear()
print(bmw.velocidade)
print(gol.direcao)
gol.girar_direita()
print(gol.direcao)
gol.girar_direita()
gol.girar_direita()
print(gol.direcao)
gol.girar_esquerda()
print(gol.direcao)
