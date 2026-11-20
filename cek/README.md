# Tree-sitter Code Checker

Program sederhana untuk memeriksa file Python menggunakan Tree-sitter.

Program memiliki tiga fitur utama:

1. Mendeteksi komentar yang mengandung `TODO` atau `FIXME`.
2. Mendeteksi fungsi yang memiliki panjang lebih dari 30 baris.
3. Mendeteksi file Python yang syntax tree-nya memiliki kesalahan.

## 1. Persyaratan

- Python 3
- tree-sitter
- tree-sitter-python

Instal dependensi dengan perintah:

```bash
pip install tree-sitter tree-sitter-python
```

## 2. Struktur Folder

```text
cek/
├── cek.py
├── README.md
├── hasil_repo_nyata.txt
└── uji/
    ├── todo.py
    ├── fungsi_panjang.py
    └── error.py
```

## 3. Cara Menjalankan

Jalankan dari folder utama repository:

```bash
python cek/cek.py <folder>
```

Contoh menggunakan folder pengujian:

```bash
python cek/cek.py cek/uji
```

Program akan memeriksa seluruh file berekstensi `.py` di folder tersebut beserta subfoldernya.

## 4. Fitur Program

### A. Deteksi TODO/FIXME

Menggunakan Tree-sitter Query untuk menemukan komentar yang mengandung kata `TODO` atau `FIXME`.

Hasil menampilkan lokasi file, nomor baris, dan isi komentar.

### B. Deteksi Fungsi Panjang

Menggunakan query untuk menemukan node `function_definition`.

Jumlah baris dihitung berdasarkan posisi awal dan akhir node. Fungsi dilaporkan apabila memiliki lebih dari 30 baris.

Fungsi di dalam kelas dan fungsi bersarang juga ikut diperiksa.

### C. Deteksi Kesalahan Sintaks

Program memeriksa properti `root_node.has_error`.

Jika ditemukan kesalahan, program menelusuri syntax tree secara rekursif untuk menemukan node `ERROR` atau `MISSING` pertama.

## 5. Contoh Output

```text
Memeriksa 3 file Python...

[TODO/FIXME] cek/uji/todo.py:1: # TODO: lengkapi validasi input
[TODO/FIXME] cek/uji/todo.py:2: # FIXME: perbaiki pesan kesalahan
[FUNGSI PANJANG] cek/uji/fungsi_panjang.py:1: proses_data (33 baris)
[FILE ERROR] cek/uji/error.py:1:1: ERROR (ERROR)

Pemeriksaan selesai.
```

## 6. Hasil Pengujian pada Proyek Nyata

Pengujian dilakukan pada proyek CRUD Extractor yang berisi 16 file Python.

Hasil pemeriksaan:

- TODO/FIXME ditemukan: 0
- Fungsi dengan panjang lebih dari 30 baris: 4
- File dengan kesalahan sintaks: 0

Pemeriksaan manual dilakukan pada fungsi `_scan_token` di `lexer.py` dan `_primary` di `parser.py`.

Hasil pemeriksaan manual sesuai dengan hasil program, yaitu masing-masing 66 dan 32 baris.

Hasil lengkap pengujian tersimpan di `hasil_repo_nyata.txt`.
