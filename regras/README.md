# Regras base

O [`AGENTS.md`](AGENTS.md) desta pasta é um arquivo de regras pronto para copiar no seu projeto. Com ele, a IA responde em português, explica antes de mudar, não inventa comando e fecha cada mudança dizendo o que muda, como desfazer e como conferir.

## Onde colocar

| Ferramenta | Arquivo no seu projeto |
|---|---|
| Codex, Cursor, Gemini CLI e outros que leem `AGENTS.md` | `AGENTS.md` na raiz |
| Claude Code | `CLAUDE.md` na raiz, com a linha `@AGENTS.md`, ou o conteúdo copiado |
| GitHub Copilot | `.github/copilot-instructions.md` |

Para copiar, rode na raiz do seu projeto:

```bash
curl -fsSL https://raw.githubusercontent.com/rizzygo/favos/main/regras/AGENTS.md -o AGENTS.md
```

**Antes de rodar**

1. **O que muda:** cria o arquivo `AGENTS.md` na pasta atual. Se já existir um, ele é substituído.
2. **Como desfazer:** se o arquivo não existia, apague-o. Se existia e está no git, `git checkout -- AGENTS.md`.
3. **Como saber que deu certo:** `head -1 AGENTS.md` mostra `# Regras para a IA neste projeto`.
4. **O que não verifiquei:** se o seu projeto já tem um `AGENTS.md`. Se tiver, junte as regras à mão em vez de rodar o comando.

Ajuste à vontade: as regras são um ponto de partida.

## Modelos para organizar o projeto

Além do `AGENTS.md` de regras, esta pasta tem três modelos para deixar o projeto fácil de entender, para pessoas e para a IA:

| Modelo | Para quê |
|---|---|
| [`esqueleto-agents.md`](esqueleto-agents.md) | O `AGENTS.md` do repositório como mapa: o que é, fatias, comandos, regras e onde ficam as decisões |
| [`modelo-spec.md`](modelo-spec.md) | Uma página para descrever o problema antes do código: quem sente, o que muda, critérios de aceite e como conferir |
| [`modelo-adr.md`](modelo-adr.md) | Registro de uma decisão difícil de desfazer (ADR): contexto, opções e consequências |

Os repositórios abertos da Rizzygo seguem esses modelos. Veja o [`AGENTS.md` do Ako](https://github.com/rizzygo/ako/blob/main/AGENTS.md) como exemplo.
