# Exercício 03 — Controle de temperatura em processo de resfriamento industrial

## Contexto

Em processos industriais como fundição, tratamento térmico de metais e reações químicas, o controle de temperatura é uma etapa crítica de segurança. Após uma operação em alta temperatura, o equipamento precisa ser resfriado de forma controlada antes que qualquer intervenção humana ou próxima etapa do processo possa ocorrer.

Engenheiros de processo definem uma **temperatura de segurança operacional**, abaixo da qual o equipamento pode ser manipulado sem risco. O sistema de resfriamento opera continuamente e a temperatura cai a uma taxa conhecida a cada minuto. O processo de monitoramento registra a temperatura a cada intervalo e só libera o equipamento quando a temperatura atinge o limite seguro.

Neste exercício você vai simular esse processo de resfriamento usando um loop `while`, registrando o histórico de temperatura minuto a minuto.

---

## Dados do problema

```
temperatura_inicial = 850.0    # temperatura inicial do reator em graus Celsius
temperatura_segura = 120.0     # limite de liberação do equipamento em graus Celsius
taxa_resfriamento = 35.0       # queda de temperatura por minuto em graus Celsius
tempo_minuto = 0               # contador de tempo em minutos
```

A taxa de resfriamento não é constante ao longo de todo o processo. Conforme a temperatura cai, o gradiente térmico diminui e o resfriamento fica mais lento. Use as seguintes faixas:

| Temperatura atual (°C) | Taxa de resfriamento (°C/min) |
|------------------------|-------------------------------|
| Acima de 500 | 35,0 |
| Entre 300 e 500 | 22,0 |
| Entre 120 e 300 | 10,0 |

O loop deve continuar enquanto a temperatura estiver **acima** da temperatura de segurança.

---

## O que calcular

A cada minuto do processo:

1. Determine a taxa de resfriamento correta para a temperatura atual
2. Subtraia a taxa da temperatura atual
3. Incremente o contador de minutos
4. Registre o minuto e a temperatura resultante

Ao final do loop, calcule e exiba:

- Tempo total de resfriamento em minutos
- Temperatura final registrada
- Quantos minutos o processo ficou em cada faixa de temperatura

---

## Atenção sobre a temperatura final

A temperatura pode ultrapassar ligeiramente o limite de segurança a depender da taxa aplicada no último intervalo. Isso é esperado e representa o comportamento real de um sistema de monitoramento por intervalos discretos. Não corrija esse valor artificialmente.

---

## Estrutura do notebook

Monte seu notebook no Colab com as células na seguinte ordem:

**Célula 1 — Markdown**
Título do exercício e seu nome completo.

**Célula 2 — Markdown**
Breve descrição do problema com suas próprias palavras. Duas a quatro linhas explicando o que o programa vai fazer.

**Célula 3 — Código: dados de entrada**
Declare todas as variáveis fornecidas no enunciado. Declare também três contadores zerados, um para cada faixa de temperatura, que serão incrementados a cada minuto conforme a faixa ativa.

**Célula 4 — Código: loop de resfriamento**
Implemente o `while` que roda enquanto a temperatura estiver acima do limite seguro. A cada iteração, use `if/elif` para determinar a taxa e qual contador de faixa incrementar, atualize a temperatura, incremente o tempo e imprima o estado atual do minuto.

**Célula 5 — Código: saída final**
Imprima o relatório completo com tempo total, temperatura final e o tempo em minutos gasto em cada faixa de temperatura.

**Célula 6 — Markdown**
Interpretação do resultado. Responda em texto: em qual faixa o processo passou mais tempo? Por que isso acontece fisicamente? O que aconteceria se a taxa de resfriamento fosse constante em 35 °C/min durante todo o processo? Mínimo de quatro linhas.

---

## Saída esperada

Durante o loop, imprima o estado a cada minuto em formato semelhante a este:

```
Minuto 01 | Temperatura: 815.0 °C | Taxa aplicada: 35.0 °C/min
Minuto 02 | Temperatura: 780.0 °C | Taxa aplicada: 35.0 °C/min
...
Minuto 12 | Temperatura: 478.0 °C | Taxa aplicada: 22.0 °C/min
...
```

E ao final o relatório de encerramento:

```
=== RELATÓRIO DE RESFRIAMENTO ===
Temperatura inicial:   850.0 °C
Temperatura final:     XXX.X °C
Tempo total:           XX minutos
Tempo na faixa > 500:  XX minutos
Tempo na faixa 300-500: XX minutos
Tempo na faixa 120-300: XX minutos
Status: Equipamento liberado para operação
=================================
```

Os valores marcados com XX devem ser calculados pelo seu código.

---

## Entrega

Salve o arquivo como:

```
ex03-controle-temperatura-nome-sobrenome.ipynb
```

E coloque na sua pasta de entrega conforme descrito no README da tarefa.