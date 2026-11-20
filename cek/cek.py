import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

# Menyiapkan parser Python
PY = Language(tspython.language())
parser = Parser(PY)

# Query untuk mencari komentar TODO dan FIXME
Q_TODO = Query(
    PY,
    '((comment) @c (#match? @c "TODO|FIXME"))'
)

# Query untuk mencari definisi fungsi dan namanya
Q_FUNGSI = Query(
    PY,
    '(function_definition name: (identifier) @nama) @fungsi'
)

# Folder yang tidak perlu diperiksa
SKIP_DIRS = {".git", "venv", ".venv", "__pycache__", "node_modules"}


def cari_error(node):
    """Mencari node ERROR atau MISSING pertama secara rekursif."""
    if node.is_error or node.is_missing:
        return node

    for child in node.children:
        hasil = cari_error(child)
        if hasil is not None:
            return hasil

    return None


def cek_file(path):
    """Memeriksa satu file Python."""
    kode = path.read_bytes()
    tree = parser.parse(kode)
    root = tree.root_node

    # Fitur 1: mencari komentar TODO/FIXME
    for node in QueryCursor(Q_TODO).captures(root).get("c", []):
        baris = node.start_point[0] + 1
        teks = node.text.decode(errors="replace").strip()
        print(f"[TODO/FIXME] {path}:{baris}: {teks}")

    # Fitur 2: mencari fungsi yang lebih dari 30 baris
    hasil_fungsi = QueryCursor(Q_FUNGSI).matches(root)

    for _, cap in hasil_fungsi:
        nama = cap["nama"][0].text.decode(errors="replace")
        fungsi = cap["fungsi"][0]

        jumlah_baris = (
            fungsi.end_point[0] - fungsi.start_point[0] + 1
        )

        if jumlah_baris > 30:
            baris = fungsi.start_point[0] + 1
            print(
                f"[FUNGSI PANJANG] {path}:{baris}: "
                f"{nama} ({jumlah_baris} baris)"
            )

    # Fitur 3: memeriksa kesalahan sintaks
    if root.has_error:
        node_error = cari_error(root)

        if node_error is not None:
            baris = node_error.start_point[0] + 1
            kolom = node_error.start_point[1] + 1

            jenis = "MISSING" if node_error.is_missing else "ERROR"

            print(
                f"[FILE ERROR] {path}:{baris}:{kolom}: "
                f"{jenis} ({node_error.type})"
            )


def main():
    if len(sys.argv) != 2:
        print("Penggunaan: python cek.py <folder>")
        sys.exit(1)

    folder = Path(sys.argv[1])

    if not folder.is_dir():
        print(f"Error: folder tidak ditemukan: {folder}")
        sys.exit(1)

    daftar_file = sorted(folder.rglob("*.py"))

    daftar_file = [
        path for path in daftar_file
        if not SKIP_DIRS.intersection(path.parts)
    ]

    if not daftar_file:
        print("Tidak ditemukan file Python.")
        return

    print(f"Memeriksa {len(daftar_file)} file Python...\n")

    for path in daftar_file:
        try:
            cek_file(path)
        except OSError as error:
            print(f"[READ ERROR] {path}: {error}")

    print("\nPemeriksaan selesai.")


if __name__ == "__main__":
    main()
