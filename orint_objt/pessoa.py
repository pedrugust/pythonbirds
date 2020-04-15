class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=30):
        self.idade = idade
        self.nome = nome
        self.filhos =  list(filhos)
    def cumprimentar(self):     # função de classe referente a objeto chama-se método
        return f'Olá {id(self)}'
    @staticmethod    # decorator
    def metodo_estatico():    # função de classe com decorator é um metodo de classe, indepennde do objeto
        return 50
    @classmethod    # acesso ao nome e aos atributos de classe
    def nome_atributos(cls):
        return f'{cls} - {cls.olhos}'
if __name__ == '__main__':
    p = Pessoa()
    b = Pessoa(p, nome='Barto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())     # nesse caso p já é automaticamente o 1° parametro
    print(p.cumprimentar(7))     # como está escrito eu estou passando 2 parametros ao metodo, mas ele não aceita 2 paramtros
    print(Pessoa.cumprimentar(p, 7))    # essa linha é uma tradução mais explicita do erro da linha de cima
    print(p.nome)
    p.nome = 'Pedrugust'
    print(p.nome)
    print(p.idade)
    print(b.filhos)
    for filho in b.filhos:
        print(filho.nome)
    b.sobrenome = 'Abel'
    print(b.__dict__)
    b.olhos = 1
    print(p.__dict__)
    del b.filhos
    print(b.__dict__)
    print(p.olhos)
    Pessoa.olhos = 3
    print(p.olhos)
    print(b.olhos)  # como objeto b recebeu um valor próprio para olhos, mesmo mudando o valor do atributo para a classe o seu fica
    print(Pessoa.olhos)
    print(Pessoa.metodo_estatico())     # não precisa de um objeto
    print(p.metodo_estatico())     # mas pode ser referenciado a um objeto
    print(p.nome_atributos(), Pessoa.nome_atributos())
