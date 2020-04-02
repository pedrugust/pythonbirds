class Pessoa:
    def __init__(self, *filhos, nome = None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos =  list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    b = Pessoa(p, nome='Barto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Pedrugust'
    print(p.nome)
    print(p.idade)
    print(b.filhos)
    for filho in b.filhos:
        print(filho.nome)


