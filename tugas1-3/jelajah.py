
import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# Membuat parser untuk bahasa Python
parser = Parser(Language(tspython.language()))


def jelajah(node, kedalaman=0, field=None):
    # Mengambil posisi node
    baris, kolom = node.start_point

    # Menyiapkan label field jika tersedia
    label = f"{field}: " if field else ""

    # Menampilkan tipe node dan posisinya
    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")

    # TODO: menelusuri child yang bernama
    for i, child in enumerate(node.children):
        if child.is_named:
            nama_field = node.field_name_for_child(i)
            jelajah(child, kedalaman + 1, nama_field)

# Membaca file Python dari argumen terminal
with open(sys.argv[1], "rb") as f:
    tree = parser.parse(f.read())

# Memulai penelusuran dari root node
jelajah(tree.root_node)
