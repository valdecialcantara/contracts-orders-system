# Testes unitários para a classe Orders.

import pytest
from src.orders import Orders

class TestOrders:
    
    def setup_method(self):
        # Setup executado antes de cada teste.
        self.orders_manager = Orders()
    
    def test_combine_orders_basic_functionality(self):
        # Testa funcionalidade básica do método combine_orders.
        requests = [100, 200, 150, 300]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
    
    def test_combine_orders_empty_requests(self):
        # Testa com lista vazia de pedidos.
        result = self.orders_manager.combine_orders([], 400)
        assert result == []
    
    def test_combine_orders_zero_n_max(self):
        # Testa com n_max = 0.
        requests = [100, 200, 150]
        result = self.orders_manager.combine_orders(requests, 0)
        assert result == []
    
    def test_combine_orders_negative_n_max(self):
        # Testa com n_max negativo.
        requests = [100, 200, 150]
        result = self.orders_manager.combine_orders(requests, -100)
        assert result == []
    
    def test_combine_orders_single_request(self):
        # Testa com apenas um pedido.
        requests = [100]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        assert len(result) == 1
        assert result[0] == [100]
    
    def test_combine_orders_request_equals_n_max(self):
        #Testa com pedido igual ao limite máximo.
        requests = [400, 200, 100]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # O pedido de 400 deve estar sozinho em um grupo.
        assert [400] in result
    
    def test_combine_orders_request_exceeds_n_max(self):
        # Testa com pedidos que excedem o limite máximo.
        requests = [500, 200, 600, 100]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Pedidos que excedem o limite devem estar sozinhos.
        assert [500] in result
        assert [600] in result
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
    
    def test_combine_orders_all_requests_exceed_n_max(self):
        # Testa quando todos os pedidos excedem o limite.
        requests = [500, 600, 700]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Cada pedido deve estar em seu próprio grupo.
        assert len(result) == 3
        assert [500] in result
        assert [600] in result
        assert [700] in result
    
    def test_combine_orders_optimal_grouping(self):
        # Testa se o agrupamento é otimizado.
        requests = [100, 200, 300, 100]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar se o agrupamento é eficiente.
        # Com First Fit Decreasing, devemos ter:
        # [300, 100] = 400 e [200, 100] = 300
        assert len(result) == 2
        
        group_sums = [sum(group) for group in result]
        assert 400 in group_sums  # Grupo otimizado
        assert all(sum_val <= n_max for sum_val in group_sums)
    
    def test_combine_orders_identical_requests(self):
        # Testa com pedidos idênticos.
        requests = [100, 100, 100, 100]
        n_max = 300
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # Com pedidos de 100 e limite 300, cada grupo pode ter até 3 pedidos.
        # Espero 2 grupos: [100, 100, 100] e [100].
        assert len(result) == 2
        
        # Verificar que todos os pedidos foram incluídos.
        total_requests = sum(len(group) for group in result)
        assert total_requests == 4
    
    def test_combine_orders_zero_requests(self):
        # Testa com pedidos de valor zero.
        requests = [0, 100, 0, 200]
        n_max = 300
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
    
    def test_combine_orders_negative_requests(self):
        # Testa com pedidos negativos.
        requests = [-100, 200, -50, 300]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
    
    def test_combine_orders_large_number_of_requests(self):
        #Testa com grande número de pedidos.
        requests = [50] * 20  # 20 pedidos de 50
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # Com pedidos de 50 e limite 400, cada grupo pode ter até 8 pedidos.
        # Espero 3 grupos: [50*8], [50*8], [50*4]
        assert len(result) == 3
        
        # Verificar que todos os pedidos foram incluídos.
        total_requests = sum(len(group) for group in result)
        assert total_requests == 20
    
    def test_combine_orders_float_requests(self):
        # Testa com pedidos em formato float.
        requests = [100.5, 200.3, 150.7]
        n_max = 400.0
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os grupos respeitam o limite.
        for group in result:
            assert sum(group) <= n_max
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
    
    def test_combine_orders_preserves_original_list(self):
        # Testa que a lista original não é modificada.
        original_requests = [100, 200, 150, 300]
        requests = original_requests.copy()
        n_max = 400
        
        self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que a lista original não foi modificada
        assert requests == original_requests
    
    def test_combine_orders_deterministic_behavior(self):
        # Testa que o comportamento é determinístico.
        requests = [100, 200, 150, 300]
        n_max = 400
        
        result1 = self.orders_manager.combine_orders(requests, n_max)
        result2 = self.orders_manager.combine_orders(requests, n_max)
        
        # Deve produzir o mesmo resultado
        assert result1 == result2
    
    def test_combine_orders_edge_case_n_max_1(self):
        # Testa caso limite com n_max = 1.
        requests = [1, 1, 1, 2]
        n_max = 1
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Pedidos de 1 devem estar em grupos individuais.
        # Pedido de 2 deve estar sozinho (excede o limite).
        assert len(result) == 4
        assert [1] in result
        assert [2] in result
        
        # Contar quantos grupos têm [1].
        count_single_ones = sum(1 for group in result if group == [1])
        assert count_single_ones == 3
    
    def test_combine_orders_mixed_values(self):
        # Testa com valores mistos (inteiros, floats, zeros, negativos.
        requests = [100, 200.5, 0, -50, 150, 300]
        n_max = 400
        
        result = self.orders_manager.combine_orders(requests, n_max)
        
        # Verificar que todos os pedidos foram incluídos.
        all_requests_in_result = []
        for group in result:
            all_requests_in_result.extend(group)
        
        assert sorted(all_requests_in_result) == sorted(requests)
        
        # Verificar que grupos não ultrapassam o limite.
        for group in result:
            assert sum(group) <= n_max