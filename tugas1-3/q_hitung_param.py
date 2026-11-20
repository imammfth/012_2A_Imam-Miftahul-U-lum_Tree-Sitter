import sys

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

kode = open(sys.argv[1], "rb").read()
pola = open(sys.argv[2], encoding="utf-8").read()

tree = parser.parse(kode)
query = Query(PY, pola)

hasil = QueryCursor(query).matches(tree.root_node)

for _, cap in hasil:
    nama = cap["nama"][0].text.decode()
    jumlah = cap["params"][0].named_child_count

    print(f"Fungsi {nama} memiliki {jumlah} parameter")
