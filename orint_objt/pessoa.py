class Pessoa:
    olhos = 2   # atirbuto de classe ou default(padrão). Valido a todos objetos. Econimia de memoria
    def __init__(self, *filhos, nome=None, idade=30):   # criação de um atributo de dado.   # variavel(nome) só nevessario-
        self.idade = idade                                                                  # -para tornar o atributo mutavel
        self.nome = nome    # self.nome(atributo de dado) != nome(variavel)
        self.filhos =  list(filhos)     # { ALT + ENTER constrói o atributo automaticamente a partir da variavel(vice-versa)
                                        # | é possivel inserir objetos em listas, como será inserido p em b
    def cumprimentar(self):     # função de classe referente a objeto chama-se método
        return f'Olá {id(self)}'
    @staticmethod    # decorator
    def metodo_estatico():    # função de classe com decorator é um metodo de classe, independe do objeto
        return 50
    @classmethod    # acesso a classe que está executando esse método
    def nome_atributos(cls):        # primeiro parametro(cls) será uma classe
        return f'{cls} - <{cls.olhos}>'     # pode-se acessar os atributos de classe(cls.olhos) pelo @classmethod
if __name__ == '__main__':
    p = Pessoa()
    b = Pessoa(p, nome='Barto')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())     # nesse caso p já é automaticamente o 1° parametro
#    print(p.cumprimentar(7))     # como está escrito eu estou passando 2 parametros ao metodo, mas ele não aceita 2 paramtros
 #   print(Pessoa.cumprimentar(p, 7))    # essa linha é uma tradução mais explicita do erro da linha de cima
    print(p.nome)   # acesso de um atributo de dado não requer () como o metodo
    p.nome = 'Pedrugust'
    print(p.nome)
    print(p.idade)
    print(b.filhos)
    for filho in b.filhos:
        print(filho.nome)
    b.sobrenome = 'Abel'    # atributo dinamico(não foi definido com __init__)
    print(b.__dict__)       # .__dict__ ferramenta mostra todos atributos de um objeto, inclusive os dinamicos, os de classe não
    b.olhos = 1             # atributo de classe torna-se dinamica para o objeto b
    print(p.__dict__)       # Pedrugust não tem sobrenome, pois este foi defido apenas para Barto
    del b.filhos            # remoção de atributos dinamicamente, pode ser aqueles dados por __init__ ou os de classe
    print(b.__dict__)
    print(p.olhos)
    Pessoa.olhos = 3
    print(p.olhos)
    print(b.olhos)  # como objeto b recebeu um valor próprio para olhos, mesmo mudando o valor do atributo para a classe o seu fica
    print(Pessoa.olhos)     # pode-se revelar o valor de atributo de classe diretamente pela classe(não precisa de um objeto)
    print(Pessoa.metodo_estatico())     # não precisa de um objeto
    print(p.metodo_estatico())     # mas pode ser referenciado a um objeto
    print(p.nome_atributos(), Pessoa.nome_atributos())
