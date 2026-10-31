# AGENTS.md: instruções para agentes de IA

Este arquivo vale para qualquer agente (Claude Code, Codex, Gemini CLI, GitHub Copilot, Cursor e outros). O `CLAUDE.md` só aponta para cá.

## O que é este repositório

O **favos** guarda as skills abertas da Rizzygo, no formato Agent Skills, agrupadas em plugins por público. Cada skill é uma pasta com `SKILL.md` (frontmatter `name` e `description`, depois o procedimento). Faz parte da Iniciativa Ako: conteúdo gratuito, em português.

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
- **`antes-de-rodar` existe também no repositório `ako`.** Mudou aqui, mude lá, e vice-versa.
- **Valide:** `python3 scripts/validar.py`.
- Português, voz ativa, frases curtas.

## Commits

Conventional Commits com o plugin no escopo: `feat(favo-estudo): ...`, `fix(favo-trilhas): ...`. O release-please sobe a versão de cada plugin e do `plugin.json` dele.
