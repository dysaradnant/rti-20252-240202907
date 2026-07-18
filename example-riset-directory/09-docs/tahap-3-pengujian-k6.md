# Tahap 3 — Simulasi dan Pengujian Adaptive Energy Scheduler

**Status:** Selesai — simulasi satu tahun penuh menggunakan dataset NASA POWER (8.784 data per jam) telah dijalankan sebanyak **5 replikasi**, dan seluruh hasil tersimpan pada folder `output/`.

**Bergantung pada:** [tahap-2-implementasi-model.md](tahap-2-implementasi-model.md)

**Lokasi kode:** [../05-kode/simulasi/](../05-kode/simulasi/)

---

# Tujuan

Melakukan simulasi dan pengujian terhadap performa **Adaptive Energy Scheduler** dibandingkan **Rule-Based Scheduler** pada sistem hidroponik cerdas berbasis panel surya.

Pengujian dilakukan menggunakan dataset meteorologi NASA POWER selama satu tahun penuh untuk mengevaluasi:

- Efisiensi penggunaan energi.
- Produksi energi panel surya.
- Konsumsi energi sistem.
- State of Charge (SOC) baterai.
- Distribusi mode operasi sistem.
- Peningkatan performa Adaptive Energy Scheduler dibandingkan Rule-Based Scheduler.

---

# Deliverable

- [x] Dataset NASA POWER tahun 2024 berhasil divalidasi (8.784 data per jam).
- [x] Simulasi Photovoltaic Model berhasil dijalankan.
- [x] Simulasi Energy Demand Model berhasil dijalankan.
- [x] Simulasi Battery Model berhasil dijalankan.
- [x] Rule-Based Scheduler berhasil diimplementasikan sebagai baseline.
- [x] Adaptive Energy Scheduler berhasil diimplementasikan.
- [x] Multiple Run Experiment sebanyak **5 replikasi** berhasil dilakukan.
- [x] Seluruh output simulasi berhasil disimpan dalam format CSV dan Excel.
- [x] Grafik hasil simulasi berhasil dibuat menggunakan Matplotlib.
- [x] Ringkasan statistik penelitian berhasil dihasilkan.

---

# Desain Simulasi

## Pipeline Simulasi

```text
NASA POWER Dataset
        │
        ▼
Validasi Dataset
        │
        ▼
Preprocessing
        │
        ▼
Photovoltaic Model
        │
        ▼
Energy Demand Model
        │
        ▼
Battery Model
        │
        ▼
Rule-Based Scheduler
        │
        ├──────────────┐
        ▼              ▼
Adaptive Energy Scheduler
        │
        ▼
Multiple Run Experiment
        │
        ▼
Analisis Statistik
        │
        ▼
Visualisasi Hasil
```

---

# Struktur Program

```text
05-kode/

experiment_final_part1.py
experiment_final_part2.py
experiment_final_part3.py
experiment_final_part4.py

pv_model.py
battery_model.py
load_model.py
scheduler.py

output/
graph/
model/
```

---

# Konfigurasi Simulasi

| Parameter | Nilai |
|---|---:|
| Dataset | NASA POWER |
| Periode | Januari–Desember 2024 |
| Resolusi | Per Jam |
| Jumlah Data | 8.784 |
| Jumlah Replikasi | 5 |
| Bahasa Pemrograman | Python 3.x |

---

# Parameter Model

## Photovoltaic Model

| Parameter | Nilai |
|---|---:|
| Panel Surya | 100 Wp |
| Koefisien Temperatur | −0,0045 / °C |

---

## Battery Model

| Parameter | Nilai |
|---|---:|
| Kapasitas | 240 Wh |
| Efisiensi Charge | 95 % |
| Efisiensi Discharge | 95 % |
| Self-discharge | 0,02 %/jam |
| SOC Minimum | 20 % |
| SOC Maksimum | 100 % |

---

## Beban Sistem

| Aktuator | Daya |
|---|---:|
| Pompa Air | 18 W |
| Kipas Pendingin | 12 W |
| Lampu LED | 24 W |

---

## Adaptive Energy Scheduler

Scheduler menggunakan skor komposit berdasarkan:

| Parameter | Bobot |
|---|---:|
| State of Charge | 40 % |
| Energi Panel Surya | 30 % |
| Beban Sistem | 20 % |
| Temperatur | 10 % |

---

# Output Simulasi

Seluruh hasil simulasi disimpan pada folder:

```text
output/
```

dengan struktur:

```text
output/

experiment_part1.csv
experiment_part1.xlsx

experiment_part2.csv
experiment_part2.xlsx

experiment_part3.csv
experiment_part3.xlsx

experiment_final_run_1.csv
experiment_final_run_2.csv
experiment_final_run_3.csv
experiment_final_run_4.csv
experiment_final_run_5.csv

summary_final.csv
summary_final.xlsx
```

---

# Grafik Hasil

Seluruh visualisasi disimpan pada folder:

```text
graph/
```

berupa:

```text
battery_soc.png

daily_energy.png

comparison_efficiency.png
```

Grafik tersebut digunakan sebagai dasar analisis pada tahap berikutnya.

---

# Hasil Pengujian

## Ringkasan Lima Replikasi

| Run | Rule (%) | Adaptive (%) | Improvement (%) | Average SOC (%) |
|---|---:|---:|---:|---:|
| 1 | 39,98 | 41,98 | 2,00 | 50,77 |
| 2 | 40,40 | 42,19 | 1,79 | 50,94 |
| 3 | 39,29 | 41,62 | 2,33 | 50,62 |
| 4 | 40,44 | 42,21 | 1,77 | 50,99 |
| 5 | 39,18 | 41,56 | 2,38 | 50,59 |
| **Rata-rata** | **39,86** | **41,91** | **2,05** | **50,78** |

---

# Ringkasan Statistik

| Parameter | Nilai |
|---|---:|
| Total Produksi Energi PV | 177,51 kWh |
| Total Konsumsi Energi | 196,52 kWh |
| Rule Efficiency | 39,86 % |
| Adaptive Efficiency | 41,91 % |
| Mean Improvement | 2,05 % |
| Average SOC | 50,84 % |
| Standard Deviation SOC | 32,02 |

---

# Temuan Pengujian

Hasil simulasi menunjukkan bahwa:

- Adaptive Energy Scheduler secara konsisten menghasilkan efisiensi yang lebih tinggi dibandingkan Rule-Based Scheduler pada seluruh replikasi.
- Rata-rata peningkatan efisiensi sebesar **2,05%**.
- Rata-rata **State of Charge (SOC)** baterai mencapai **50,84%**.
- Total produksi energi panel surya (**177,51 kWh**) masih lebih rendah dibandingkan kebutuhan energi sistem (**196,52 kWh**), sehingga terjadi defisit energi tahunan sekitar **10,7%**.
- Kondisi **Emergency Mode** terjadi sekitar **44%** dari total waktu operasi, menunjukkan bahwa peningkatan kapasitas panel surya atau baterai masih diperlukan agar sistem dapat beroperasi secara mandiri sepanjang tahun.

---

# Catatan Lingkungan

- Simulasi dijalankan menggunakan **Python 3.x**.
- Analisis numerik menggunakan **NumPy** dan **Pandas**.
- Analisis statistik menggunakan **SciPy**.
- Visualisasi dibuat menggunakan **Matplotlib**.
- Dataset berasal dari **NASA POWER Hourly Dataset**.
- Seluruh simulasi dilakukan secara lokal menggunakan empat skrip utama (`experiment_final_part1.py` hingga `experiment_final_part4.py`).
- Multiple Run Experiment sebanyak **5 kali** digunakan untuk mengevaluasi konsistensi performa Adaptive Energy Scheduler sebelum dilakukan analisis statistik dan penyusunan manuskrip penelitian.
