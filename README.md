# Proposal Approval System (PAS)

### Deskripsi
Proposal Approval System (PAS) merupakan rancangan aplikasi sederhana menggunakan Python untuk membantu mengevaluasi persetujuan proposal kegiatan berdasarkan beberapa kriteria.

### Kriteria Penilaian
1. Kelengkapan proposal.
2. Persetujuan pembina.
3. Ketersediaan dana.
4. Ketersediaan jadwal.

### Model Logika
Sistem menggunakan empat variabel proposisi:

- K = Proposal lengkap
- B = Pembina menyetujui
- D = Dana mencukupi
- J = Jadwal tersedia

Rumus keputusan:

**A = K ∧ B ∧ D ∧ J**

Proposal disetujui apabila seluruh kriteria terpenuhi.

### Rencana Pengembangan
- Input data proposal.
- Evaluasi otomatis menggunakan logika Boolean.
- Menampilkan hasil dan alasan keputusan.
- Membuat tabel kebenaran dengan 16 kombinasi.
- Pengembangan antarmuka aplikasi.

### Teknologi
- Python
- Python Standard Library
- Command Line Interface (CLI)

### Status
Masih dalam tahap perancangan dan pengembangan awal backend Python.