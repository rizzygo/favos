# Como contribuir

Toda contribuição é bem-vinda: corrigir um erro, melhorar a explicação de uma skill ou propor um favo novo. Para ideias, abra uma issue antes de escrever a skill.

## Um favo novo

1. Escolha o plugin pelo público: `favo-estudo` (quem estuda com IA), `favo-trilhas` (quem segue as trilhas do Ako) ou `favo-carreira` (quem planeja a carreira). Se nenhum servir, explique na issue para quem é a skill.
2. Crie `plugins/<plugin>/skills/<nome>/SKILL.md`, com frontmatter `name` (igual ao nome da pasta) e `description` (o que faz e quando acionar, até 1024 caracteres).
3. Crie `plugins/<plugin>/commands/<nome>.md`, um adaptador curto que chama a skill no Claude Code. Copie um dos que já existem.
4. Acrescente a linha no índice do [`AGENTS.md`](AGENTS.md) e na tabela do README.

## Regras de escrita

- Português do Brasil, frases curtas, termo técnico com a explicação ao lado.
- Funciona em qualquer agente: verbos genéricos ("leia o arquivo", "rode o comando").
- Nada de dado de empresa ou de pessoa.
- Link e material só depois de abertos e conferidos. Material pago nunca é obrigatório.
- Ação que apaga, sobrescreve ou mexe em produção só com confirmação de quem usa.

## Conventional Commits

O release-please lê o tipo e o escopo do commit para versionar cada plugin.

| Commit | Efeito |
|---|---|
| `feat(favo-estudo): adiciona exemplo de erro de permissão` | sobe a versão menor do `favo-estudo` |
| `fix(favo-trilhas): corrige ordem das etapas` | sobe a versão de correção do `favo-trilhas` |
| `docs: explica instalação no Copilot` | sem release |

## Antes do PR

```bash
python3 scripts/validar.py
shellcheck scripts/*.sh
```
