# Testes de integração para as classes Contract, Contracts e Orders.

import pytest
from src.contract import Contract
from src.contracts import Contracts
from src.orders import Orders

class TestIntegration:
    
    def setup_method(self):
        # Setup executado antes de cada teste.
        self.contracts_manager = Contracts()
        self.orders_manager = Orders()
    
    def test_contract_contracts_integration(self):
        # Testa integração entre Contract e Contracts.
        # Criar contratos com diferentes tipos de dados.
        contracts_list = [
            Contract(1, 1000),
            Contract("ABC", 2500.50),
            Contract(3, 0),
            Contract("XYZ", -500),
            Contract(5, 3000)
        ]
        
        renegotiated = [3, "ABC"]
        
        result = self.contracts_manager.get_top_N_open_contracts(
            contracts_list, renegotiated, 3
        )
        
        # Verificar se os contratos retornados são objetos Contract válidos.
        assert len(result) == 3
        for contract in result:
            assert isinstance(contract, Contract)
            assert hasattr(contract, 'id')
            assert hasattr(contract, 'debt')
            assert hasattr(contract, '__str__')
            assert hasattr(contract, '__repr__')
        
        # Verificar ordenação correta
        assert result[0].debt == 3000  # Maior débito
        assert result[1].debt == 1000  # Segundo maior
        assert result[2].debt == -500  # Terceiro maior
    
    
    def test_orders_with_contract_debts(self):
        # Testa Orders usando débitos de contratos como pedidos.
        # Cenário: Usar débitos de contratos como valores de pedidos.
        contracts_list = [
            Contract(1, 1000),
            Contract(2, 2500),
            Contract(3, 1500),
            Contract(4, 3000),
            Contract(5, 800),
            Contract(6, 2000)
        ]
        
        # Extrair débitos para usar como pedidos.
        debts = [contract.debt for contract in contracts_list]
        
        # Agrupar débitos com limite máximo.
        max_group_value = 4000
        grouped_debts = self.orders_manager.combine_orders(debts, max_group_value)
        
        # Verificações
        assert len(grouped_debts) > 0
        
        # Verificar que todos os débitos foram incluídos.
        all_debts_in_groups = []
        for group in grouped_debts:
            all_debts_in_groups.extend(group)
        
        assert sorted(all_debts_in_groups) == sorted(debts)
        
        # Verificar que nenhum grupo excede o limite.
        for group in grouped_debts:
            assert sum(group) <= max_group_value
    