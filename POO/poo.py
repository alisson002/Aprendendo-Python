class Computador():
    #propriedades da classe
    # marca = 'Samsung'
    # processador = 'intel'
    # usb = 3
    # ligado
    
    #NO PYTHON NÃO TEM DESTRUTOR
    def __init__(self):#construtor
        #o ideal é que as prorpiedade sejam definidas aqui
        self.ligado = False
        self.marca = 'Samsung'
        self.processador = 'intel'
        self.usb = 3
    
    
    #metodo, vai mudar caracteristicas da classe
    def ligar_computador(self):#todo objeto que tem uma caracteristica interna da classe, deve ser referenciado como self
        #self referencia as variaveis internas da classe
        self.ligado = True
    
    def mudar_marca(self, marca):#SET: set_marca
        self.marca = marca
        
    #o ideal é que não se tenha um acesso direto as propriedades
    def obter_marca(self):#GET: get_marca
        return self.marca
        

pc = Computador()#para instanciar a classe

print(pc.marca)
print(pc.processador)
print(pc.ligado)
pc.ligar_computador()
print(pc.ligado)

pc.mudar_marca('waio')
print(pc.marca)#isso aqui seria um acesso direto

print(pc.obter_marca())

#herança, classe filha
class Notebook(Computador):
    pass
print('herança'.upper())
pc2 = Notebook()#instanciar
print(pc2.obter_marca())#retorna samsung, ja que na herança são herdadas as propriedades/variaveis default da classe pai

#herança, classe filha
class Notebook2(Computador):
    #NO PYTHON NÃO TEM DESTRUTOR
    def __init__(self):#construtor
        #o ideal é que as prorpiedade sejam definidas aqui
        self.ligado = False
        self.marca = 'dell'
        self.processador = 'intel'
        self.usb = 3
        self.horas_ligado = 100#msm sendo uma classe filha eu posso criar novas prorpiedades nela

print('herança2'.upper())
pc3 = Notebook2()#instanciar
print(pc3.obter_marca())#retorna dell, ja que nesse caso eu fiz uma sobre carga do construtor
