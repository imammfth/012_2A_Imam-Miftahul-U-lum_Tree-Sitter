# Laporan Tugas Awal Tree-sitter

**Nama:** Imam Miftahul U'lum  
**Kelas:** 2A  
**Kode folder:** 012  
**Mata kuliah:** PLP  
**Tanggal:** 20 November 2026

## Ringkasan
Enam tugas dikerjakan menggunakan Tree-sitter dan binding Python: membaca syntax tree, node explorer, query, grammar DSL filter, highlight, dan mini project pemeriksa kode Python.

## Tugas 1 — Membaca syntax tree
Parser Python diuji pada assignment, fungsi, if/else, dan class. Node anonim seperti `def`, tanda kurung, dan titik dua dibedakan dari node bernama seperti `identifier`, `parameters`, dan `block`. Fungsi yang kehilangan titik dua menghasilkan `ERROR`. Hasil disimpan di `tugas1-3/output/hasil_tugas1.txt`. Catatan: bukti prediksi manual sebelum parsing sebaiknya ditambahkan jika tersedia.

## Tugas 2 — Node explorer
`jelajah.py` menelusuri node bernama secara rekursif, menampilkan indentasi, tipe, posisi, dan field. Diuji pada `parser.py` sebanyak 391 baris; output 3.351 baris dan tidak ditemukan `ERROR`/`MISSING`.

## Tugas 3 — Query pertama
Query berhasil menemukan identifier, nama fungsi `tambah` dan `sapa`, jumlah parameter 2 dan 1, dua pemanggilan `print()`, serta import `os`, `pathlib`, dan `Path`. Hasil ada di `tugas1-3/output/`.

## Tugas 4 — Grammar DSL filter
Grammar `filter` mendukung perbandingan string/angka/Boolean, `and`, `or`, tanda kurung, `not`, `in`, dan `contains`. Prioritas `and` lebih tinggi daripada `or`. `tree-sitter test`: 8 lulus, 0 gagal.

## Tugas 5 — Highlight
`queries/highlights.scm` menangkap keyword, operator, string, angka, Boolean, nama field, dan tanda baca. `tree-sitter query` menunjukkan semua capture cocok; HTML highlight berhasil dibuat. Tampilan warna di browser masih perlu pemeriksaan visual.

## Tugas 6 — Mini project checker
`cek/cek.py` mendeteksi TODO/FIXME, fungsi lebih dari 30 baris, dan file dengan syntax error. Uji sintetis berhasil untuk ketiga fitur. Pada CRUD Extractor (16 file Python): 0 TODO/FIXME, 4 fungsi panjang, 0 file error. Validasi manual: `lexer._scan_token` 66 baris dan `parser._primary` 32 baris. README dibuat di `cek/README.md`.

## Kendala dan catatan AI
- `module.exports` tidak cocok dengan konfigurasi ES module; diganti `export default`, lalu `tree-sitter generate` berhasil.
- Konflik associativity pada `and` dan `or` diselesaikan dengan `prec.left(2)` dan `prec.left(1)`.
- Query TODO awal menghasilkan false positive; predicate dibungkus menjadi `((comment) @c (#match? @c "TODO|FIXME"))`.
- Struktur import diperiksa melalui `jelajah.py` sebelum query ditulis.
- Pemeriksaan visual HTML highlight dan screenshot asli untuk setiap tugas masih perlu ditambahkan sebelum penyerahan.
