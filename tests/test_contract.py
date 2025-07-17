# Testes unitários para a classe Contract.

import pytest

from src.contract import Contract

class TestContract:
    
    def test_init_valid_parameters(self):
        # Testa inicialização com parâmetros válidos.
        contract = Contract(1, 1000)
        assert contract.id == 1
        assert contract.debt == 1000
    
    def test_init_zero_debt(self):
        # Testa inicialização com débito zero.
        contract = Contract(1, 0)
        assert contract.id == 1
        assert contract.debt == 0
    
    def test_init_negative_debt(self):
        # Testa inicialização com débito negativo.
        contract = Contract(1, -500)
        assert contract.id == 1
        assert contract.debt == -500
    
    def test_init_string_id(self):
        # Testa inicialização com ID string.
        contract = Contract("ABC123", 1000)
        assert contract.id == "ABC123"
        assert contract.debt == 1000
    
    def test_init_float_debt(self):
        # Testa inicialização com débito float.
        contract = Contract(1, 1000.50)
        assert contract.id == 1
        assert contract.debt == 1000.50
    
    def test_str_representation(self):
        # Testa representação string do contrato.
        contract = Contract(1, 1000)
        expected = 'id=1, debt=1000'
        assert str(contract) == expected
    
    def test_str_representation_string_id(self):
        # Testa representação string com ID string.
        contract = Contract("ABC123", 1500.75)
        expected = 'id=ABC123, debt=1500.75'
        assert str(contract) == expected
    
    def test_str_representation_negative_debt(self):
        # Testa representação string com débito negativo.
        contract = Contract(1, -500)
        expected = 'id=1, debt=-500'
        assert str(contract) == expected
    
    def test_repr_representation(self):
        # Testa representação repr do contrato.
        contract = Contract(1, 1000)
        expected = 'Contract(id=1, debt=1000)'
        assert repr(contract) == expected
    
    def test_repr_representation_string_id(self):
        # Testa representação repr com ID string.
        contract = Contract("ABC123", 1500.75)
        expected = 'Contract(id=ABC123, debt=1500.75)'
        assert repr(contract) == expected
    
    def test_attribute_modification(self):
        # Testa modificação de atributos após inicialização.
        contract = Contract(1, 1000)
        contract.id = 2
        contract.debt = 2000
        assert contract.id == 2
        assert contract.debt == 2000
    
    def test_equality_by_attributes(self):
        # Testa comparação de contratos por atributos.
        contract1 = Contract(1, 1000)
        contract2 = Contract(1, 1000)

        # Estes são objetos diferentes, então não são iguais
        assert contract1 is not contract2
        assert contract1.id == contract2.id
        assert contract1.debt == contract2.debt
    
    def test_different_types_parameters(self):
        # Testa com diferentes tipos de parâmetros.
        # ID None
        contract1 = Contract(None, 1000)
        assert contract1.id is None
        assert contract1.debt == 1000
        
        # Debt None
        contract2 = Contract(1, None)
        assert contract2.id == 1
        assert contract2.debt is None
        
        # Ambos None
        contract3 = Contract(None, None)
        assert contract3.id is None
        assert contract3.debt is None