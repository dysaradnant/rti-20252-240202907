# WS-12: Result Presentation & Visualization

> **Bab 12 — Penyajian Hasil & Visualisasi**

---

## Ringkasan Materi

### Data → Insight Model

```
Validated Data → Structured Presentation → Visualization → Pattern Recognition → Insight
```

Penyajian **mendahului** analisis. Tabel dan grafik membantu peneliti "melihat" data sebelum menghitung. Langsung ke uji statistik tanpa visualisasi berisiko kesimpulan yang secara teknis benar tapi kontekstual salah (Anscombe's Quartet, 1973).

### Tabel = Presisi, Grafik = Pola

Keduanya **saling melengkapi**:
- Tabel: angka presisi, self-contained (dipahami tanpa teks), sortable
- Grafik: pola visual, tren, perbandingan cepat

### Jenis Grafik Berdasarkan Tujuan

| Tujuan | Jenis Grafik |
|--------|-------------|
| Perbandingan antar-skenario | Bar chart (grouped/stacked) |
| Distribusi per-skenario | Box plot / violin plot |
| Tren temporal | Line chart |
| Korelasi dua variabel | Scatter plot |
| Proporsi (total = 100%) | Pie chart (hati-hati!) |

### Contoh Tabel Hasil yang Baik

| Model | Accuracy (%) | F1-Score (%) | Training Time (min) |
|-------|-------------|-------------|---------------------|
| BERT | 88.4 ± 1.2 | 87.1 ± 1.4 | 45.2 ± 3.1 |
| LSTM | 86.1 ± 1.8 | 84.5 ± 2.0 | 12.8 ± 1.2 |
| SVM | 82.3 ± 0.9 | 80.7 ± 1.1 | 0.3 ± 0.1 |

*N=10 per model. Mean ± std. Diurutkan berdasarkan Accuracy.*

### Visualization Bias — Yang Harus Dihindari

| Bias | Deskripsi | Dampak |
|------|----------|--------|
| Truncated axis | Y tidak dari 0 | Memperbesar perbedaan kecil |
| Inconsistent scale | Dua grafik skala beda | Perbandingan menyesatkan |
| Cherry-picked data | Hanya tampilkan yang "menang" | Selektif, tidak jujur |
| 3D effects | Efek 3D tanpa dimensi data ke-3 | Distorsi tanpa informasi |
| Missing error bar | Tidak ada variabilitas | Menyembunyikan ketidakpastian |

### Engineering vs Research Presentation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan grafik | Dashboard monitoring | Mendukung argumen ilmiah |
| Informasi wajib | KPI, threshold | Mean, std, CI, N, p-value |
| Bias handling | Less critical | Wajib dihindari (peer-review) |

---

## Template A.12 — Result Presentation Plan

```
RESULT PRESENTATION PLAN

Research Question : Bagaimana kinerja Adaptive Energy Scheduler dibandingkan dengan Rule-Based Scheduler dalam mengoptimalkan penggunaan energi pada sistem panel surya menggunakan dataset NASA POWER?
Metrik Utama      : Rule-Based Efficiency (%), Adaptive Scheduler Efficiency (%), Improvement (%), State of Charge (SOC), Total Load (Wh), PV Energy (Wh)

Tabel Hasil:
| Skenario | Rule Efficiency (Mean ± Std) | Adaptive Efficiency (Mean ± Std) | n |
|----------|----------------------|----------------------|---|
| Adaptive Energy Scheduler | 40.40 ± 0.14 % | 42.19 ± 0.07 % | 5 |

Visualisasi yang Direncanakan:
| # | Jenis Grafik | Pesan Utama | Metrik |
|---|-------------|-------------|--------|
| 1 | Bar Chart | Perbandingan Rule-Based dan Adaptive Scheduler | Rule Efficiency vs Adaptive Efficiency |
| 2 | Line Chart | Perubahan SOC selama eksperimen | SOC (%) |
| 2 | Line Chart | Produksi energi panel surya harian  | PV Energy (Wh) |

Bias Check:
  [✓] Y-axis mulai dari 0 (atau dijustifikasi)
  [✓] Error bar/CI ditampilkan
  [✓] Semua data disertakan (tidak cherry-picked)
  [✓] Tidak menggunakan grafik 3D 
```

---

## Latihan 1 — Tabel Hasil

Buat tabel hasil eksperimen Anda (boleh dengan data simulasi jika belum punya data riil).

| Skenario | Rule Efficiency (Mean ± Std) | Adaptive Efficiency (Mean ± Std) | Average SOC | Jumlah Run |
|----------|----------------------|----------------------|---|
| Adaptive Energy Scheduler | 40.40 ± 0.14 % | 42.19 ± 0.07 % | 51.0 % | 5 |

Ringkasan Hasil Setiap Run

| Run | Rule Efficiency (%) | Adaptive Efficiency (%) | Improvement (%) | Average SOC (%) |
|-----|---------------------|------------------------ |-----------------|-----------------|
| 1 | 40.50 | 42.24 | 1.74 | 51.05 |
| 2 | 40.17 | 42.07 | 1.91 | 50.82 |
| 3 | 40.40 | 42.19 | 1.79 | 50.94 |
| 4 | 40.46 | 42.22 | 1.76 | 51.01 |
| 5 | 40.49 | 42.24 | 1.74 | 51.05 |

Statistik Deskriptif
| Parameter | Nilai |
|-----|---------------------|
| Mean Rule Efficiency | 40.40 % |
| Standard Deviasi Rule | 0.14 |
| Mean Adaptive Efficiency | 42.19 % |
| Standard Deviasi Adaptive | 0.07 |
| Mean Improvement | 1.79 % |
| Jumlah Dataset | 8784 data |

**Checklist tabel:**
- [✓] Self-contained (judul jelas, satuan ada, N tercantum)
- [✓] Mean ± std (bukan single number)
- [✓] Diurutkan berdasarkan metrik utama
- [✓] Format konsisten di semua baris

---

## Latihan 2 — Rencana Visualisasi

Rencanakan 2-3 grafik untuk menyajikan data dari Latihan 1. Setiap grafik = satu pesan.

| # | Jenis Grafik | Pesan | Data yang Digunakan |
|---|-------------|-------|---------------------|
| 1 | Bar Chart | Adaptive Scheduler memiliki efisiensi lebih tinggi dibanding Rule-Based Scheduler. | Mean Rule Efficiency dan Mean Adaptive Efficiency |
| 2 | Line Chart | Menampilkan perubahan State of Charge (SOC) selama proses eksperimen. | SOC setiap jam hasil simulasi |
| 3 | Line Chart | Menampilkan perubahan produksi energi panel surya berdasarkan dataset NASA POWER. | PV Energy (Wh) |

---

## Latihan 3 — Bias Detection

Evaluasi visualisasi berikut untuk bias (skenario dari contoh):

**Skenario:** Metode A = 91.2%, Metode B = 90.8%. Bar chart dengan Y-axis mulai dari 90%.

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah Y-axis menyesatkan? | Tidak. Seluruh grafik menggunakan skala yang konsisten. |
| Apakah error bar ditampilkan? | Ya. Nilai standar deviasi dicantumkan pada hasil. |
| Apakah semua kondisi ditampilkan? | Ya. Seluruh lima eksperimen ditampilkan tanpa menghilangkan data tertentu. |
| Apa solusinya jika terjadi bias? | Menggunakan skala yang sama, tidak melakukan cherry-picking data, serta menampilkan error bar dan seluruh hasil eksperimen. |

**Evaluasi grafik Anda sendiri dari Latihan 2:**
- [✓] Semua bias check lulus
- [✓] Tidak ditemukan bias visual yang signifikan

---

## Refleksi

> Mengapa tabel dan grafik keduanya diperlukan — tidak cukup salah satu saja? Pernahkah Anda membuat grafik yang (tanpa sengaja) menyesatkan?

> Penyajian hasil penelitian tidak cukup hanya menggunakan tabel atau hanya menggunakan grafik. Tabel memberikan informasi numerik yang presisi sehingga memudahkan pembaca mengetahui nilai rata-rata, standar deviasi, dan jumlah eksperimen. Sebaliknya, grafik memudahkan pembaca melihat pola, tren, dan perbandingan antar-metode secara cepat. Oleh karena itu, keduanya saling melengkapi dalam menyampaikan hasil penelitian.
> Dalam penelitian ini saya berusaha menghindari bias visual dengan menggunakan skala sumbu yang konsisten, tidak menghilangkan data yang tidak sesuai harapan, serta menyajikan seluruh hasil eksperimen beserta statistik deskriptifnya. Dengan demikian, visualisasi yang disajikan tidak hanya menarik secara visual, tetapi juga tetap akurat dan dapat dipertanggungjawabkan secara ilmiah.
