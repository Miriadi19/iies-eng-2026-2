# Introdução a Algoritmos com Python

Repositório de tarefas práticas da disciplina. Cada tarefa está em uma pasta separada com enunciado e estrutura base para você completar.

---

## Como funciona

Cada tarefa segue o mesmo fluxo. Leia com atenção antes de começar.

---

## Passo a passo para entregar

### 1. Abra o repositório no VS Code Online

Acesse no navegador:

```
https://vscode.dev/github/eduardo-arcade-metrics/iies-eng-2026-2
```

Na primeira vez, faça login com sua conta GitHub.

Salve esse link nos favoritos — você vai usar em toda aula.

---

### 2. Crie sua branch

O nome da branch deve seguir o padrão:

```
tarefa-XX/nome-sobrenome
```

Exemplo:

```
tarefa-01/joao-silva
```

Clique no nome **main** no canto inferior esquerdo e escolha **Criar novo branch...**.

A branch `main` está protegida — commits diretos são bloqueados. Só é possível enviar código via Pull Request.

---

### 3. Faça a tarefa

Navegue até a pasta da tarefa no Explorer lateral e siga o enunciado do `README.md`.

---

### 4. Commit e push

Clique no ícone de **Source Control** na barra lateral (`Ctrl+Shift+G`), adicione os arquivos, escreva uma mensagem descritiva e clique em **Commit & Push**.

```
tarefa-01: resolução joao-silva
```

---

### 5. Abra um Pull Request

Acesse o repositório no GitHub. Clique em **Compare & pull request**, preencha o formulário de entrega e clique em **Create pull request**.

O professor irá revisar, comentar e aprovar (ou solicitar ajustes) diretamente na PR.

---

## Estrutura do repositório

```
/
├── README.md               <- você está aqui
├── recursos/               <- tutoriais e guias de apoio
├── tarefas/
│   ├── 01-hello-world-github/
│   │   ├── README.md       <- enunciado
│   │   └── entregas/
│   │       └── seu-nome/   <- você cria esta pasta
│   ├── 02-variaveis-e-prints/
│   │   ├── README.md
│   │   ├── notebook.ipynb  <- base para completar
│   │   └── entregas/
│   │       └── seu-nome/
│   └── ...
└── .github/
    └── pull_request_template.md
```

---

## Material de apoio

As aulas e materiais complementares estão no Google Drive da disciplina. O acesso deve ser solicitado com o mesmo e-mail da sua conta GitHub.

[Acessar o Drive da disciplina](https://drive.google.com/drive/folders/1CPAK7SCvkkxN6uk4QucqYotFNrspRuTt?usp=sharing)

---

## Regras

- Um aluno por branch — não compartilhe sua branch
- Commits com mensagens descritivas (não vale `aaa` ou `final final`)
- Prazo de entrega = data de abertura da PR no GitHub
- Dúvidas? Abra uma Issue no repositório ou traga para a aula

---

## Trabalho NP1 — fluxo diferente

O trabalho NP1 está em `tarefas/04-trabalho-np1/` e tem um fluxo de entrega diferente das tarefas regulares. Os exercícios são resolvidos no Google Colab, não no VS Code Online. O notebook deve ser baixado e enviado via branch e Pull Request no GitHub.

O padrão de branch para o NP1 é:

```
np1/nome-sobrenome
```

Leia o README dentro da pasta da tarefa antes de começar. Ele detalha o passo a passo completo, a nomenclatura dos arquivos e os critérios de avaliação.

### Composição da nota NP1

| Componente | Pontuação |
|---|---|
| Prova escrita | 8,0 pontos |
| Trabalho prático (tarefas/04-trabalho-np1) | + 2,0 pontos adicionais |
| Entrega de todas as tarefas anteriores no prazo | + 1,0 ponto adicional |

Os pontos adicionais somam à nota da prova e podem ultrapassar 10. Um aluno que tira 7,0 na prova, entrega o trabalho e tem todas as tarefas em dia fecha a NP1 com 10,0.

---

## Primeira vez usando Git?

Consulte os guias na pasta `recursos/`:

- `tutorial-vscode.md` — passo a passo do fluxo completo
- `guia-markdown.md` — sintaxe Markdown essencial
- `ambiente-local.md` — como configurar no seu próprio computador