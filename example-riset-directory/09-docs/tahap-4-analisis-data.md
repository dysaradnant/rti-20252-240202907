# Tahap 4 — Analisis Data dan Visualisasi

**Status:** Selesai — seluruh pipeline analisis telah dijalankan menggunakan hasil simulasi Adaptive Energy Scheduler sebanyak **5 replikasi**. Seluruh tabel, grafik, dan ringkasan statistik berhasil dihasilkan pada folder `output/` dan `graph/`.

**Bergantung pada:** [tahap-3-simulasi-dan-pengujian.md](tahap-3-simulasi-dan-pengujian.md)

**Lokasi kode:** [../05-kode/analysis/](../05-kode/analysis/)

---

# Tujuan

Mengolah seluruh data hasil simulasi menjadi statistik deskriptif, analisis inferensial, serta visualisasi yang digunakan sebagai dasar penyusunan hasil penelitian.

Analisis dilakukan terhadap:

- Produksi energi panel surya.
- Konsumsi energi sistem.
- Efisiensi Rule-Based Scheduler.
- Efisiensi Adaptive Energy Scheduler.
- State of Charge (SOC) baterai.
- Distribusi mode operasi sistem.
- Perbandingan hasil dengan penelitian acuan.

---

# Deliverable

- [x] Pengolahan seluruh output simulasi menjadi dataset analisis.
- [x] Perhitungan statistik deskriptif.
- [x] Perhitungan rata-rata efisiensi setiap metode.
- [x] Perhitungan peningkatan efisiensi Adaptive Energy Scheduler.
- [x] Perhitungan State of Charge (SOC).
- [x] Perhitungan total produksi energi panel surya.
- [x] Perhitungan total konsumsi energi.
- [x] Uji statistik (Paired t-test).
- [x] Uji Independent t-test.
- [x] Perhitungan Cohen's d.
- [x] Pembuatan grafik penelitian.
- [x] Penyusunan tabel hasil penelitian.

---

# Desain Analisis

## Struktur Program

```text
05-kode/analysis/

descriptive_statistics.py

paired_ttest.py

independent_ttest.py

cohens_d.py

visualization.py

summary.py
```

Pipeline analisis dijalankan secara berurutan sehingga seluruh hasil penelitian dapat direproduksi secara otomatis.

---

# Pipeline Analisis

```text
Output Simulasi
        │
        ▼
Import Data CSV
        │
        ▼
Validasi Dataset
        │
        ▼
Statistik Deskriptif
        │
        ▼
Perhitungan Efisiensi
        │
        ▼
Analisis SOC
        │
        ▼
Uji Statistik
        │
        ▼
Visualisasi
        │
        ▼
Ringkasan Hasil Penelitian
```

---

# Statistik Deskriptif

Parameter yang dianalisis meliputi:

- Produksi energi panel surya.
- Konsumsi energi sistem.
- Rule Efficiency.
- Adaptive Efficiency.
- Improvement.
- Battery State of Charge (SOC).

Statistik yang dihitung meliputi:

- Mean
- Minimum
- Maximum
- Standard Deviation

---

# Uji Statistik

Evaluasi performa dilakukan menggunakan dua pendekatan statistik.

## Paired t-test

Digunakan untuk membandingkan efisiensi Rule-Based Scheduler dan Adaptive Energy Scheduler pada data simulasi yang identik.

Hasil:

| Parameter | Nilai |
|---|---:|
| t-statistic | 30,82 |
| p-value | < 0,001 |

Hasil menunjukkan bahwa Adaptive Energy Scheduler memiliki performa yang **berbeda secara signifikan** dibandingkan Rule-Based Scheduler.

---

## Independent t-test

Digunakan sebagai analisis pendukung untuk mengevaluasi perbedaan rata-rata efisiensi antar metode.

| Parameter | Nilai |
|---|---:|
| t-statistic | 2,61 |
| p-value | 0,009 |

---

## Effect Size

Perhitungan menggunakan Cohen's d.

| Parameter | Nilai |
|---|---:|
| Cohen's d | 0,04 |

Nilai tersebut menunjukkan bahwa ukuran efek peningkatan efisiensi masih tergolong kecil meskipun signifikan secara statistik.

---

# Ringkasan Hasil

## Efisiensi Sistem

| Parameter | Nilai |
|---|---:|
| Rule-Based Efficiency | 39,86 % |
| Adaptive Efficiency | 41,91 % |
| Mean Improvement | 2,05 % |

Adaptive Energy Scheduler memberikan peningkatan efisiensi dibandingkan Rule-Based Scheduler pada seluruh replikasi simulasi.

---

## Produksi dan Konsumsi Energi

| Parameter | Nilai |
|---|---:|
| Produksi Energi Panel Surya | 177,51 kWh |
| Konsumsi Energi Sistem | 196,52 kWh |
| Defisit Energi | 10,7 % |

Hasil menunjukkan bahwa kapasitas panel surya dan baterai pada konfigurasi saat ini masih belum mampu memenuhi kebutuhan energi sistem selama satu tahun penuh.

---

## Battery State of Charge (SOC)

| Parameter | Nilai |
|---|---:|
| Average SOC | 50,84 % |
| Standard Deviation | 32,02 |

Battery Model berhasil menjaga kondisi baterai pada rata-rata sekitar 50%, meskipun masih terjadi siklus pengosongan mendalam (*deep cycling*) pada periode tertentu.

---

## Distribusi Mode Operasi

| Mode | Persentase |
|---|---:|
| Emergency Mode | 44 % |
| Priority Pump | 24 % |
| Adaptive Saving | 18 % |
| Normal Operation | 14 % |

Distribusi tersebut menunjukkan bahwa kondisi kekurangan energi masih cukup sering terjadi, terutama pada musim dengan intensitas radiasi matahari rendah.

---

# Visualisasi

Grafik yang dihasilkan meliputi:

```text
graph/

battery_soc.png

daily_energy.png

comparison_efficiency.png
```

Visualisasi digunakan untuk memperlihatkan:

- dinamika Battery State of Charge,
- produksi energi panel surya,
- perbandingan Rule-Based dan Adaptive Energy Scheduler.

---

# Perbandingan dengan Penelitian Acuan

Hasil penelitian dibandingkan dengan penelitian Wardhana dkk. (2025).

| Aspek | Penelitian Acuan | Penelitian Ini |
|---|---:|---:|
| Durasi Pengujian | 2 minggu | 1 tahun |
| Efisiensi | 69–74 % | 39,86–41,91 % |
| Uji Statistik | Tidak ada | Ada |
| Adaptive Scheduler | Tidak | Ya |

Evaluasi selama satu tahun memberikan gambaran yang lebih realistis terhadap kondisi operasional sistem dibandingkan pengujian jangka pendek.

---

# Output Analisis

Seluruh hasil analisis berhasil diekspor dalam format:

```text
output/

summary_final.csv

summary_final.xlsx
```

serta visualisasi:

```text
graph/

comparison_efficiency.png

battery_soc.png

daily_energy.png
```

---

# Temuan Penelitian

Beberapa temuan utama dari analisis adalah sebagai berikut.

- Adaptive Energy Scheduler meningkatkan efisiensi rata-rata sebesar **2,05%** dibandingkan Rule-Based Scheduler.
- Perbedaan kedua metode signifikan secara statistik (**p < 0,001**).
- Ukuran efek masih kecil (**Cohen's d = 0,04**), sehingga peningkatan performa belum terlalu besar secara praktis.
- Produksi energi panel surya masih lebih rendah dibandingkan kebutuhan energi sistem, sehingga terjadi defisit energi tahunan sekitar **10,7%**.
- Kondisi **Emergency Mode** terjadi sekitar **44%** dari total waktu operasi, menunjukkan bahwa peningkatan kapasitas panel surya dan baterai masih diperlukan untuk mencapai sistem yang mandiri energi.

---

# Catatan untuk Tahap 5

Seluruh tabel, grafik, dan hasil analisis pada tahap ini menjadi dasar penyusunan **manuskrip jurnal ilmiah**.

Data yang dihasilkan telah memenuhi kebutuhan untuk:

- Bab Hasil dan Pembahasan.
- Tabel penelitian.
- Gambar penelitian.
- Analisis statistik.
- Kesimpulan penelitian.
- Perbandingan dengan penelitian terdahulu.

Dengan demikian, penelitian telah siap memasuki tahap akhir, yaitu penyusunan artikel ilmiah sesuai template jurnal SINTA 2 atau Scopus.
