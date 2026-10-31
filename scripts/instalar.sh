#!/usr/bin/env bash
# Copia as skills do favos para a pasta que o seu agente de IA lê.
#
# Uso:
#   scripts/instalar.sh [--plugin favo-estudo|favo-trilhas|favo-carreira|todos]
#                       [--agente claude|agents] [--escopo projeto|usuario]
#                       [--destino <pasta>] [--forcar]
#
# Exemplos:
#   scripts/instalar.sh --plugin favo-estudo --agente claude              # ./.claude/skills
#   scripts/instalar.sh --plugin todos --agente agents --escopo usuario # ~/.agents/skills
#   scripts/instalar.sh --plugin favo-estudo --destino ~/minhas-skills    # qualquer pasta
#
# Destinos:
#   claude  projeto: ./.claude/skills    usuario: ~/.claude/skills
#   agents  projeto: ./.agents/skills    usuario: ~/.agents/skills
# Para um agente que não leia nenhuma dessas pastas, use --destino com a pasta de
# instruções dele, ou aponte o agente para o SKILL.md direto.
#
# O que muda: cria uma pasta por skill no destino. Como desfazer: apague essas pastas
# (a lista sai no fim). Sem --forcar, uma skill que já existe no destino não é tocada.
set -euo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PLUGIN="todos"; AGENTE="claude"; ESCOPO="projeto"; DESTINO=""; FORCAR=0

while [ $# -gt 0 ]; do
  case "$1" in
    --plugin) PLUGIN="$2"; shift 2 ;;
    --agente) AGENTE="$2"; shift 2 ;;
    --escopo) ESCOPO="$2"; shift 2 ;;
    --destino) DESTINO="$2"; shift 2 ;;
    --forcar) FORCAR=1; shift ;;
    -h|--help) sed -n '2,24p' "$0"; exit 0 ;;
    *) echo "opção desconhecida: $1 (veja --help)" >&2; exit 2 ;;
  esac
done

if [ -z "$DESTINO" ]; then
  case "$AGENTE:$ESCOPO" in
    claude:projeto) DESTINO="./.claude/skills" ;;
    claude:usuario) DESTINO="$HOME/.claude/skills" ;;
    agents:projeto) DESTINO="./.agents/skills" ;;
    agents:usuario) DESTINO="$HOME/.agents/skills" ;;
    *) echo "combinação inválida: --agente $AGENTE --escopo $ESCOPO" >&2; exit 2 ;;
  esac
fi

if [ "$PLUGIN" = "todos" ]; then
  PLUGINS=$(ls "$RAIZ/plugins")
else
  [ -d "$RAIZ/plugins/$PLUGIN" ] || { echo "plugin não existe: $PLUGIN" >&2; exit 2; }
  PLUGINS="$PLUGIN"
fi

mkdir -p "$DESTINO"
instaladas=(); puladas=()
for p in $PLUGINS; do
  for s in "$RAIZ/plugins/$p/skills"/*/; do
    nome=$(basename "$s")
    alvo="$DESTINO/$nome"
    if [ -e "$alvo" ] && [ "$FORCAR" -ne 1 ]; then
      puladas+=("$nome"); continue
    fi
    rm -rf "$alvo"
    cp -R "$s" "$alvo"
    instaladas+=("$alvo")
  done
done

echo "Destino: $DESTINO"
[ ${#instaladas[@]} -gt 0 ] && printf 'instalada: %s\n' "${instaladas[@]}"
[ ${#puladas[@]} -gt 0 ] && printf 'já existia (use --forcar para trocar): %s\n' "${puladas[@]}"
echo "Confira: ls \"$DESTINO\"  ·  Desfazer: apague as pastas listadas acima."
