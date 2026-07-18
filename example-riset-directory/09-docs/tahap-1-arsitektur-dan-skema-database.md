# Tahap 1 — Studi Literatur dan Perancangan Sistem

**Status:** Selesai

---

## 1. Komponen Sistem

Sistem yang dikembangkan merupakan integrasi **Internet of Things (IoT)** dengan **panel surya** dan **Adaptive Energy Scheduler** untuk mengelola distribusi energi pada sistem hidroponik cerdas di daerah dengan fluktuasi energi.

Komponen utama sistem terdiri atas:

1. **NASA POWER Dataset**
   - Menyediakan data meteorologi per jam sebagai masukan simulasi.
   - Variabel yang digunakan meliputi:
     - Radiasi matahari (*ALLSKY_SFC_SW_DWN*)
     - Suhu udara (*T2M*)
     - Kelembaban relatif (*RH2M*)
     - Kecepatan angin (*WS10M*)

2. **Photovoltaic (PV) Model**
   - Menghitung energi listrik yang dihasilkan panel surya berdasarkan radiasi matahari.
   - Memperhitungkan koreksi temperatur terhadap efisiensi panel.

3. **Energy Demand Model**
   - Menghitung kebutuhan energi sistem hidroponik.
   - Beban meliputi:
     - Pompa air
     - Kipas pendingin
     - Lampu LED

4. **Battery Model**
   - Mensimulasikan proses pengisian (*charging*) dan penggunaan energi (*discharging*).
   - Menghitung **State of Charge (SOC)** setiap jam.
   - Memperhitungkan efisiensi baterai dan *self-discharge*.

5. **Adaptive Energy Scheduler**
   - Mengoptimalkan distribusi energi berdasarkan kondisi sistem.
   - Menggunakan skor komposit dari:
     - State of Charge (SOC)
     - Produksi energi panel surya
     - Beban sistem
     - Temperatur lingkungan

6. **Rule-Based Scheduler**
   - Digunakan sebagai metode pembanding (*baseline*).
   - Menggunakan aturan berbasis ambang batas (*threshold*).

---

# 2. Arsitektur Sistem

```text
                NASA POWER Dataset
                         │
                         ▼
           Validasi & Preprocessing Data
                         │
                         ▼
              Photovoltaic (PV) Model
                         │
                         ▼
              Energy Demand Model
                         │
                         ▼
                 Battery Model (SOC)
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 Rule-Based Scheduler      Adaptive Energy Scheduler
          │                             │
          └──────────────┬──────────────┘
                         ▼
             Perhitungan Efisiensi Energi
                         │
                         ▼
              Analisis Statistik & Grafik
```

---

# 3. Alur Simulasi Sistem

```text
Dataset NASA POWER
        │
        ▼
Validasi Data
        │
        ▼
Preprocessing
        │
        ▼
Perhitungan Produksi Energi PV
        │
        ▼
Perhitungan Beban Sistem
        │
        ▼
Simulasi Battery Model
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

# 4. Parameter Sistem

## Panel Surya

| Parameter | Nilai |
|---|---:|
| Kapasitas Panel | 100 Wp |
| Koefisien Temperatur | −0,0045/°C |
| Efisiensi Model | Berdasarkan NASA POWER |

---

## Baterai

| Parameter | Nilai |
|---|---:|
| Jenis | Lithium-ion |
| Kapasitas | 240 Wh |
| Efisiensi Charging | 95 % |
| Efisiensi Discharging | 95 % |
| Self-discharge | 0,02 %/jam |
| SOC Minimum | 20 % |
| SOC Maksimum | 100 % |

---

## Beban Sistem

| Komponen | Daya |
|---|---:|
| Pompa Air | 18 W |
| Kipas Pendingin | 12 W |
| Lampu LED | 24 W |

Duty cycle masing-masing aktuator ditentukan berdasarkan kondisi lingkungan yang diperoleh dari dataset meteorologi.

---

## Adaptive Energy Scheduler

Scheduler menggunakan skor komposit berdasarkan empat parameter utama.

| Parameter | Bobot |
|---|---:|
| State of Charge (SOC) | 40 % |
| Energi Panel Surya | 30 % |
| Beban Sistem | 20 % |
| Temperatur | 10 % |

Mode operasi ditentukan berdasarkan nilai skor akhir.

| Mode | Kondisi |
|---|---|
| Normal Operation | Skor ≥ 80 |
| Adaptive Saving | 60 ≤ Skor < 80 |
| Priority Pump | 40 ≤ Skor < 60 |
| Emergency Mode | Skor < 40 |

---

# 5. Dataset Penelitian

| Parameter | Nilai |
|---|---|
| Sumber Data | NASA POWER |
| Periode | Januari–Desember 2024 |
| Resolusi | Per Jam |
| Jumlah Data | 8.784 |
| Koordinat | 7,55° LS; 109,67° BT |

Tahap validasi menunjukkan:

- Tidak terdapat *missing value*.
- Tidak terdapat data duplikat.
- Seluruh data berhasil diproses sebagai deret waktu (*time series*).

---

# 6. Keputusan Teknis (Final)

1. **Platform simulasi** menggunakan **Python 3.x**.

2. **Analisis data** menggunakan:

   - Pandas
   - NumPy

3. **Analisis statistik** menggunakan:

   - SciPy

4. **Visualisasi** menggunakan:

   - Matplotlib

5. **Metode pembanding** menggunakan **Rule-Based Scheduler**.

6. **Metode yang diusulkan** adalah **Adaptive Energy Scheduler** berbasis skor komposit.

7. **Dataset penelitian** menggunakan **NASA POWER Hourly Dataset** periode Januari–Desember 2024 sebanyak **8.784 data**.

8. **Metode evaluasi** menggunakan:

   - Multiple Run Experiment (5 kali)
   - Analisis statistik deskriptif
   - Paired t-test
   - Independent t-test
   - Cohen's d

9. **Output penelitian** meliputi:

   - Produksi energi panel surya
   - Konsumsi energi sistem
   - Battery State of Charge (SOC)
   - Rule-Based Efficiency
   - Adaptive Efficiency
   - Grafik Daily PV Energy
   - Grafik Battery SOC
   - Grafik Rule vs Adaptive Efficiency

10. Seluruh hasil simulasi diekspor dalam format:

- CSV
- Excel
- PNG

sehingga dapat digunakan untuk analisis lanjutan maupun penyusunan manuskrip jurnal.
