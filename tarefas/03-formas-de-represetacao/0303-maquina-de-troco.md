# Atividade — Máquina de Troco

## Contexto

Você foi contratado para programar o sistema de uma máquina de autoatendimento.
Quando o cliente insere dinheiro e escolhe um produto, a máquina precisa calcular
o troco e informar quantas cédulas e moedas devem ser devolvidas.

Seu objetivo é representar esse processo de três formas diferentes.

---

## Regras do sistema

- O cliente informa o **preço do produto** e o **valor pago**
- Se o valor pago for **menor que o preço**, exibir mensagem de valor insuficiente
- Se o valor pago for **igual ao preço**, exibir "sem troco"
- Se houver troco, devolvê-lo usando o **menor número possível de cédulas e moedas**
- Cédulas e moedas disponíveis (em ordem decrescente):
  R$ 100 · R$ 50 · R$ 20 · R$ 10 · R$ 5 · R$ 2 · R$ 1 · R$ 0,50 · R$ 0,25 · R$ 0,10 · R$ 0,05 · R$ 0,01

---

## Parte 1 — Descrição narrativa

Escreva em português corrido, como se estivesse explicando o funcionamento
da máquina para alguém que nunca a viu.

Sua descrição deve deixar claro:

- O que acontece quando o valor pago é insuficiente
- O que acontece quando não há troco
- Como a máquina decide quais cédulas e moedas devolver
- Quando o processo termina

> **Dica:** tente ser preciso o suficiente para que outra pessoa consiga
> implementar o sistema só com o que você escreveu — sem adivinhar nada.

---

## Parte 2 — Fluxograma

Desenhe o fluxograma completo usando os símbolos padrão:

| Símbolo | Uso |
|---------|-----|
| Oval | Início e Fim |
| Paralelogramo | Entrada e Saída |
| Retângulo | Processamento |
| Losango | Decisão (Sim / Não) |

Seu fluxograma deve conter:

- Leitura do preço e do valor pago
- Verificação se o valor pago é suficiente
- Cálculo do troco
- Loop pelas cédulas e moedas
- Exibição das quantidades de cada cédula/moeda
- Fim do processo

---

## Parte 3 — Pseudocódigo

Escreva o algoritmo em pseudocódigo (Portugol ou linguagem estruturada).

Use as estruturas:

- `LEIA` e `ESCREVA` para entrada e saída
- `SE ... ENTÃO ... SENÃO` para decisões
- `PARA CADA ... FAÇA` para o loop pelas cédulas
- Operadores `DIV` (divisão inteira) e `MOD` (resto)

**Exemplo de estrutura esperada:**

```
ALGORITMO maquina_de_troco
  LEIA preco, pago
  SE pago < preco ENTÃO
    ESCREVA "Valor insuficiente"
  SENÃO
    troco ← pago - preco
    SE troco == 0 ENTÃO
      ESCREVA "Sem troco"
    SENÃO
      PARA CADA valor EM [10000, 5000, ...] FAÇA
        ...
      FIM PARA
  FIM SE
FIM ALGORITMO
```

> **Atenção:** trabalhe com os valores em **centavos** para evitar erros
> de arredondamento. R$ 1,00 = 100 centavos, R$ 0,25 = 25 centavos.

---

## Exemplos para testar sua solução

| Preço (R$) | Pago (R$) | Resultado esperado |
|------------|-----------|-------------------|
| 3,50 | 2,00 | Valor insuficiente |
| 5,00 | 5,00 | Sem troco |
| 3,50 | 5,00 | 1 × R$ 1,00 + 1 × R$ 0,50 |
| 7,30 | 10,00 | 1 × R$ 2,00 + 2 × R$ 0,25 + 4 × R$ 0,10 + 1 × R$ 0,05 |

---

## O que entregar

As três representações (narrativa, fluxograma e pseudocódigo) para o mesmo problema.
Ao final, compare as três: o que ficou mais fácil de escrever? O que ficou mais preciso?