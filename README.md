# Sistema de Gerenciamento de Contratos e Pedidos

Este projeto implementa um sistema para gerenciar contratos e pedidos, fornecendo funcionalidades para identificar contratos com os maiores débitos e otimizar o agrupamento de pedidos.

## 📋 Índice

- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Classes](#classes)
- [Instalação](#instalação)
- [Uso](#uso)
- [Exemplos](#exemplos)
- [Testes](#testes)
- [Contribuição](#contribuição)

## 🎯 Visão Geral

O sistema é composto por três classes principais:

- **Contract**: Representa um contrato individual com ID e débito
- **Contracts**: Gerencia operações com múltiplos contratos
- **Orders**: Gerencia operações de agrupamento de pedidos

## 📁 Estrutura do Projeto

```
projeto/
├── contract.py          # Classe Contract
├── contracts.py         # Classe Contracts
├── orders.py           # Classe Orders
├── main.py             # Arquivo de teste principal
└── README.md           # Documentação
```

## 🔧 Classes

### Contract

Classe base que representa um contrato individual.

**Atributos:**
- `id`: Identificador único do contrato
- `debt`: Valor do débito do contrato

**Métodos:**
- `__init__(id, debt)`: Inicializa o contrato
- `__str__()`: Retorna representação string do contrato
- `__repr__()`: Retorna representação para debug

### Contracts

Classe para gerenciar operações com múltiplos contratos.

**Métodos:**
- `get_top_N_open_contracts(open_contracts, renegotiated_contracts, top_n)`: Retorna os top N contratos com maior débito, excluindo os renegociados

**Parâmetros:**
- `open_contracts`: Lista de objetos Contract
- `renegotiated_contracts`: Lista de IDs de contratos renegociados
- `top_n`: Número de contratos a retornar

**Retorno:**
- Lista dos top N contratos ordenados por débito (decrescente)

**Complexidade:** O(n log n)

### Orders

Classe para gerenciar operações de agrupamento de pedidos.

**Métodos:**
- `combine_orders(requests, n_max)`: Combina pedidos em grupos otimizados

**Parâmetros:**
- `requests`: Lista de valores/quantidades dos pedidos
- `n_max`: Valor máximo que um grupo pode ter

**Retorno:**
- Lista de listas, onde cada sublista é um grupo de pedidos

**Algoritmo:** First Fit Decreasing  
**Complexidade:** O(n² m) onde n = número de pedidos, m = número de grupos

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/valdecialcantara/contracts-orders-system.git
cd contracts-orders-system
```

2. Certifique-se de ter Python 3.6+ instalado:
```bash
python --version
```

3. Não são necessárias dependências externas - o projeto usa apenas a biblioteca padrão do Python.

## 💡 Uso

### Importação das Classes

```python
from contract import Contract
from contracts import Contracts
from orders import Orders
```

### Uso Básico

#### Trabalhando com Contratos

```python
# Criar contratos
contract1 = Contract(1, 1000)
contract2 = Contract(2, 2500)
contract3 = Contract(3, 1500)

# Gerenciar contratos
contracts_manager = Contracts()
open_contracts = [contract1, contract2, contract3]
renegotiated_ids = [2]  # Contract 2 foi renegociado

# Obter top 2 contratos (excluindo renegociados)
top_contracts = contracts_manager.get_top_N_open_contracts(
    open_contracts, renegotiated_ids, 2
)

for contract in top_contracts:
    print(contract)
```

#### Trabalhando com Pedidos

```python
# Gerenciar pedidos
orders_manager = Orders()
requests = [100, 200, 150, 300, 50, 250]
max_group_size = 400

# Combinar pedidos em grupos
groups = orders_manager.combine_orders(requests, max_group_size)

print(f"Grupos formados: {groups}")
print(f"Somas dos grupos: {[sum(group) for group in groups]}")
```

## 📊 Exemplos

### Exemplo 1: Contratos com Maior Débito

```python
from contract import Contract
from contracts import Contracts

# Criar contratos
contracts_list = [
    Contract(1, 1000),
    Contract(2, 2500),
    Contract(3, 1500),
    Contract(4, 3000),
    Contract(5, 800)
]

# IDs dos contratos renegociados
renegotiated = [2, 5]

# Obter top 3 contratos
manager = Contracts()
top_3 = manager.get_top_N_open_contracts(contracts_list, renegotiated, 3)

# Resultado: [Contract(4, 3000), Contract(3, 1500), Contract(1, 1000)]
```

### Exemplo 2: Otimização de Pedidos

```python
from orders import Orders

# Pedidos a serem agrupados
requests = [100, 200, 150, 300, 50, 250]
limit = 400

# Agrupar pedidos
manager = Orders()
groups = manager.combine_orders(requests, limit)

# Resultado possível: [[300, 50], [250, 150], [200, 100]]
```

## 🧪 Testes

Execute os testes completos:

```bash
python main.py
```

Execute os testes unitários:

```bash
pytest
```
Resultado esperado:
rootdir: /home/valdeci/Projetos/contracts-orders-system collected 48 items       
tests/test_contract py .............      [ 27%]
tests/test_contracts.py ...............   [ 58%]
tests/test_integration.py ..              [ 62%]
tests/test_orders.py ..................   [100%]

### Cenários de Teste

O arquivo `main.py` inclui testes para:

**Contracts:**
- Filtragem de contratos renegociados
- Ordenação por débito
- Casos limite (lista vazia, top_n = 0, todos renegociados)

**Orders:**
- Agrupamento otimizado de pedidos
- Pedidos que excedem o limite
- Casos limite (lista vazia, n_max = 0, todos excedem)

### Exemplo de Saída

```
=== Teste Contracts ===
Contratos abertos:
  id=1, debt=1000
  id=2, debt=2500
  id=3, debt=1500
  id=4, debt=3000
  id=5, debt=800
  id=6, debt=2000

Contratos renegociados (IDs): [2, 5]

Top 3 contratos abertos (excluindo renegociados):
  id=4, debt=3000
  id=6, debt=2000
  id=3, debt=1500

=== Teste Orders ===
Teste 1:
  Pedidos: [100, 200, 150, 300, 50, 250]
  Limite máximo: 400
  Grupos formados: [[300, 50], [250, 150], [200, 100]]
  Somas dos grupos: [350, 400, 300]
```

## 🔍 Detalhes Técnicos

### Algoritmos Utilizados

**Contracts.get_top_N_open_contracts:**
- Filtragem usando set para O(1) lookup
- Ordenação por débito usando Timsort
- Complexidade total: O(n log n)

**Orders.combine_orders:**
- First Fit Decreasing (FFD) algorithm
- Ordena pedidos em ordem decrescente
- Tenta encaixar cada pedido no primeiro grupo disponível
- Complexidade: O(n² m)

### Tratamento de Casos Limite

- **Listas vazias**: Retorna lista vazia
- **Parâmetros inválidos**: Validação de entrada
- **Valores que excedem limites**: Tratamento especial
- **Casos extremos**: Todos os contratos renegociados, etc.

## 📞 Contato

- E-mail: valdeci.alcantara@gmail.com
Para dúvidas ou sugestões, entre em contato através dos issues do GitHub.