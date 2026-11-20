# Proposal Draf Proyek Tree-sitter

**Judul:** Pemeriksa Kualitas Kode Python untuk Backend Aplikasi Web Enterprise  
**Nama:** Imam Miftahul U'lum | **Kelas:** 2A  
**Status:** Usulan awal turunan mini project Tugas 6; dapat diselaraskan dengan topik pilihan akhir.

1. **Judul.** Pemeriksa Kualitas Kode Python untuk Backend Aplikasi Web Enterprise.
2. **Masalah dan pengguna.** Developer, reviewer, dan QA perlu menemukan komentar TODO/FIXME, fungsi terlalu panjang, dan file Python yang memiliki kesalahan sintaks di repository backend.
3. **Mengapa AI saja belum cukup.** AI membantu review, tetapi hasilnya probabilistik. Tree-sitter memberikan pemeriksaan deterministik yang dapat dijalankan berulang dan diintegrasikan ke CI.
4. **Bahasa/framework.** Python backend; framework-agnostic pada tahap awal, dengan contoh integrasi FastAPI. Grammar `tree-sitter-python`, binding Python `tree-sitter`.
5. **Contoh.** Deteksi `# TODO: validate request`, fungsi >30 baris, dan file yang parse tree-nya memiliki ERROR/MISSING. Jangan deteksi komentar biasa tanpa TODO/FIXME atau fungsi <=30 baris.
6. **Query S-expression.** `((comment) @comment (#match? @comment "TODO|FIXME"))`
7. **Output.** Laporan terminal dengan kategori, path, nomor baris, nama fungsi/jumlah baris, dan posisi error.
8. **Evaluasi.** CRUD Extractor (16 file Python) dan corpus sintetis. Baseline: 4 fungsi panjang, 0 TODO/FIXME setelah query diperbaiki, 0 file error. Dua fungsi diverifikasi manual: 66 dan 32 baris. Tahap lanjutan: minimal 20 sampel manual dan contoh backend FastAPI.
9. **Rencana/risiko.** Minggu 1 aturan dan corpus; minggu 2 query dan pengurangan false positive; minggu 3 uji repository dan validasi manual; minggu 4 integrasi CLI/CI dan dokumentasi. Risiko: false positive, encoding, dan repository besar; mitigasi dengan corpus, decode replacement, dan skip direktori dependency.
