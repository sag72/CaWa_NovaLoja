# -*- coding: utf-8 -*-
"""
Gera web/github/index.html (pagina completa, para o GitHub Pages) a partir de
aberturas_lojas.html, que e o fragmento publicado no claude.ai.

Uso:
    python gerar_index_github.py
"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(BASE, "aberturas_lojas.html")
DESTINO = os.path.join(BASE, "github", "index.html")

CABECALHO = (
    '<!doctype html>\n<html lang="pt-PT">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>:root{color-scheme:light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    '</head>\n<body>\n'
)
RODAPE = '\n</body>\n</html>\n'

with open(ORIGEM, encoding="utf-8") as fh:
    fragmento = fh.read()
os.makedirs(os.path.dirname(DESTINO), exist_ok=True)
with open(DESTINO, "w", encoding="utf-8", newline="\n") as fh:
    fh.write(CABECALHO + fragmento + RODAPE)
print("Gerado:", DESTINO)
