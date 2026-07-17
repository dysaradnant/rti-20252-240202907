# 04-data

Folder ini berisi seluruh data yang digunakan selama proses penelitian, baik data mentah (raw data), data hasil preprocessing, maupun data yang digunakan sebagai input simulasi Adaptive Energy Scheduler.

Data pada folder ini menjadi dasar proses perhitungan **PV Model**, **Battery Model**, **Energy Demand Model**, hingga evaluasi performa **Adaptive Energy Scheduler**.

---

# Isi yang Diharapkan

Folder ini berisi beberapa jenis data sebagai berikut.

## 1. Dataset NASA POWER

Dataset cuaca historis yang digunakan sebagai sumber utama simulasi produksi energi panel surya.

Parameter yang digunakan meliputi:

- Solar Radiation
- Air Temperature
- Relative Humidity
- Wind Speed
- Date and Time

Format:

- CSV

---

## 2. Data Hasil Preprocessing

Dataset yang telah melalui proses validasi dan pembersihan data.

Meliputi:

- Missing Value Handling
- Normalisasi Format
- Konversi Timestamp
- Seleksi Parameter

Format:

- CSV

---

## 3. Data Produksi Energi Panel Surya

Output dari **PV Model**.

Data meliputi:

- PV Power (Watt)
- PV Energy (Wh)
- Solar Irradiance
- PV Efficiency

Format:

- CSV

---

## 4. Data Battery Model

Output simulasi baterai.

Meliputi:

- State of Charge (SOC)
- Charging
- Discharging
- Battery Capacity

Format:

- CSV

---

## 5. Data Energy Demand

Data kebutuhan energi sistem hidroponik.

Meliputi:

- Beban Sistem
- Konsumsi Energi
- Total Load

Format:

- CSV

---

## 6. Metadata Simulasi

Informasi setiap proses eksperimen.

Meliputi:

- Tanggal Simulasi
- Jumlah Data
- Parameter Simulasi
- Konfigurasi Scheduler
- Lama Simulasi

Format:

- TXT / CSV

---

# Struktur Folder

```
04-data/
│
├── raw/
│   └── POWER_Point_Hourly_20240101_20241231_007d55S_109d67E_LST.csv
│
├── preprocessing/
│   └── experiment_part1.csv
│
├── pv/
│   └── experiment_part1.csv
│
├── battery/
│   └── experiment_part2.csv.csv
│
├── load/
│   └── experiment_part2.csv.csv
│
├── metadata/
│   └── simulation_metadata.csv
│
└── README.md
```

---

# Catatan

Seluruh data pada folder ini merupakan **data mentah (raw data)** dan **data hasil preprocessing** yang digunakan sebagai masukan (input) pada proses simulasi.

Analisis statistik, perhitungan efisiensi, visualisasi grafik, serta hasil evaluasi **Rule-Based Scheduler** dan **Adaptive Energy Scheduler** tidak disimpan pada folder ini, melainkan pada folder **../06-output/**.

Folder **04-data** hanya berfungsi sebagai repositori data penelitian sehingga seluruh proses simulasi dapat direproduksi dengan menggunakan data yang sama.
