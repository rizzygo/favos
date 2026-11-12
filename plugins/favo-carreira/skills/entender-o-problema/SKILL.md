---
name: entender-o-problema
description: Use quando a pessoa receber um pedido (uma tarefa, um ticket, uma ideia de feature, um "faz um botão") e quiser entender o problema de verdade antes de começar, ou quando pedir uma spec. Faz as perguntas certas para o cargo dela (júnior, pleno, sênior, especialista, tech lead, gestão), escreve o problema numa frase e entrega uma spec de uma página com critérios de aceite.
---

# Entender o problema (Qual é o B.O.?)

O pedido que chega quase nunca é o problema. É a solução que alguém imaginou. Esta skill ajuda a pessoa a achar o problema de verdade antes de escrever código, e a sair com uma spec curta. Ela não resolve o pedido pela pessoa: faz perguntas e organiza as respostas.

## 1. Receba o pedido e o cargo

Pergunte, em uma mensagem:

- Qual é o pedido, do jeito que chegou (cole a mensagem, o ticket ou descreva).
- Quem pediu (um perfil, como "cliente", "gestora", "time de vendas"; nunca peça nome de pessoa ou de empresa).
- O cargo dela: júnior, pleno, sênior, especialista, tech lead ou gestão. Se ainda não trabalha na área, use júnior.

## 2. Separe o pedido da necessidade

Diga, em uma ou duas frases, qual parte do pedido já é uma solução (um botão, uma tela, uma ferramenta) e o que ainda não se sabe sobre o porquê.

Depois faça as perguntas abaixo, uma ou duas por vez. Se a pessoa não sabe a resposta, ajude a escrever a pergunta para levar a quem pediu.

1. **Quem** sente o problema?
2. **Quando** ele aparece? Peça a última vez que aconteceu.
3. **O que acontece hoje**, sem a solução? Como a pessoa se vira?
4. **Por que** isso incomoda? Pergunte de novo a cada resposta, umas três a cinco vezes, até chegar numa dor que alguém sente. Pergunte sobre o processo, nunca sobre um culpado.
5. **Como saber** que resolveu?
6. **O que não pode** acontecer: perder dado, ficar lento, mudar o que já funciona.

## 3. Faça a pergunta da altura dela

O mesmo pedido tem um tamanho diferente em cada cargo. Faça a pergunta do cargo dela e a do cargo seguinte:

| Cargo | O que olha primeiro | Pergunta |
|---|---|---|
| Júnior | A tarefa | Onde isso aparece e como sei que funcionou? |
| Pleno | O fluxo inteiro | O que acontece com quem já usa hoje? |
| Sênior | A solução mais simples | Existe um jeito menor de resolver a mesma dor? |
| Especialista | O risco que ninguém viu | O que pode quebrar, e como desfazer se der errado? |
| Tech lead | O time e a ordem do trabalho | Dá para entregar em partes? Quem revisa? Como o time sabe que acabou? |
| Gestão | O valor e o custo | Quantas pessoas sentem isso? É mais importante que o resto da fila? |

## 4. Escreva o problema numa frase

Escreva a frase sem a solução dentro, no formato: quem sente, em que momento, o que acontece hoje. Mostre para a pessoa e pergunte se é isso. Sugira que ela confira a frase com quem pediu antes de seguir.

Se as respostas mostrarem que a solução pedida não resolve a dor, diga isso com clareza e sugira a alternativa mais simples. A decisão continua sendo da pessoa e de quem pediu.

## 5. Entregue a spec de uma página

Use este formato:

```markdown
# Spec: <nome curto>

## Problema
<a frase do passo 4>

## Resultado esperado
<o que muda para quem sente o problema, em uma frase>

## Fora do escopo
<o que não vai ser feito agora>

## Critérios de aceite
- [ ] Dado ..., quando ..., então ...
- [ ] Dado ..., quando ..., então ...

## Como conferir
<comando de teste, telas para abrir, o que acontece com quem já usava>
```

Escreva pelo menos um critério para o caso de erro ou para quem já usava, não só para o caminho feliz.

Regras:

- Não invente número, prazo, custo ou fato sobre a empresa. O que faltar vira pergunta para levar a quem pediu.
- Não peça nem guarde dado pessoal ou da empresa. Use perfis ("quem atende o cliente"), não nomes.
- Termos técnicos em inglês ficam em inglês (deploy, pull request, feature).

Termine com uma pergunta para ela pensar: qual parte do pedido mudou depois dessa conversa?

O exemplo completo, com o mesmo pedido visto nos seis cargos, está na lição do Ako: https://ako.rizzygo.com.br/trilhas/materiais/qual-e-o-bo.html
