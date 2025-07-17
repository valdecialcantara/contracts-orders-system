# src/main.py
# Arquivo principal para testar as classes Contract, Contracts e Orders.

from contract import Contract
from contracts import Contracts
from orders import Orders


def test_contracts():
    # Testa a funcionalidade da classe Contracts.

    print("=== Teste Contracts ===")
    contracts = Contracts()
    
    # Criar contratos de exemplo
    open_contracts = [
        Contract(1, 1000),
        Contract(2, 2500),
        Contract(3, 1500),
        Contract(4, 3000),
        Contract(5, 800),
        Contract(6, 2000)
    ]
    
    renegotiated_contracts = [2, 5]  # IDs dos contratos renegociados
    top_3 = contracts.get_top_N_open_contracts(open_contracts, renegotiated_contracts, 3)
    
    print("Contratos abertos:")
    for contract in open_contracts:
        print(f"  {contract}")
    
    print(f"\nContratos renegociados (IDs): {renegotiated_contracts}")
    print(f"\nTop 3 contratos abertos (excluindo renegociados):")
    for contract in top_3:
        print(f"  {contract}")
    
    # Teste com casos limite
    print("\n--- Testes de casos limite ---")
    
    # Lista vazia
    result_empty = contracts.get_top_N_open_contracts([], [], 3)
    print(f"Lista vazia: {result_empty}")
    
    # Top_n = 0
    result_zero = contracts.get_top_N_open_contracts(open_contracts, [], 0)
    print(f"Top_n = 0: {result_zero}")
    
    # Todos os contratos renegociados
    all_renegotiated = [1, 2, 3, 4, 5, 6]
    result_all_renegotiated = contracts.get_top_N_open_contracts(
        open_contracts, all_renegotiated, 3
    )
    print(f"Todos renegociados: {result_all_renegotiated}")


def test_orders():
    # Testa a funcionalidade da classe Orders.
    
    print("\n=== Teste Orders ===")
    orders = Orders()
    
    # Teste 1: Pedidos normais
    requests1 = [100, 200, 150, 300, 50, 250]
    n_max1 = 400
    result1 = orders.combine_orders(requests1, n_max1)
    
    print(f"Teste 1:")
    print(f"  Pedidos: {requests1}")
    print(f"  Limite máximo: {n_max1}")
    print(f"  Grupos formados: {result1}")
    print(f"  Somas dos grupos: {[sum(group) for group in result1]}")
    
    # Teste 2: Pedidos com valores que excedem o limite
    requests2 = [500, 100, 200, 600, 150]
    n_max2 = 400
    result2 = orders.combine_orders(requests2, n_max2)
    
    print(f"\nTeste 2:")
    print(f"  Pedidos: {requests2}")
    print(f"  Limite máximo: {n_max2}")
    print(f"  Grupos formados: {result2}")
    print(f"  Somas dos grupos: {[sum(group) for group in result2]}")
    
    # Teste 3: Casos limite
    print(f"\n--- Testes de casos limite ---")
    
    # Lista vazia
    result_empty = orders.combine_orders([], 100)
    print(f"Lista vazia: {result_empty}")
    
    # N_max = 0
    result_zero_max = orders.combine_orders([10, 20, 30], 0)
    print(f"N_max = 0: {result_zero_max}")
    
    # Todos os pedidos excedem o limite
    result_all_exceed = orders.combine_orders([500, 600, 700], 400)
    print(f"Todos excedem limite: {result_all_exceed}")


def main():
    # Função principal para executar todos os testes.

    print("Iniciando testes das classes Contract, Contracts e Orders\n")
    
    test_contracts()
    test_orders()
    
    print("\n=== Testes concluídos ===")


if __name__ == "__main__":
    main()