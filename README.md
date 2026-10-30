# ACME_FOCUS — Análise de Satisfação dos Funcionários

## 1. Sobre o projeto

O ACME_FOCUS é um projeto desenvolvido em Python com o objetivo de analisar dados de uma pesquisa de satisfação dos funcionários de uma empresa.

A aplicação lê um arquivo CSV, identifica a resposta mais recente de cada funcionário e gera indicadores estatísticos e um gráfico para facilitar a interpretação dos resultados.

## 2. Objetivos

- Ler e processar dados de um arquivo CSV.
- Identificar a resposta mais recente de cada funcionário.
- Contabilizar as notas de satisfação de 1 a 5.
- Calcular a média geral das avaliações.
- Calcular a porcentagem de cada nota.
- Apresentar os resultados em um gráfico de barras.

## 3. Tecnologias utilizadas

- Python 3
- Matplotlib
- Git
- GitHub
- Arquivo CSV

## 4. Estrutura do projeto

```text
ACME_FOCUS/
│
├── employee_satisfaction_survey.csv
├── lista.py
└── README.md
```

## 5. Como executar o projeto

### Passo 1 — Clonar o repositório

```bash
git clone https://github.com/MarcosJuniors/ACME_FOCUS.git
```

### Passo 2 — Entrar na pasta

```bash
cd ACME_FOCUS
```

### Passo 3 — Instalar a biblioteca Matplotlib

```bash
pip install matplotlib
```

### Passo 4 — Executar o programa

```bash
python lista.py
```

## 6. Funcionamento da aplicação

O programa realiza as seguintes etapas:

1. Abre o arquivo CSV e faz a leitura dos dados.
2. Separa as linhas e identifica os registros dos funcionários.
3. Utiliza o e-mail como identificador de cada funcionário.
4. Compara as datas para manter somente a resposta mais recente.
5. Soma as notas e contabiliza a quantidade de avaliações.
6. Calcula a média e as porcentagens de satisfação.
7. Gera um gráfico de barras utilizando Matplotlib.

## 7. Resultados esperados

Ao executar o programa, são apresentados:

- Quantidade de funcionários analisados.
- Soma das notas.
- Média geral de satisfação.
- Quantidade e percentual de cada nota.
- Gráfico de barras com a distribuição das avaliações.

## 8. Aprendizados

O desenvolvimento deste projeto permite praticar conceitos fundamentais de programação em Python, como:

- Manipulação de arquivos.
- Listas e dicionários.
- Estruturas de repetição.
- Condicionais.
- Variáveis acumuladoras.
- Processamento de dados.
- Visualização de informações.

## 9. Autor

Desenvolvido por **Marcos Junior**.

Projeto de estudo e prática de análise de dados com Python.
