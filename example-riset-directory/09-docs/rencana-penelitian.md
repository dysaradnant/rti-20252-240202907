# Rencana Penelitian: Evaluasi Adaptive Energy Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas

## 1. Ringkasan

| Item | Keterangan |
|---|---|
| Judul | Performance Evaluation of an Adaptive Energy Scheduler Based on Solar Photovoltaic for Smart Hydroponic Systems under Energy Fluctuation Conditions |
| Target Publikasi | SINTA 2 (Jurnal RESTI/JTIIK/Telematika) atau Scopus Q3–Q4 |
| Stack | Python, NASA POWER Dataset, Pandas, NumPy, Matplotlib, OpenPyXL |
| Masalah | Fluktuasi intensitas radiasi matahari menyebabkan produksi energi panel surya berubah-ubah sehingga Rule-Based Scheduler kurang mampu mengoptimalkan distribusi energi dan menjaga kestabilan baterai pada sistem hidroponik cerdas. |
| Solusi | Adaptive Energy Scheduler yang mengintegrasikan Photovoltaic Model, Battery Model, dan Energy Demand Model untuk mengoptimalkan distribusi energi secara adaptif berdasarkan kondisi energi yang tersedia. |

## 2. Alur Kerja (Roadmap)

Setiap tahap memiliki file rencana detail tersendiri agar dokumentasi penelitian lebih terstruktur.

- [x] **Tahap 1** — [Studi Literatur & Perancangan Sistem](tahap-1-studi-literatur-dan-perancangan.md) — *Selesai*
- [x] **Tahap 2** — [Implementasi Photovoltaic Model, Battery Model, dan Energy Demand Model](tahap-2-implementasi-model.md) — *Selesai*
- [x] **Tahap 3** — [Implementasi Adaptive Energy Scheduler & Simulasi](tahap-3-adaptive-energy-scheduler.md) — *Selesai*
- [x] **Tahap 4** — [Analisis Data & Visualisasi Hasil](tahap-4-analisis-dan-visualisasi.md) — *Selesai*
- [ ] **Tahap 5** — [Penyusunan Paper Jurnal](tahap-5-draf-paper.md) — *Berikutnya*

---

## 3. Hasil Penelitian

Hasil simulasi menggunakan dataset **NASA POWER** tahun 2024 (8.784 data) menunjukkan bahwa Adaptive Energy Scheduler memberikan peningkatan performa dibandingkan Rule-Based Scheduler.

| Parameter | Hasil |
|---|---:|
| Dataset | NASA POWER (2024) |
| Jumlah Data | 8.784 |
| Jumlah Simulasi | 5 Kali |
| Mean Rule Efficiency | 39,86 % |
| Mean Adaptive Efficiency | 41,91 % |
| Mean Improvement | 2,05 % |
| Average Battery SOC | 50,78 % |

Visualisasi yang dihasilkan meliputi:

- Daily PV Energy
- Battery State of Charge (SOC)
- Rule vs Adaptive Efficiency

---

## 4. Catatan

Dokumen ini merupakan indeks utama penelitian. Seluruh detail implementasi, proses simulasi, analisis statistik, visualisasi hasil, serta penyusunan manuskrip jurnal didokumentasikan pada setiap file `tahap-N-*.md` dan diperbarui sesuai perkembangan penelitian.

Target akhir penelitian adalah menghasilkan manuskrip ilmiah yang siap disubmit ke jurnal **SINTA 2** atau **Scopus** dengan kontribusi berupa evaluasi performa **Adaptive Energy Scheduler** pada sistem hidroponik cerdas berbasis panel surya menggunakan dataset NASA POWER.
