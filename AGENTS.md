# AGENTS.md: instruções para agentes de IA

Este arquivo vale para qualquer agente (Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor e outros). O `CLAUDE.md` só aponta para cá.

## O que é este repositório

O **favos** guarda as skills abertas da Rizzygo, no formato Agent Skills, agrupadas em plugins por público. Cada skill é uma pasta com `SKILL.md` (frontmatter `name` e `description`, depois o procedimento). Faz parte da Rizzygo All, a parte aberta e gratuita da Rizzygo, ao lado do Ako: conteúdo gratuito, em português.

## Índice das skills

Leia o `SKILL.md` da skill antes de usá-la. A `description` diz quando acionar.

| Skill | Plugin | Quando usar | Arquivo |
|---|---|---|---|
| `antes-de-rodar` | favo-estudo | Antes de sugerir ou executar qualquer mudança: o que muda, como desfazer, como conferir | [`plugins/favo-estudo/skills/antes-de-rodar/SKILL.md`](plugins/favo-estudo/skills/antes-de-rodar/SKILL.md) |
| `entender-antes` | favo-estudo | Explicar um comando, arquivo ou erro antes de a pessoa rodar | [`plugins/favo-estudo/skills/entender-antes/SKILL.md`](plugins/favo-estudo/skills/entender-antes/SKILL.md) |
| `estudar-junto` | favo-estudo | Estudar um assunto perguntando, explicando em partes e pedindo a explicação de volta | [`plugins/favo-estudo/skills/estudar-junto/SKILL.md`](plugins/favo-estudo/skills/estudar-junto/SKILL.md) |
| `proximo-passo` | favo-trilhas | Sugerir o próximo tópico nas trilhas e mapas do Ako | [`plugins/favo-trilhas/skills/proximo-passo/SKILL.md`](plugins/favo-trilhas/skills/proximo-passo/SKILL.md) |
| `carreira-em-y` | favo-carreira | Plano de evolução pela técnica ou pela gestão, com metas de 90 dias | [`plugins/favo-carreira/skills/carreira-em-y/SKILL.md`](plugins/favo-carreira/skills/carreira-em-y/SKILL.md) |

## Regras para mudar este repositório

- **Um plugin por público.** Plugin novo só quando o público muda. Skill nova entra no plugin de quem vai usar.
- **Escreva para qualquer agente:** verbos genéricos, sem depender de nome de ferramenta do Claude. O que for específico de um agente vai marcado ("no Claude Code, ...").
- **Nada de dado de empresa ou de pessoa** nas skills. Este repositório é público.
- **Não invente fonte:** link, curso ou número só entra depois de aberto e conferido. Material pago nunca é obrigatório.
- **A `antes-de-rodar` mora só aqui.** O repositório `ako` não guarda mais cópia: o guia e o site apontam para este repositório.
- **Toda skill tem uma página no Ako**, em `ako.rizzygo.com.br/favos/<skill>/` (pasta `favos/` do repositório `ako`). Skill nova ou mudança no que a skill faz: atualize a página lá também.
- **Prompts para colar em qualquer IA** ficam em `prompts/` e saem do `SKILL.md` por `python3 scripts/gerar_prompts.py`. O botão "Estudar com IA" do Ako baixa esses arquivos. Mudou uma skill que tem prompt: rode o script e faça commit do resultado.
- **Decisões difíceis de desfazer** viram um arquivo em [`decisoes/`](decisoes/), no [modelo](regras/modelo-adr.md).
- Português, voz ativa, frases curtas.

## Comandos

```sh
python3 scripts/validar.py                # SKILL.md, plugins, links e termos proibidos
python3 scripts/gerar_prompts.py          # gera prompts/ a partir dos SKILL.md
python3 scripts/gerar_prompts.py --conferir   # confere se prompts/ está em dia (o CI roda este)
```

O CI (`.github/workflows/validar.yml`) também roda `shellcheck scripts/*.sh` e `yamllint`.

## Commits

Conventional Commits com o plugin no escopo: `feat(favo-estudo): ...`, `fix(favo-trilhas): ...`. O release-please sobe a versão de cada plugin e do `plugin.json` dele.
