
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# Membuat parser
PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

# Kode fungsi
kode = b"def halo(nama):\n    return nama\n"

# Melakukan parsing
tree = parser.parse(kode)

# Mengambil node function_definition
fungsi = tree.root_node.children[0]

# Menampilkan semua children
print("Semua children:")
for child in fungsi.children:
    print(child.type)

# Menampilkan named_children saja
print("\nNamed children:")
for child in fungsi.named_children:
    print(child.type)
