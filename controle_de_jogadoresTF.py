'''
    A idéia desse arquivo é implementar o controle de jogadores
    de um jogo simples chamado towerfall

    O jogo tem 4 jogadores, no máximo.

    Assim, vamos representar ele por uma classe, que tenha a capacidade de
    guardar um nome de jogador (uma string) em uma posicao (1,2,3 ou 4)

    Primeiramente, implementei os métodos de adicionar, remover e consultar jogador.

    Depois, criei o método de trocar os jogadores, ou seja, trocar as posições deles.

    Então, implementei os erros (exception), para isso, usei classes.
'''

class PosicaoOcupadaException(Exception):
    pass

class PosicaoDesocupadaException(Exception):
    pass

class PosicaoInexistenteException(Exception):
    pass

'''
    Caso o usuário tente adicionar, remover ou trocar jogadores para uma
    posição invalida (lembramos que as unicas posições possiveis são 1,2,3 e 4)
    o programa irá restornar um exception (posicaoInexistenteException)

    Se tentar trocar ou remover um jogador de uma posição inexistente, será 
    retornado "PosiçãoDescoupadaException"

    Por fim, se tentar adicionar um jogador a uma posição que ja está ocupada 
    receberá o erro PosicaoOcupadaException
'''

from logging import exception


class Towerfall():
    def __init__(self):
        self.players={}

    def posicao_desocupada(self,n):             #Essa função verifica se a posição está desocupada
        if n not in self.players.keys():                                     
            raise PosicaoDesocupadaException('Esta posição está vazia.')
        else:pass

    def posicao_ocupada(self, n):               #Essa função verifica se a posição está ocupada.
        if n in self.players.keys():
            raise PosicaoOcupadaException(f'posicao {n} ocupada')
        else:pass

    def posicao_invalida(self,n):               #Essa função verifica se o número é valido
        if n >=1 and n<=4:                      
            pass
        else:
            raise PosicaoInexistenteException(f'Essa posição não existe.')
            
    def jogador(self, position):
        self.posicao_invalida(position)
        self.posicao_desocupada(position)

        return f'{self.players[position]} (player {position})'

    def adicionar(self, name, position):
        self.posicao_invalida(position)         # <--- Verifica se a posição do numero é valida.
        self.posicao_ocupada(position)          # <--- Verifica se a posição ja esta ocupada.

        self.players[position]= name
    
    def trocar(self, position1, position2):
        self.posicao_invalida(position1)        # <--- Verifica se as posições 1 e 2 são válidas.
        self.posicao_invalida(position2)        

        self.posicao_desocupada(position1)      # <--- Verifica se as posições 1 e 2 estão desocupadas.
        self.posicao_desocupada(position2)

        troca = self.players[position1]                 
        self.players[position1] = self.players[position2]       #Este bloco faz a troca de posições
        self.players[position2] = troca 

    def remover(self, position):
        self.posicao_invalida(position)         # <--- Verifica se a posição do numero é valida.
        self.posicao_desocupada(position)       # <--- Aqui verificamos se as posições estão desocupadas.
                                                
        self.players.pop(position)

    #Gustavo Lucas dos Santos