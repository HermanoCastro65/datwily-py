# datwily

**datwily** é uma biblioteca Python para preparação, limpeza e exploração inicial de dados.

O objetivo é simplificar tarefas comuns de pré-processamento antes de análise de dados ou Machine Learning, sem precisar trabalhar diretamente com o pandas o tempo todo.

---

## Instalação (modo desenvolvimento)

Clone o repositório:

```
git clone https://github.com/SEU-USUARIO/datwily-py.git
cd datwily-py
```

Crie o ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

Instale a biblioteca:

```
pip install -e .
```

---

## Uso básico

```python
from datwily import Dataset

data = Dataset("clientes.csv")

print(data.shape)
print(data.rows)
```

Você também pode usar um DataFrame diretamente:

```python
import pandas as pd
from datwily import Dataset

df = pd.read_csv("clientes.csv")
data = Dataset(df)
```

---

# Funcionalidades

---

## Informações básicas

| Propriedade | Descrição            |
| ----------- | -------------------- |
| data.shape  | (linhas, colunas)    |
| data.rows   | quantidade de linhas |

---

## Seleção de colunas

Manter apenas colunas específicas:

```python
data.select(["name", "age"])
```

Remover colunas:

```python
data.drop(["salary"])
```

---

## Tratamento de valores ausentes

Quantidade total:

```python
data.missing.count()
```

Relatório por coluna:

```python
data.missing.report()
```

Remover linhas com valores ausentes:

```python
data.missing.drop_rows()
```

Preencher com média:

```python
data.missing.fill_mean("age")
```

Preencher com valor fixo:

```python
data.missing.fill_value("city", "Unknown")
```

---

## Normalização de nomes de colunas

```python
data.columns.normalize()
```

Exemplo:

```
"Full Name" -> full_name
"E-mail@Cliente" -> email_cliente
"Cidade/Estado" -> cidade_estado
```

---

## Detecção de outliers

Detectar valores extremos:

```python
data.outliers.detect("age")
```

Remover outliers:

```python
data.outliers.remove("age")
```

---

## Encoding categórico (One-Hot)

Transformar texto em colunas binárias:

```python
data.encode.one_hot("city")
```

---

## Escalonamento numérico

Normalização Min-Max (0 a 1):

```python
data.scale.minmax("salary")
```

---

## Estatísticas descritivas

Resumo estatístico de colunas numéricas:

```python
report = data.describe()

print(report["age"]["mean"])
print(report["salary"]["max"])
```

---

## Rodar testes

```
python -m pytest
```

---

## Objetivo do projeto

O `datwily` não pretende substituir o pandas.
Ele funciona como uma camada de preparação de dados mais simples e organizada para:

* limpeza de dados
* análise exploratória inicial
* pré-processamento para Machine Learning

---

## Status

Projeto em desenvolvimento (v0.1.0)
