
from pathlib import Path
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

# Membuat parser bahasa Python
PY_LANGUAGE = Language(tspython.language())
parser = Parser(PY_LANGUAGE)

hasil = []

# Kumpulan kode untuk pengujian
pengujian = {
    "1. Kode sederhana": b"x = 1\n",

    "2. Fungsi Python":
        b"def halo(nama):\n    return nama\n",

    "3. Percabangan if/else":
        b'if nilai > 80:\n'
        b'    print("Lulus")\n'
        b'else:\n'
        b'    print("Tidak lulus")\n',

    "4. Class dengan satu method":
        b"class Mahasiswa:\n"
        b"    def belajar(self):\n"
        b"        print('Sedang belajar')\n"
}

# Melakukan seluruh pengujian parsing
hasil.append("========== HASIL PENGUJIAN TUGAS 1 ==========")

for nama, kode in pengujian.items():
    tree = parser.parse(kode)

    hasil.append(f"\n{nama}")
    hasil.append(f"Kode: {kode.decode().strip()}")
    hasil.append(f"Syntax Tree: {tree.root_node}")
    hasil.append(f"Memiliki error: {tree.root_node.has_error}")

# Menguji node bernama dan anonim
tree_fungsi = parser.parse(
    b"def halo(nama):\n    return nama\n"
)

fungsi = tree_fungsi.root_node.named_children[0]

hasil.append("\n========== NODE BERNAMA DAN ANONIM ==========")

hasil.append("\nSemua children function_definition:")
for child in fungsi.children:
    status = "bernama" if child.is_named else "anonim"
    hasil.append(f"{child.type}: {status}")

parameters = fungsi.child_by_field_name("parameters")

hasil.append("\nSemua children parameters:")
for child in parameters.children:
    status = "bernama" if child.is_named else "anonim"
    hasil.append(f"{child.type}: {status}")

hasil.append("\nNamed children function_definition:")
for child in fungsi.named_children:
    hasil.append(child.type)

# Menguji error recovery
kode_salah = b"def halo(nama)\n    return nama\n"
tree_error = parser.parse(kode_salah)

hasil.append("\n========== ERROR RECOVERY ==========")
hasil.append(f"Syntax Tree: {tree_error.root_node}")
hasil.append(f"Memiliki error: {tree_error.root_node.has_error}")

def cari_error(node):
    if node.is_error:
        hasil.append(f"ERROR ditemukan: {node.type}")

    if node.is_missing:
        hasil.append(f"MISSING ditemukan: {node.type}")

    for child in node.children:
        cari_error(child)

cari_error(tree_error.root_node)

# Menampilkan perbedaan children dan named_children
hasil.append("\n========== CHILDREN VS NAMED_CHILDREN ==========")

hasil.append("\nChildren:")
for child in fungsi.children:
    hasil.append(child.type)

hasil.append("\nNamed children:")
for child in fungsi.named_children:
    hasil.append(child.type)

# Menyimpan output ke file TXT
output_dir = Path(__file__).parent / "output"
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "hasil_tugas1.txt"
output_file.write_text("\n".join(hasil), encoding="utf-8")

# Menampilkan hasil di terminal
print("\n".join(hasil))
print(f"\nHasil berhasil disimpan di: {output_file}")
