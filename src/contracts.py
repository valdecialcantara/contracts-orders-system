# src/contracts.py

class Contracts:
    # Classe para gerenciar operações com contratos.
    
    def get_top_N_open_contracts(self, open_contracts, renegotiated_contracts, top_n):
        # Retorna os top N contratos abertos com maior débito, excluindo aqueles que foram renegociados.
        
        # Validação de entrada
        if not open_contracts:
            return []
        
        if top_n <= 0:
            return []
        
        # Converter lista de IDs renegociados para set para busca mais eficiente
        renegotiated_ids = set(renegotiated_contracts) if renegotiated_contracts else set()
        
        # Filtrar contratos abertos que não foram renegociados
        valid_contracts = [
            contract for contract in open_contracts 
            if contract.id not in renegotiated_ids
        ]
        
        # Ordenar por débito em ordem decrescente
        valid_contracts.sort(key=lambda contract: contract.debt, reverse=True)
        
        # Retornar os top N
        return valid_contracts[:top_n]