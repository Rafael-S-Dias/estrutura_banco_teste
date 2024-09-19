import pytest
from banco.models.conta import Conta

@pytest.fixture
def conta_valida():
    conta = Conta(222, 8888)
    return conta

def test_numero_conta_valida(conta_valida):
    assert conta_valida._numero_conta == 222

def test_agencia_valida(conta_valida):
    assert conta_valida._agencia == 8888

def test_saldo_inicial_zero(conta_valida):
    assert conta_valida._saldo == 0

def test_depositar_valor_negativo(conta_valida):
    conta_valida.set_deposito(-100)
    assert conta_valida._saldo == 0