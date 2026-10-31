#!/usr/bin/env python3
"""Validação do repositório, sem rede: roda igual na máquina e no CI.

Confere:
  1. frontmatter YAML de todo SKILL.md (name e description obrigatórios, name igual à pasta)
  2. todo .json e .yaml/.yml é válido
  3. links relativos em Markdown apontam para arquivo que existe
  4. nenhum termo proibido aparece (lista fora do git: arquivo .termos-proibidos ou
     variável TERMOS_PROIBIDOS, um termo por linha ou separados por vírgula)

Uso: python3 scripts/validar.py [raiz]
"""
import json
import os
import pathlib
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML não encontrado: pip install pyyaml")

RAIZ = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
IGNORAR = {".git", "node_modules", ".venv", "__pycache__"}
erros = []


def arquivos(*sufixos):
    for p in RAIZ.rglob("*"):
        if p.is_file() and not (set(p.relative_to(RAIZ).parts) & IGNORAR) and p.suffix in sufixos:
            yield p


def rel(p):
    return p.relative_to(RAIZ).as_posix()


# 1. SKILL.md
for p in RAIZ.rglob("SKILL.md"):
    if set(p.relative_to(RAIZ).parts) & IGNORAR:
        continue
    texto = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        erros.append(f"{rel(p)}: sem frontmatter YAML")
        continue
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        erros.append(f"{rel(p)}: frontmatter inválido ({e})")
        continue
    for campo in ("name", "description"):
        if not meta.get(campo):
            erros.append(f"{rel(p)}: falta `{campo}` no frontmatter")
    if meta.get("name") and meta["name"] != p.parent.name:
        erros.append(f"{rel(p)}: name `{meta['name']}` difere da pasta `{p.parent.name}`")
    if len(str(meta.get("description", ""))) > 1024:
        erros.append(f"{rel(p)}: description passa de 1024 caracteres")

# 2. JSON e YAML
for p in arquivos(".json"):
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        erros.append(f"{rel(p)}: JSON inválido ({e})")
for p in arquivos(".yaml", ".yml"):
    if "templates" in p.parts and "charts" in p.parts:
        continue  # templates Helm não são YAML puro
    try:
        list(yaml.safe_load_all(p.read_text(encoding="utf-8")))
    except yaml.YAMLError as e:
        erros.append(f"{rel(p)}: YAML inválido ({e})")

# 3. links relativos
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
for p in arquivos(".md"):
    texto = re.sub(r"```.*?```", "", p.read_text(encoding="utf-8"), flags=re.S)
    for alvo in LINK.findall(texto):
        if re.match(r"^[a-z][a-z0-9+.-]*:|^#|^<|^mailto:", alvo):
            continue
        caminho = alvo.split("#", 1)[0]
        if caminho and not (p.parent / caminho).exists():
            erros.append(f"{rel(p)}: link quebrado -> {alvo}")

# 4. termos proibidos
termos = []
arq = RAIZ / ".termos-proibidos"
if arq.exists():
    termos += [t.strip() for t in arq.read_text(encoding="utf-8").splitlines()]
termos += [t.strip() for t in re.split(r"[,\n]", os.environ.get("TERMOS_PROIBIDOS", ""))]
termos = [t for t in termos if t and not t.startswith("#")]
if termos:
    padrao = re.compile("|".join(re.escape(t) for t in termos), re.I)
    for p in RAIZ.rglob("*"):
        if not p.is_file() or set(p.relative_to(RAIZ).parts) & IGNORAR or p.name == ".termos-proibidos":
            continue
        try:
            texto = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        for m in padrao.finditer(texto):
            linha = texto.count("\n", 0, m.start()) + 1
            erros.append(f"{rel(p)}:{linha}: termo proibido `{m.group(0)}`")

# 5. plugins: marketplace, manifesto e comando por skill
mk = RAIZ / ".claude-plugin/marketplace.json"
if mk.exists():
    listados = {p["name"] for p in json.loads(mk.read_text(encoding="utf-8")).get("plugins", [])}
    for d in sorted((RAIZ / "plugins").glob("*/")):
        if d.name not in listados:
            erros.append(f"plugins/{d.name}: fora do .claude-plugin/marketplace.json")
        if not (d / ".claude-plugin/plugin.json").exists():
            erros.append(f"plugins/{d.name}: sem .claude-plugin/plugin.json")
        for s in sorted((d / "skills").glob("*/")):
            if not (d / "commands" / f"{s.name}.md").exists():
                erros.append(f"plugins/{d.name}/skills/{s.name}: sem commands/{s.name}.md")

if erros:
    print("\n".join(erros))
    print(f"\n{len(erros)} problema(s).")
    sys.exit(1)
print("ok: skills, JSON, YAML, links e termos conferidos.")
