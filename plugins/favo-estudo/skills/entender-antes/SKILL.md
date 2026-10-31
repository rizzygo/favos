---
name: entender-antes
description: Use quando a pessoa colar ou pedir um comando, script, arquivo de configuração, trecho de código ou mensagem de erro que ainda não entende, ou perguntar "o que isso faz?". Explica parte por parte, em português simples, o que acontece ao rodar, o risco e como conferir, antes de a pessoa executar ou colar uma correção.
---

# Entender antes

Rodar o que não se entende é o jeito mais rápido de quebrar algo e o mais lento de aprender. Esta skill explica primeiro e deixa a decisão de rodar com a pessoa.

## 1. Identifique o que chegou

- **Comando ou script:** o que vai ser executado.
- **Arquivo** (configuração, Dockerfile, YAML, código): o que ele define.
- **Erro ou log:** o que deu errado e onde.

Se faltar algo que muda a explicação, como o sistema operacional, a ferramenta ou de onde veio o comando, pergunte. No máximo duas perguntas.

## 2. Explique parte por parte

Quebre em pedaços pequenos e explique cada um numa linha, na ordem em que acontecem:

```text
sudo apt update && sudo apt upgrade -y
│    │          │  │                └ responde "sim" a tudo, sem perguntar
│    │          │  └ instala as versões novas dos pacotes
│    │          └ só roda a segunda parte se a primeira der certo
│    └ atualiza a lista de pacotes disponíveis (não instala nada)
└ roda como administrador
```

- Use palavras do dia a dia. Termo técnico aparece com a explicação ao lado na primeira vez.
- Não invente o que uma flag ou função faz. Se não tem certeza, diga "não confirmei" e mostre como conferir: `--help`, `man`, a documentação oficial.
- Num erro, aponte a linha que importa (a primeira causa, não a última linha do log) e diga o que ela significa.

## 3. Diga o que acontece ao rodar

- **Só lê ou também altera?** Arquivos, pacotes, permissões, dados, algo na nuvem.
- **Dá para desfazer?** Como. Se não der, avise em destaque.
- **O que pode dar errado** no caso da pessoa.
- **Como conferir** que deu certo, com um comando ou sinal concreto.

Se o comando apaga dados, mexe em permissões, em produção ou baixa e executa algo da internet (`curl ... | bash`), diga isso antes de tudo, logo no começo da resposta.

## 4. Confira o entendimento

Termine com uma pergunta curta para a pessoa responder com as palavras dela, por exemplo:

- "Com o que você leu, o que acontece se rodar esse comando duas vezes?"
- "Qual parte desse comando você trocaria para só simular, sem alterar nada?"

Se a pessoa pedir para executar, siga a skill `antes-de-rodar` quando ela estiver instalada.
