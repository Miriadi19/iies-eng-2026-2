# Atividade - Fluxograma: Inspeção de Segurança de Laje

## Contexto

Em projetos de construção civil, antes de aprovar uma laje, o engenheiro precisa verificar se as dimensões e a carga prevista estão dentro dos limites de segurança. Nesta atividade, você vai representar esse processo de verificação como um fluxograma.

## Dados de entrada

- `vao` — vão livre da laje em metros (distância entre apoios)
- `espessura` — espessura da laje em centímetros
- `carga` — carga prevista em kg/m²

## Regras de verificação

Aplicar **nesta ordem**:

1. Se `espessura < vao × 3`, a laje é **muito fina** → **Reprovar**
2. Se `carga > 500`, a carga é **excessiva** → **Reprovar**
3. Se `espessura < vao × 4` **e** `carga > 300`, a laje está no **limite** → **Reforço necessário**
4. Se nenhuma das condições anteriores for verdadeira → **Aprovada**

## O que entregar

Um fluxograma com:

- Início e fim
- Blocos de entrada para os três dados
- Losangos de decisão para cada regra
- As saídas possíveis: **Aprovada**, **Reforço necessário**, **Reprovar**

## Exemplos para testar seu fluxograma

| vão (m) | espessura (cm) | carga (kg/m²) | resultado esperado |
|---------|----------------|---------------|--------------------|
| 4 | 10 | 200 | Aprovada |
| 4 | 10 | 400 | Reforço necessário |
| 4 | 8 | 200 | Reprovar — laje muito fina |
| 4 | 14 | 600 | Reprovar — carga excessiva |