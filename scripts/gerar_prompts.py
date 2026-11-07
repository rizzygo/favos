#!/usr/bin/env python3
"""Gera os prompts para colar em qualquer IA a partir do SKILL.md das skills.

O botão "Estudar com IA" do Ako baixa estes arquivos e junta o conteúdo do tópico.
A fonte é sempre o SKILL.md: mudou a skill, rode este script e faça commit do resultado.

Uso:
  python3 scripts/gerar_prompts.py            # escreve prompts/*.txt
  python3 scripts/gerar_prompts.py --conferir # só confere se estão em dia (usado no CI)
"""
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "prompts"
REPO = "https://github.com/rizzygo/favos"

# skill -> (caminho do SKILL.md, abertura do prompt)
PROMPTS = {
    "estudar-junto": (
        "plugins/favo-estudo/skills/estudar-junto/SKILL.md",
        "Quero estudar um assunto com você. Siga o método abaixo do começo ao fim da conversa. "
        f"Ele vem da skill estudar-junto, dos Favos da Rizzygo ({REPO}).",
    ),
}


def corpo(skill_md):
    texto = (RAIZ / skill_md).read_text(encoding="utf-8")
    return re.sub(r"^---\n.*?\n---\n", "", texto, count=1, flags=re.S).strip()


def gerar(nome, skill_md, abertura):
    return (
        f"{abertura}\n\n"
        "=== Método ===\n\n"
        f"{corpo(skill_md)}\n\n"
        "=== O que eu quero estudar ===\n"
    )


def main():
    conferir = "--conferir" in sys.argv[1:]
    desatualizados = []
    for nome, (skill_md, abertura) in PROMPTS.items():
        destino = SAIDA / f"{nome}.txt"
        novo = gerar(nome, skill_md, abertura)
        atual = destino.read_text(encoding="utf-8") if destino.exists() else None
        if atual == novo:
            continue
        if conferir:
            desatualizados.append(destino.relative_to(RAIZ).as_posix())
        else:
            SAIDA.mkdir(exist_ok=True)
            destino.write_text(novo, encoding="utf-8")
            print(f"gerado: {destino.relative_to(RAIZ).as_posix()}")
    if desatualizados:
        print("Prompts fora de dia com o SKILL.md: " + ", ".join(desatualizados))
        print("Rode: python3 scripts/gerar_prompts.py e faça commit do resultado.")
        sys.exit(1)
    if conferir:
        print("Prompts em dia com as skills.")


if __name__ == "__main__":
    main()
