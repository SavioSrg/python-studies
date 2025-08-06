class Pessoa:
    
    def __init__(self, name, age, res):
        
        #inicializar os atributos da classe
        self.nome = name
        self.idade = age
        self.residencia = res
        
        #inicializar alguns atributos cujo valores são fixados
        self.num_filhos = 0
        self.profissao = None
        
    def fala(self, mensagem):
        print(f"{self.nome} diz: '{mensagem}'")
        
    def consegue_emprego(self, prof, valor_salario):
        self.profissao = prof
        self.salario = valor_salario
    
    def aumenta_salario(self, porcentagem):
        '''
        porcentagem: float entre 0 e 1, indicando o percentual de aumento de salario
        '''
        self.salario = self.salario*(1 + porcentagem)

joao = Pessoa("João", 20, "SP")
maria = Pessoa(name="Maria", age=18, res="Paris")

vars(joao)
vars(maria)

maria.fala("Obrigado")


class Horario:
    def __init__(self, hora, min, seg):
        
        self.h = hora
        self.m = min
        self.s = seg
        
        agora = Horario(15, 12, 30)
        vars(agora)