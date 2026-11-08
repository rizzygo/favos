# Favos

Plugins e skills abertos da [Rizzygo](https://github.com/rizzygo), em português, para quem estuda e trabalha com tecnologia usando IA. Cada skill é um favo, e a colmeia é de todos.

Os Favos fazem parte da Iniciativa Ako, a frente gratuita da Rizzygo. As skills seguem o formato aberto **Agent Skills** (`SKILL.md`): foram escritas para o Claude Code e funcionam em outros agentes que leem esse formato ou aceitam um arquivo de instruções.

## Os plugins

| Plugin | Para quem | Skills |
|---|---|---|
| **`favo-estudo`** | Quem estuda tecnologia com IA | `antes-de-rodar` · `entender-antes` · `estudar-junto` |
| **`favo-trilhas`** | Quem segue as [trilhas do Ako](https://ako.rizzygo.com.br/trilhas/) | `proximo-passo` |
| **`favo-carreira`** | Quem planeja o próximo passo na carreira | `carreira-em-y` |

Além dos plugins, a pasta [`regras/`](regras) tem um `AGENTS.md` base para copiar no seu projeto: a IA responde em português, explica antes de mudar e fecha cada mudança dizendo como desfazer.

O índice completo, com o que cada skill faz e quando acionar, está no [`AGENTS.md`](AGENTS.md). Para ver cada skill com exemplos e botão de copiar, abra a [página dos Favos no Ako](https://ako.rizzygo.com.br/favos/).

A `antes-de-rodar` tem um [README próprio](plugins/favo-estudo/skills/antes-de-rodar/README.md), com a instalação em cada ferramenta, três exemplos e o resultado do teste com e sem a skill.

## Sem instalar nada: o botão "Estudar com IA" do Ako

Cada tópico das [trilhas do Ako](https://ako.rizzygo.com.br/trilhas/) tem um botão que copia um prompt pronto para o ChatGPT, o Claude, o Gemini ou outra IA, até pelo celular. O prompt junta o método da `estudar-junto` com o conteúdo do tópico. O método sai de [`prompts/estudar-junto.txt`](prompts/estudar-junto.txt), gerado do `SKILL.md` por `scripts/gerar_prompts.py`.

## Instalar

### Claude Code

```bash
claude plugin marketplace add rizzygo/favos
claude plugin install favo-estudo@favos
claude plugin install favo-trilhas@favos
claude plugin install favo-carreira@favos
```

Instale só os plugins que fazem sentido para você. Os comandos aparecem como `/favo-estudo:entender-antes`, `/favo-trilhas:proximo-passo` e assim por diante, e as skills também são acionadas sozinhas quando o assunto aparece na conversa.

Para atualizar:

```bash
claude plugin marketplace update favos
claude plugin update favo-estudo@favos
```

### Outros agentes

Copie as skills para a pasta que o seu agente lê:

```bash
git clone https://github.com/rizzygo/favos.git
favos/scripts/instalar.sh --plugin favo-estudo --agente claude   # ./.claude/skills
favos/scripts/instalar.sh --plugin todos --agente agents         # ./.agents/skills
favos/scripts/instalar.sh --plugin favo-estudo --destino <pasta> # qualquer pasta
```

| Agente | Como usar |
|---|---|
| Agentes que leem Agent Skills | Instale com `--agente agents` ou `--agente claude` |
| GitHub Copilot | Instale com `--destino .github/skills` |
| Codex, Gemini CLI, Cursor e outros | Aponte o agente para o `SKILL.md` da skill que quer usar |

Sem pasta de skills, a forma que sempre funciona: peça ao agente *"leia `<caminho>/SKILL.md` e siga o procedimento"*.

**Antes de rodar** o `instalar.sh`

1. **O que muda:** cria uma pasta por skill no destino. Uma skill que já existe lá não é tocada, a não ser com `--forcar`.
2. **Como desfazer:** apague as pastas que o script lista no fim.
3. **Como saber que deu certo:** `ls .claude/skills` (ou o destino escolhido) mostra as pastas das skills.
4. **O que não verifiquei:** em que pasta o seu agente procura skills. Confira na documentação dele.

## Contribuir com um favo

Tem uma skill que ajudou nos seus estudos ou no trabalho? Proponha um favo. O passo a passo está no [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Licença

[MIT](LICENSE).
