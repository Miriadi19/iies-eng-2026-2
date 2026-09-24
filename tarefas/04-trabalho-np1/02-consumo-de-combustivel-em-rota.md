# Exercício 02 — Consumo de combustível em rota de transporte

## Contexto

No planejamento logístico e no dimensionamento de frotas, engenheiros precisam estimar o consumo de combustível de veículos em rotas com condições variadas. Uma rodovia raramente tem velocidade constante: há trechos urbanos, rodovias, subidas e descidas, congestionamentos e zonas de obra.

O consumo de um veículo não é fixo. Ele varia com a velocidade: em velocidades muito baixas o motor trabalha em marcha lenta e consome mais por quilômetro; em velocidades muito altas o arrasto aerodinâmico aumenta e o consumo também sobe. Existe uma faixa de velocidade mais econômica.

Neste exercício você vai calcular o consumo total de combustível de um caminhão em uma rota dividida em trechos, onde cada trecho tem uma extensão e uma velocidade média diferente.

---

## Dados do problema

Um caminhão percorre uma rota de entrega dividida em 5 trechos. Os dados de cada trecho estão nas listas abaixo:

```
extensoes_km = [42, 18, 65, 30, 25]        # distância de cada trecho em km
velocidades_kmh = [90, 40, 110, 60, 80]    # velocidade média em cada trecho em km/h
```

O consumo do caminhão varia conforme a velocidade média do trecho, seguindo a tabela abaixo:

| Velocidade média (km/h) | Consumo (litros por 100 km) |
|-------------------------|-----------------------------|
| Até 50 | 18,0 |
| Entre 51 e 80 | 14,5 |
| Entre 81 e 100 | 12,0 |
| Acima de 100 | 15,5 |

O consumo acima de 100 km/h volta a subir por conta do arrasto aerodinâmico.

---

## O que calcular

Para cada trecho, você deve:

1. Identificar o consumo em L/100km com base na velocidade do trecho
2. Calcular o consumo em litros naquele trecho
3. Calcular o tempo de viagem naquele trecho em horas
4. Acumular o consumo total e o tempo total da rota

Ao final, calcule também o custo total de combustível, considerando o preço do diesel:

```
preco_litro = 6.89   # preço do litro do diesel em reais
```

---

## Fórmulas necessárias

**Consumo em litros por trecho:**

```
consumo_trecho = (extensao_km * consumo_L_por_100km) / 100
```

**Tempo de viagem por trecho:**

```
tempo_trecho_h = extensao_km / velocidade_kmh
```

**Custo total:**

```
custo_total = consumo_total_litros * preco_litro
```

---

## Estrutura do notebook

Monte seu notebook no Colab com as células na seguinte ordem:

**Célula 1 — Markdown**
Título do exercício e seu nome completo.

**Célula 2 — Markdown**
Breve descrição do problema com suas próprias palavras. Duas a quatro linhas explicando o que o programa vai fazer.

**Célula 3 — Código: dados de entrada**
Declare todas as listas e variáveis fornecidas no enunciado. Comente cada linha indicando o que representa.

**Célula 4 — Código: loop de cálculo por trecho**
Use `for` com `range()` para percorrer os trechos. A cada iteração, determine o consumo do trecho com base na velocidade usando `if/elif/else`, calcule o consumo em litros e o tempo, e imprima os dados do trecho. Acumule o consumo total e o tempo total em variáveis.

**Célula 5 — Código: cálculo do custo**
Com o consumo total calculado, compute o custo total da rota.

**Célula 6 — Código: saída final**
Imprima um relatório com o resumo completo da rota: distância total percorrida, tempo total de viagem, consumo total em litros e custo total em reais. Use f-strings com duas casas decimais.

**Célula 7 — Markdown**
Interpretação do resultado. Responda em texto: qual trecho foi o mais caro em termos de consumo? Por que a velocidade mais alta nem sempre é a mais econômica? Mínimo de três linhas.

---

## Saída esperada

Durante o loop, imprima os dados de cada trecho em um formato semelhante a este:

```
Trecho 1: 42 km a 90 km/h | Consumo: 12,0 L/100km | Gasto: 5.04 L | Tempo: 0.47 h
Trecho 2: 18 km a 40 km/h | Consumo: 18,0 L/100km | Gasto: 3.24 L | Tempo: 0.45 h
...
```

E ao final, o relatório de resumo:

```
=== RELATÓRIO DE ROTA ===
Distância total:     180.00 km
Tempo total:         2.13 h
Consumo total:       XX.XX litros
Custo total:         R$ XXX.XX
=========================
```

Os valores marcados com XX devem ser calculados pelo seu código.

---

## Entrega

Salve o arquivo como:

```
ex02-consumo-combustivel-nome-sobrenome.ipynb
```

E coloque na sua pasta de entrega conforme descrito no README da tarefa.