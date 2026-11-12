# AGENTS.md: <nome do projeto>

<!-- Esqueleto de AGENTS.md para um repositório. Funciona como mapa: curto, com
     ponteiros para o resto. Passou de cerca de 100 linhas, mova detalhes para o
     AGENTS.md ou o README de cada pasta e deixe aqui só o ponteiro. -->

Este arquivo vale para qualquer agente de IA e para pessoas. O `CLAUDE.md` só aponta para cá.

## O que é este repositório

Uma ou duas frases: o que ele entrega, para quem, onde é publicado e se é público ou privado.

## Fatias

Cada pasta é uma funcionalidade completa (vertical slice): tela, código, dados e testes juntos. Para mexer numa fatia, abra só ela.

| Fatia | O que é | Mapa próprio |
| --- | --- | --- |
| `<pasta>/` | ... | `<pasta>/AGENTS.md` |

**Compartilhado:** o que serve a várias fatias e muda com mais cuidado.

## Comandos

```sh
<comando de validar>   # o mesmo que o CI roda
<comando de prévia>    # como ver o resultado
```

## Regras

- O que nunca pode acontecer (segredo no git, mexer em produção sem OK).
- O que costuma dar errado neste projeto e como evitar.

## Decisões e specs

- Decisões difíceis de desfazer: `decisoes/NNNN-titulo.md` ([modelo](modelo-adr.md)).
- Funcionalidade nova: `<fatia>/specs/<nome>.md` ([modelo](modelo-spec.md)).

## Commits

Conventional Commits, com a fatia no escopo: `feat(<fatia>): ...`.
