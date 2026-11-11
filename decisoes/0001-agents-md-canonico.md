# 0001: AGENTS.md é o arquivo canônico de instruções

- Estado: aceita
- Data: registrada em 11/11/2026; vale desde a criação do repositório

## Contexto

Quem usa os Favos trabalha com agentes diferentes: Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor. Cada um procura instruções num arquivo. Manter um arquivo por agente cria várias versões da mesma regra, e uma acaba desatualizada.

## Decisão

As instruções ficam num `AGENTS.md` na raiz, no formato aberto mantido pela Agentic AI Foundation, da Linux Foundation ([agents.md](https://agents.md/)). O `CLAUDE.md` só aponta para ele. Uma pasta pode ter um `AGENTS.md` próprio, e o mais perto do arquivo editado vale primeiro. Vale para todos os repositórios da Rizzygo.

## Opções consideradas

- **`AGENTS.md` canônico (escolhida):** um texto só, lido pela maioria dos agentes.
- **Um arquivo por agente:** cada um no formato preferido, mas com regras duplicadas.
- **Só `CLAUDE.md`:** simples para o Claude Code, mas deixa os outros agentes sem instrução.

## Consequências

- Regra nova entra no `AGENTS.md`. O que for específico de um agente vai marcado ("no Claude Code, ...").
- O `AGENTS.md` funciona como mapa: curto, com ponteiros. Modelo em [`regras/esqueleto-agents.md`](../regras/esqueleto-agents.md).
