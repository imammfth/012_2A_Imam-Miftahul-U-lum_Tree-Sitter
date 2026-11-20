import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

if len(sys.argv) != 3:
    print("Penggunaan: python q.py file.py query.scm")
    sys.exit(1)

file_kode = Path(sys.argv[1])
file_query = Path(sys.argv[2])

kode = file_kode.read_bytes()
pola = file_query.read_text(encoding="utf-8")

tree = parser.parse(kode)
query = Query(PY, pola)

hasil = QueryCursor(query).captures(tree.root_node)

if not hasil:
    print("Tidak ada hasil yang cocok.")
else:
    for nama, nodes in hasil.items():
        for node in nodes:
            baris = node.start_point[0] + 1
            teks = node.text.decode("utf-8")
            print(f"@{nama}  baris {baris}: {teks}")
