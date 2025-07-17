# src/orders.py
class Orders:
    #Classe para gerenciar operações com pedidos.
    
    def combine_orders(self, requests, n_max):
        # Combina pedidos em grupos otimizados respeitando o limite máximo.
        # Retorna Lista de listas, onde cada sublista representa um grupo de pedidos combinados
        
        # Validação de entrada
        if not requests:
            return []
        
        if n_max <= 0:
            return []
        
        # Ordenar pedidos em ordem decrescente para melhor aproveitamento
        requests_sorted = sorted(requests, reverse=True)
        groups = []
        
        for request in requests_sorted:
            # Se o pedido individual já excede o limite, criar grupo próprio
            if request > n_max:
                groups.append([request])
                continue
            
            # Tentar adicionar a um grupo existente
            added = False
            for group in groups:
                if sum(group) + request <= n_max:
                    group.append(request)
                    added = True
                    break
            
            # Se não foi possível adicionar a nenhum grupo, criar novo grupo
            if not added:
                groups.append([request])
        
        return groups