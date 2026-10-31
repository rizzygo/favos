---
name: proximo-passo
description: Use quando a pessoa perguntar o que estudar agora, por onde continuar, qual o próximo tópico ou como está o progresso dela nas trilhas da Rizzygo Ako (Primeiros passos em TI e mapas das áreas). Lê a trilha publicada e o progresso que a pessoa informar ou exportar, e sugere um próximo tópico com a lição, o exercício e o tempo estimado.
---

# Próximo passo

A pessoa sai daqui com um tópico para estudar agora, e não com uma lista de vinte. As trilhas ficam em https://ako.rizzygo.com.br/trilhas/.

## 1. Carregue a trilha

Leia os dados publicados do Ako. Se o seu agente tiver acesso à internet, baixe os arquivos. Se não tiver, peça que a pessoa abra o link e cole o conteúdo, ou siga só com o que ela contar.

| Arquivo | O que tem |
|---|---|
| https://raw.githubusercontent.com/rizzygo/ako/main/trilhas/dados/primeiros-passos.json | A trilha Primeiros passos em TI: `etapas` em ordem, `topicos` (com `etapa`, `horas`, `resumo`, `checklist`, `recursos`) e `areas` |
| https://raw.githubusercontent.com/rizzygo/ako/main/trilhas/dados/mapas.json | Os mapas das áreas (infra, dev, dados, qa, seguranca, produto): `mapas[].secoes[].nos[]`, cada nó com `titulo`, `resumo`, `nivel`, `pratica`, `licao` e `topico` (quando liga a um tópico da trilha) |

Não invente tópico, lição ou link: use só o que está nesses arquivos. As lições ficam em `https://ako.rizzygo.com.br/trilhas/materiais/<licao>`.

## 2. Descubra onde a pessoa está

Pergunte, nesta ordem, e pare assim que tiver o suficiente:

1. **Ela tem o arquivo de progresso?** Na página de conquistas do site dá para exportar um `progresso-trilhas-rizzygo-<data>.json`. Nele, `topicos` traz cada tópico iniciado, com `check` (itens do checklist marcados), `quiz` (resultado do desafio) e `ensinei`. `caminho` é a área escolhida no fim da trilha.
2. **Se não tiver:** quais tópicos ela já estudou, ou em que etapa parou.
3. **Quanto tempo tem por semana** para estudar.

O arquivo de progresso só fica com a pessoa. Não peça para ela publicar nem mandar a outra pessoa.

## 3. Escolha um próximo tópico

- **Ainda na trilha Primeiros passos:** o primeiro tópico, na ordem das `etapas`, que não foi concluído. Um tópico começado e não terminado vem antes de um novo.
- **Terminou a trilha:** vá para o mapa da área em `caminho`, ou pergunte qual área interessa. Sugira o primeiro nó `essencial` que ela ainda não estudou, na ordem das seções.
- **Mais de uma opção boa:** mostre no máximo duas e diga o que diferencia cada uma.

## 4. Entregue o próximo passo

Responda neste formato, curto:

**Seu próximo passo: <título do tópico>**

- **Por que agora:** uma frase ligando ao que a pessoa já fez.
- **Tempo:** as `horas` do tópico, divididas pelo tempo por semana que ela informou.
- **Comece por:** a lição do Ako, quando existir, ou o primeiro recurso gratuito do tópico.
- **Pratique:** o `checklist` do tópico ou a `pratica` do nó.
- **Depois:** o tópico seguinte, numa linha, para ela saber o caminho.

Termine lembrando que, no Ako, explicar o assunto para outra pessoa também conta como estudo.
