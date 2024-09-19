
class Conta:
    def __init__(self, numero_conta: int, agencia : str) -> None:
        self._numero_conta = numero_conta
        self._agencia = agencia
        self._saldo = 0

    def sacar (self, valor):
       self._saldo -= valor

    def depositar(self, valor) : 
        self._saldo += valor 

    def set_deposito(self, valor):
        if valor < 0:
           self._saldo = 0 
        else :
            self._saldo += valor