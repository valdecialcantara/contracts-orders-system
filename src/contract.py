# src/contract.py
class Contract:
    # Classe que representa um contrato com ID e valor de débito.
    
    def __init__(self, id, debt):
        # Inicializa um contrato.
        
        self.id = id
        self.debt = debt
    
    def __str__(self):
        # Retorna uma representação string do contrato.
        
        return 'id={}, debt={}'.format(self.id, self.debt)
    
    def __repr__(self):
        # Retorna uma representação para debug.
        
        return f'Contract(id={self.id}, debt={self.debt})'