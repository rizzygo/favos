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
