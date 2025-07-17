# Testes unitários para a classe Contracts.

import pytest
from src.contract import Contract
from src.contracts import Contracts

class TestContracts:
    
    def setup_method(self):
        # Setup executado antes de cada teste.
        self.contracts_manager = Contracts()
        self.sample_contracts = [
            Contract(1, 1000),
            Contract(2, 2500),
            Contract(3, 1500),
            Contract(4, 3000),
            Contract(5, 800),
            Contract(6, 2000)
        ]
    
    def test_get_top_n_basic_functionality(self):
        # Testa funcionalidade básica do método get_top_N_open_contracts.
        renegotiated = [2, 5]
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, renegotiated, 3
        )
        
        assert len(result) == 3
        assert result[0].id == 4  # Maior débito: 3000
        assert result[1].id == 6  # Segundo maior: 2000
        assert result[2].id == 3  # Terceiro maior: 1500
        
        # Verificar que contratos renegociados não estão no resultado.
        result_ids = [contract.id for contract in result]
        assert 2 not in result_ids
        assert 5 not in result_ids
    
    def test_get_top_n_empty_open_contracts(self):
        # Testa com lista vazia de contratos abertos.
        result = self.contracts_manager.get_top_N_open_contracts([], [], 3)
        assert result == []
    
    def test_get_top_n_empty_renegotiated_contracts(self):
        # Testa com lista vazia de contratos renegociados.
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, [], 3
        )
        
        assert len(result) == 3
        assert result[0].id == 4  # 3000
        assert result[1].id == 2  # 2500
        assert result[2].id == 6  # 2000
    
    def test_get_top_n_none_renegotiated_contracts(self):
        # Testa com None como lista de contratos renegociados.
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, None, 3
        )
        
        assert len(result) == 3
        assert result[0].id == 4  # 3000
        assert result[1].id == 2  # 2500
        assert result[2].id == 6  # 2000
    
    def test_get_top_n_zero_top_n(self):
        # Testa com top_n = 0.
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, [], 0
        )
        assert result == []
    
    def test_get_top_n_negative_top_n(self):
        # Testa com top_n negativo.
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, [], -1
        )
        assert result == []
    
    def test_get_top_n_top_n_greater_than_available(self):
        # Testa com top_n maior que contratos disponíveis.
        renegotiated = [2, 5]  # Remove 2 contratos
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, renegotiated, 10
        )
        
        # Deve retornar apenas os 4 contratos disponíveis
        assert len(result) == 4
        assert result[0].id == 4  # 3000
        assert result[1].id == 6  # 2000
        assert result[2].id == 3  # 1500
        assert result[3].id == 1  # 1000
    
    def test_get_top_n_all_contracts_renegotiated(self):
        #Testa quando todos os contratos foram renegociados.
        all_ids = [1, 2, 3, 4, 5, 6]
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, all_ids, 3
        )
        assert result == []
    
    def test_get_top_n_single_contract(self):
        # Testa com apenas um contrato.
        single_contract = [Contract(1, 1000)]
        result = self.contracts_manager.get_top_N_open_contracts(
            single_contract, [], 1
        )
        
        assert len(result) == 1
        assert result[0].id == 1
        assert result[0].debt == 1000
    
    def test_get_top_n_contracts_with_same_debt(self):
        # Testa com contratos que têm o mesmo débito.
        same_debt_contracts = [
            Contract(1, 1000),
            Contract(2, 1000),
            Contract(3, 1000),
            Contract(4, 2000)
        ]
        
        result = self.contracts_manager.get_top_N_open_contracts(
            same_debt_contracts, [], 3
        )
        
        assert len(result) == 3
        assert result[0].id == 4  # 2000
        assert result[0].debt == 2000

        # Os outros dois podem estar em qualquer ordem (débito igual).
        remaining_ids = [result[1].id, result[2].id]
        assert all(contract_id in [1, 2, 3] for contract_id in remaining_ids)
    
    def test_get_top_n_contracts_with_zero_debt(self):
        # Testa com contratos que têm débito zero.
        zero_debt_contracts = [
            Contract(1, 0),
            Contract(2, 1000),
            Contract(3, 0)
        ]
        
        result = self.contracts_manager.get_top_N_open_contracts(
            zero_debt_contracts, [], 2
        )
        
        assert len(result) == 2
        assert result[0].id == 2
        assert result[0].debt == 1000

        # O segundo pode ser qualquer um com débito 0.
        assert result[1].debt == 0
    
    def test_get_top_n_contracts_with_negative_debt(self):
        # Testa com contratos que têm débito negativo.
        negative_debt_contracts = [
            Contract(1, -500),
            Contract(2, 1000),
            Contract(3, -1000)
        ]
        
        result = self.contracts_manager.get_top_N_open_contracts(
            negative_debt_contracts, [], 3
        )
        
        assert len(result) == 3
        assert result[0].id == 2  # 1000
        assert result[1].id == 1  # -500
        assert result[2].id == 3  # -1000
    
    def test_get_top_n_renegotiated_id_not_in_contracts(self):
        # Testa quando ID renegociado não existe nos contratos.
        renegotiated = [999, 1000]  # IDs que não existem
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, renegotiated, 3
        )
        
        # Deve retornar normalmente, ignorando IDs inexistentes.
        assert len(result) == 3
        assert result[0].id == 4  # 3000
        assert result[1].id == 2  # 2500
        assert result[2].id == 6  # 2000
    
    def test_get_top_n_mixed_renegotiated_ids(self):
        # Testa com mix de IDs renegociados válidos e inválidos.
        renegotiated = [2, 999, 5, 1000]  # 2 e 5 existem, 999 e 1000 não
        result = self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, renegotiated, 3
        )
        
        assert len(result) == 3
        assert result[0].id == 4  # 3000
        assert result[1].id == 6  # 2000
        assert result[2].id == 3  # 1500
        
        # Verificar que contratos renegociados não estão no resultado.
        result_ids = [contract.id for contract in result]
        assert 2 not in result_ids
        assert 5 not in result_ids
    
    def test_get_top_n_preserves_original_lists(self):
        #Testa que as listas originais não são modificadas.
        original_contracts = self.sample_contracts.copy()
        renegotiated = [2, 5]
        
        self.contracts_manager.get_top_N_open_contracts(
            self.sample_contracts, renegotiated, 3
        )
        
        # Verificar que a lista original não foi modificada.
        assert len(self.sample_contracts) == len(original_contracts)
        for i, contract in enumerate(self.sample_contracts):
            assert contract.id == original_contracts[i].id
            assert contract.debt == original_contracts[i].debt