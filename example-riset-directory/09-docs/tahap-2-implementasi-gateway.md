# Tahap 2 — Implementasi Model Simulasi

**Status:** Selesai  
**Acuan penelitian:** [tahap-1-studi-literatur-dan-perancangan.md](tahap-1-studi-literatur-dan-perancangan.md)  
**Lokasi kode:** [../05-kode/simulasi/](../05-kode/simulasi/)

---

## Tujuan

Mengimplementasikan model simulasi sistem hidroponik cerdas berbasis panel surya menggunakan Python dengan mengintegrasikan beberapa komponen utama, yaitu:

- Photovoltaic (PV) Model
- Energy Demand Model
- Battery Model
- Adaptive Energy Scheduler

Seluruh model dikembangkan untuk mengevaluasi performa sistem pada kondisi fluktuasi energi menggunakan dataset NASA POWER selama satu tahun penuh.

---

## Deliverable

- [x] Implementasi **Photovoltaic Model** (`pv_model.py`) untuk menghitung produksi energi panel surya berdasarkan radiasi matahari dan koreksi temperatur.
- [x] Implementasi **Energy Demand Model** (`load_model.py`) yang mensimulasikan konsumsi energi pompa air, kipas, dan lampu LED berdasarkan kondisi lingkungan.
- [x] Implementasi **Battery Model** (`battery_model.py`) menggunakan baterai lithium-ion dengan efisiensi charge/discharge dan mekanisme self-discharge.
- [x] Implementasi **Adaptive Energy Scheduler** (`scheduler.py`) menggunakan skor komposit berdasarkan SOC, energi surya, beban sistem, dan suhu.
- [x] Implementasi **Rule-Based Scheduler** sebagai metode pembanding (baseline).
- [x] Integrasi seluruh model ke dalam pipeline simulasi (`experiment_final_part1.py` sampai `experiment_final_part4.py`).
- [x] Validasi dataset NASA POWER (8.784 data per jam) tanpa missing value maupun data duplikat.
- [x] Penyimpanan hasil simulasi ke format **CSV** dan **Excel**.
- [x] Pembuatan metadata eksperimen secara otomatis.
- [x] Dokumentasi penggunaan melalui `README.md`.

---

## Arsitektur Implementasi

Pipeline simulasi terdiri atas beberapa tahapan berikut.

```text
NASA POWER Dataset
        │
        ▼
Data Validation & Preprocessing
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
Simulation Output
        │
        ▼
CSV / Excel / Graph
```

---

## Struktur Implementasi

```text
05-kode/
│
├── pv_model.py
├── battery_model.py
├── load_model.py
├── scheduler.py
├── experiment_final_part1.py
├── experiment_final_part2.py
├── experiment_final_part3.py
├── experiment_final_part4.py
│
├── output/
│   ├── experiment_part1.csv
│   ├── experiment_part2.csv
│   ├── experiment_part3.csv
│   ├── summary_final.csv
│   └── summary_final.xlsx
│
└── graph/
    ├── battery_soc.png
    ├── daily_energy.png
    └── comparison_efficiency.png
```

---

## Hasil Verifikasi

Implementasi berhasil diverifikasi menggunakan dataset **NASA POWER** periode Januari–Desember 2024 sebanyak **8.784 data**.

### Validasi Dataset

- Jumlah data : **8.784**
- Missing value : **0**
- Duplicate data : **0**
- Format waktu berhasil diproses menjadi data time-series.

---

### Photovoltaic Model

Model berhasil menghasilkan estimasi produksi energi panel surya berdasarkan:

- Radiasi matahari
- Temperatur lingkungan
- Efisiensi panel surya

Output:

- Energi PV per jam
- Energi PV harian
- Total energi tahunan

Total energi yang dihasilkan:

**177,51 kWh**

---

### Energy Demand Model

Model beban berhasil mensimulasikan konsumsi energi:

- Pompa air
- Kipas pendingin
- Lampu LED

Total konsumsi energi:

**196,52 kWh**

---

### Battery Model

Battery Model berhasil menghitung:

- Charging
- Discharging
- Self-discharge
- State of Charge (SOC)

Hasil:

- Average SOC : **50,84%**
- Standard Deviation : **32,02**

---

### Adaptive Energy Scheduler

Adaptive Energy Scheduler berhasil menentukan mode operasi berdasarkan skor komposit.

Mode operasi:

- Normal Operation
- Adaptive Saving
- Priority Pump
- Emergency Mode

Performa rata-rata:

| Parameter | Nilai |
|-----------|------:|
| Adaptive Efficiency | **41,91 %** |
| Rule-Based Efficiency | **39,86 %** |
| Improvement | **2,05 %** |

---

## Hasil Visualisasi

Visualisasi yang berhasil dihasilkan meliputi:

- Battery State of Charge (SOC)
- Daily PV Energy
- Rule vs Adaptive Efficiency

Seluruh grafik berhasil diekspor ke folder:

```text
graph/
```

---

## Catatan Lingkungan

- Bahasa pemrograman menggunakan **Python 3.x**.
- Analisis data menggunakan **Pandas** dan **NumPy**.
- Perhitungan statistik menggunakan **SciPy**.
- Visualisasi menggunakan **Matplotlib**.
- Dataset berasal dari **NASA POWER Hourly Dataset**.
- Simulasi dilakukan secara lokal menggunakan empat tahap skrip (`experiment_final_part1.py` hingga `experiment_final_part4.py`).
- Setiap eksperimen direplikasi sebanyak **5 kali** dengan variasi acak ±3% untuk mengevaluasi konsistensi performa Adaptive Energy Scheduler.
