# Exercício 01 — Classificação de carga em cabos de aço

## Contexto

Em projetos de engenharia estrutural e mecânica, cabos de aço são utilizados para sustentar cargas em pontes, guindastes, elevadores e estruturas de içamento. Cada cabo tem uma capacidade máxima de carga, chamada de **carga de ruptura**, que depende do diâmetro do cabo e do material.

A **tensão mecânica** aplicada ao cabo é calculada pela força que ele suporta dividida pela área da seção transversal. Quanto mais próxima a tensão aplicada estiver da tensão de ruptura do material, maior o risco de falha.

Neste exercício você vai calcular a tensão aplicada em um cabo e classificar o nível de risco operacional.

---

## Dados do problema

Um cabo de aço com diâmetro de **12 mm** sustenta uma carga de **8.500 N**. O aço utilizado tem tensão de ruptura de **400 MPa**.

Use os seguintes valores no seu notebook:

```
diametro_mm = 12        # diâmetro do cabo em milímetros
carga_N = 8500          # força aplicada em Newtons
tensao_ruptura_MPa = 400  # tensão de ruptura do material em MPa
```

---

## Fórmulas necessárias

**Área da seção transversal circular:**

```
A = π * (d / 2)²
```

Onde `d` é o diâmetro em metros. Converta o diâmetro de mm para m antes de calcular.

**Tensão aplicada:**

```
σ = F / A
```

O resultado estará em Pa. Converta para MPa dividindo por 1.000.000.

**Fator de utilização:**

```
fator = σ_MPa / tensao_ruptura_MPa
```

O fator de utilização indica qual fração da capacidade máxima está sendo usada.

---

## Classificação do risco

Com base no fator de utilização, classifique o cabo conforme a tabela abaixo:

| Fator de utilização | Classificação |
|---------------------|---------------|
| Menor que 0,50 | Operação segura |
| Entre 0,50 e 0,74 | Atenção — verificar periodicamente |
| Entre 0,75 e 0,89 | Risco elevado — substituição recomendada |
| 0,90 ou maior | Perigo — cabo fora de operação |

---

## Estrutura do notebook

Monte seu notebook no Colab com as células na seguinte ordem:

**Célula 1 — Markdown**
Título do exercício e seu nome completo.

**Célula 2 — Markdown**
Breve descrição do problema com suas próprias palavras. Não copie o enunciado. Duas a quatro linhas explicando o que o programa vai fazer.

**Célula 3 — Código: dados de entrada**
Declare as variáveis com os valores fornecidos no enunciado. Comente cada linha indicando o que a variável representa e sua unidade.

**Célula 4 — Código: cálculo da área e da tensão**
Calcule a área da seção transversal e a tensão aplicada. Use a biblioteca `math` para o valor de π. Converta as unidades conforme necessário. Imprima os resultados intermediários com suas unidades.

**Célula 5 — Código: fator de utilização e classificação**
Calcule o fator de utilização e aplique a estrutura if/elif/else para determinar a classificação do cabo. Armazene a classificação em uma variável.

**Célula 6 — Código: saída final**
Imprima um relatório formatado com todos os resultados: diâmetro, carga, área calculada, tensão aplicada, fator de utilização e classificação. Use f-strings e apresente os valores numéricos com duas casas decimais.

**Célula 7 — Markdown**
Interpretação do resultado. Responda em texto: o cabo está em condição segura de operação? O que você recomendaria ao engenheiro responsável? Mínimo de três linhas.

---

## Saída esperada

Ao executar todas as células, o relatório final deve ter um formato semelhante a este:

```
=== RELATÓRIO DE ANÁLISE DE CABO ===
Diâmetro:            12.00 mm
Carga aplicada:      8500.00 N
Área da seção:       0.000113 m²
Tensão aplicada:     75.23 MPa
Fator de utilização: 0.19
Classificação:       Operação segura
=====================================
```

Os valores acima são apenas ilustrativos para mostrar o formato. Os valores corretos devem ser calculados pelo seu código.

---

## Entrega

Salve o arquivo como:

```
ex01-classificacao-cabos-nome-sobrenome.ipynb, dentro da pasta entregas
```

E coloque na sua pasta de entrega conforme descrito no README da tarefa.