# Evaluasi Performa Adaptive Energy Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas di Kondisi Fluktuasi Energi

**Target Publikasi:** SINTA 2 (Jurnal Teknologi Informasi / IoT / Energi Terbarukan) atau Scopus Q3–Q4

---

## Ringkasan

Penelitian ini mengevaluasi performa **Adaptive Energy Scheduler** dalam mengelola distribusi energi pada sistem hidroponik cerdas berbasis panel surya di bawah kondisi fluktuasi energi. Penelitian dilakukan melalui simulasi menggunakan **NASA POWER Hourly Dataset** selama satu tahun penuh (8.784 data) dengan membandingkan **Adaptive Energy Scheduler** terhadap **Rule-Based Scheduler** sebagai metode baseline.

Adaptive Energy Scheduler dikembangkan menggunakan pendekatan **skor komposit** yang mempertimbangkan empat parameter utama, yaitu **State of Charge (SOC) baterai**, **produksi energi panel surya**, **kebutuhan beban sistem**, dan **temperatur lingkungan**. Kinerja kedua metode dievaluasi menggunakan **Multiple Run Experiment** sebanyak lima replikasi serta dianalisis melalui statistik deskriptif, **Paired t-test**, **Independent t-test**, dan **Cohen's d**.

Hasil penelitian menunjukkan bahwa Adaptive Energy Scheduler mampu meningkatkan efisiensi energi rata-rata menjadi **41,91%**, lebih tinggi dibandingkan Rule-Based Scheduler sebesar **39,86%**, dengan peningkatan efisiensi sebesar **2,05%**. Selain itu, penelitian juga menunjukkan bahwa kapasitas panel surya yang digunakan masih menghasilkan defisit energi tahunan sekitar **10,7%**, sehingga peningkatan kapasitas panel surya maupun baterai direkomendasikan pada penelitian selanjutnya.

Detail roadmap penelitian tersedia pada:

`09-docs/rencana-penelitian.md`

---

# Struktur Direktori

| Folder | Isi |
|---|---|
| `00-admin/` | Administrasi penelitian, jadwal, dan dokumen pendukung |
| `01-proposal/` | Proposal penelitian |
| `02-literatur/` | Literatur, referensi jurnal, dan daftar pustaka |
| `03-teori/` | Studi literatur, perancangan sistem, dan metodologi |
| `04-data/` | Dataset NASA POWER dan hasil simulasi |
| `05-kode/` | Source code simulasi (Python) |
| `06-output/` | Hasil analisis statistik, tabel, dan grafik |
| `07-manuskrip/` | Manuskrip jurnal ilmiah |
| `08-laporan/` | Laporan penelitian lengkap |
| `09-docs/` | Roadmap dan dokumentasi setiap tahapan penelitian |

---

# Status Tahapan Penelitian

- [x] **Tahap 1 — Studi Literatur dan Perancangan Sistem** — *Selesai* (`09-docs/tahap-1-studi-literatur-dan-perancangan.md`)

- [x] **Tahap 2 — Implementasi Model Simulasi** — *Selesai* (`09-docs/tahap-2-implementasi-model.md`)

- [x] **Tahap 3 — Simulasi dan Pengujian Adaptive Energy Scheduler** — *Selesai* (`09-docs/tahap-3-simulasi-dan-pengujian.md`)

- [x] **Tahap 4 — Analisis Data dan Visualisasi** — *Selesai* (`09-docs/tahap-4-analisis-data-dan-visualisasi.md`)

- [x] **Tahap 5 — Penyusunan Manuskrip Jurnal** — *Selesai* (`09-docs/tahap-5-penyusunan-manuskrip.md`)

---

# Metodologi Penelitian

Penelitian dilaksanakan melalui lima tahapan utama.

```text
Tahap 1
│
├── Studi Literatur
├── Perancangan Sistem
└── Penentuan Parameter

        │
        ▼

Tahap 2
│
├── Photovoltaic Model
├── Energy Demand Model
├── Battery Model
└── Adaptive Energy Scheduler

        │
        ▼

Tahap 3
│
├── Simulasi Dataset NASA POWER
├── Multiple Run Experiment
└── Pengumpulan Data

        │
        ▼

Tahap 4
│
├── Statistik Deskriptif
├── Paired t-test
├── Independent t-test
├── Cohen's d
└── Visualisasi

        │
        ▼

Tahap 5
│
├── Penyusunan Manuskrip
├── Pembahasan
└── Publikasi
```

---

# Dataset Penelitian

| Parameter | Nilai |
|---|---|
| Dataset | NASA POWER Hourly Dataset |
| Periode | Januari–Desember 2024 |
| Resolusi Data | Per Jam |
| Jumlah Data | 8.784 |
| Missing Value | 0 |
| Duplicate Data | 0 |

---

# Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Bahasa Pemrograman | Python 3.x |
| Analisis Data | Pandas, NumPy |
| Statistik | SciPy |
| Visualisasi | Matplotlib |
| Dataset | NASA POWER |
| Dokumentasi | Markdown & Microsoft Word |

---

# Ringkasan Hasil Penelitian

| Parameter | Nilai |
|---|---:|
| Produksi Energi Panel Surya | 177,51 kWh |
| Konsumsi Energi Sistem | 196,52 kWh |
| Rule-Based Efficiency | 39,86 % |
| Adaptive Efficiency | 41,91 % |
| Peningkatan Efisiensi | 2,05 % |
| Average Battery SOC | 50,84 % |
| Defisit Energi Tahunan | 10,7 % |

---

# Kontribusi Penelitian

Penelitian ini memberikan beberapa kontribusi sebagai berikut.

- Mengembangkan **Adaptive Energy Scheduler** berbasis skor komposit untuk sistem hidroponik cerdas.
- Mengintegrasikan **Photovoltaic Model**, **Battery Model**, dan **Energy Demand Model** dalam satu kerangka simulasi.
- Melakukan evaluasi menggunakan **NASA POWER Hourly Dataset** selama satu tahun penuh sehingga menghasilkan analisis yang lebih representatif.
- Membandingkan Adaptive Energy Scheduler dengan Rule-Based Scheduler menggunakan **Multiple Run Experiment**.
- Memvalidasi hasil menggunakan analisis statistik sehingga meningkatkan keandalan hasil penelitian.

---

# Laporan Penelitian

Laporan penelitian lengkap yang mencakup metodologi, implementasi, hasil simulasi, analisis statistik, pembahasan, dan kesimpulan tersedia pada:

`08-laporan/laporan-penelitian.md`

---

# Manuskrip Jurnal

Manuskrip lengkap tersedia pada:

- `07-manuskrip/manuskrip-jurnal.md`
- `07-manuskrip/manuskrip-jurnal.docx`

Dokumen tersebut telah memuat:

- Judul
- Abstrak (Indonesia dan Inggris)
- Pendahuluan
- Metodologi
- Hasil dan Pembahasan
- Simpulan
- Daftar Pustaka

dan siap dipindahkan ke template jurnal tujuan.

---

# Author

**Dysar**
