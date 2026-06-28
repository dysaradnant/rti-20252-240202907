# WS-10: Experiment Execution & Data Collection

> **Bab 10 — Eksekusi Eksperimen & Pengumpulan Data**

---

## Ringkasan Materi

### Experiment Execution Pipeline

```
Design → Execution Plan → Controlled Execution → Data Collection → Data Logging → Dataset for Analysis
```

### Multiple Run = Non-Negotiable

Single run **tidak pernah cukup** untuk klaim ilmiah. Minimum 5-10 run per skenario dengan seed berbeda. Multiple run menghasilkan:
- Mean, std, confidence interval
- Distribusi hasil → uji statistik
- Variabilitas → error bar di grafik

### Execution Plan

Setiap eksperimen harus memiliki plan sebelum eksekusi:
- Daftar skenario
- Jumlah run per skenario
- Random seed per run (pre-determined!)
- Urutan eksekusi (randomisasi/counterbalancing)
- Pre-execution checklist

### Data Logging Komprehensif

Setiap run menghasilkan log terstruktur:
1. **Identitas** — Run ID, timestamp, skenario
2. **Konfigurasi** — Semua parameter, seed, code version
3. **Hasil** — Semua metrik, output detail
4. **Metadata** — Waktu eksekusi, resource usage, warning/error

Format: CSV/JSON/database — **bukan stdout yang di-copy-paste**.

### Engineering vs Research Execution

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Run | Sekali (deploy) | Multiple (min 5-10, seed berbeda) |
| Logging | Error log, access log | Semua parameter, metrik, metadata |
| Anomali | Bug → fix → redeploy | Investigasi → dokumentasi → analisis |
| Urutan | Tidak penting | Bisa bias — perlu randomisasi |

### Anomali = Dokumentasi, Bukan Hapus

Run gagal/anomali tidak boleh dihapus tanpa dokumentasi. Bisa jadi:
- **Bug** → fix & re-run (dokumentasikan!)
- **Batas kemampuan metode** → DNF = temuan
- **Data yang bias** jika hanya simpan run "berhasil"

### Jebakan Kognitif

1. "Satu angka cukup" → tanpa distribusi, tidak bisa diuji
2. "Seed tidak penting" → bahkan algoritma deterministik bisa dipengaruhi library stokastik
3. "Run gagal langsung hapus" → kehilangan temuan potensial
4. "Semua run harus hari ini" → thermal throttling, fatigue

---

## Template A.10 — Execution Plan & Data Log

```
EXECUTION PLAN

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1     | Baseline (Rule-based) | 42  | mode=rule_based | Planned | - | run_01_baseline.csv |
| 2     | Baseline (Rule-based) | 123 | mode=rule_based | Planned | - | run_02_baseline.csv |
| 3     | Baseline (Rule-based) | 456 | mode=rule_based | Planned | - | run_03_baseline.csv |
| 4     | Baseline (Rule-based) | 789 | mode=rule_based | Planned | - | run_04_baseline.csv |
| 5     | Baseline (Rule-based) | 101 | mode=rule_based | Planned | - | run_05_baseline.csv |
| 6     | Treatment (Holistic)  | 42  | mode=adaptive_scheduler | Planned | - | run_06_treatment.csv |
| 7     | Treatment (Holistic)  | 123 | mode=adaptive_scheduler | Planned | - | run_07_treatment.csv |
| 8     | Treatment (Holistic)  | 456 | mode=adaptive_scheduler | Planned | - | run_08_treatment.csv |
| 9     | Treatment (Holistic)  | 789 | mode=adaptive_scheduler | Planned | - | run_09_treatment.csv |
| 10    | Treatment (Holistic)  | 101 | mode=adaptive_scheduler | Planned | - | run_10_treatment.csv |


Jumlah runs per skenario : 5
Total runs               : 10

DATA LOG (per run):
  Run ID    : run_01_baseline
  Timestamp : 2026-06-28 14:00:00
  Skenario  : Baseline / Treatment
  Input     : Sensor readings (suhu, kelembaban, intensitas cahaya, energi surya)
  Output    : Efisiensi energi (%), Uptime (jam & %), Deviasi suhu/kelembaban, Pertumbuhan tanaman
  Anomali   : Sensor disconnect / baterai rendah / simulasi cuaca ekstrem (jika ada)
  Catatan   : Catatan khusus (thermal throttling, restart, perubahan manual, dll)
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter Kunci | Status |
|-------|----------|------|----------------|--------|
| 1 | Baseline (Rule-based)* | 42 | mode=rule_based | Planned |
| 2 | Baseline (Rule-based)* | 123 | mode=rule_based | Planned |
| 3 | Baseline (Rule-based)* | 456 | mode=rule_based | Planned |
| 4 | Baseline (Rule-based)* | 789 | mode=rule_based | Planned |
| 5 | Baseline (Rule-based)* | 101 | mode=rule_based | Planned |
| 6 | Treatment (Holistic)* | 42 | mode=adaptive_scheduler | Planned |
| 7 | Treatment (Holistic)* | 123 | mode=adaptive_scheduler | Planned |
| 8 | Treatment (Holistic)* | 456 | mode=adaptive_scheduler | Planned |
| 9 | Treatment (Holistic)* | 789 | mode=adaptive_scheduler | Planned |
| 10 | Treatment (Holistic)* | 101 | mode=adaptive_scheduler | Planned |


**Total skenario:** 2
**Run per skenario:** 5
**Total run keseluruhan:** 10

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run_01_treatment |
| Timestamp | 2026-06-28 14:30:00 |
| Skenario | Treatment (Holistic) |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Seed | 42 |
| Code version | commit abc1234 (Git) |
| Mode Scheduler | adaptive_scheduler |
| Energy Threshold | 30% baterai minimum |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Efisiensi Penggunaan Energi | float | 0 – 100 (%) |
| Kestabilan Operasional (Uptime) | float | 0 – 8 (jam) / 0–100 (%) |
| Deviasi Suhu rata-rata | float | 0 – 5 (°C) |
| Deviasi Kelembaban rata-rata | float | 0 – 10 (%RH) |
| Tinggi Tanaman rata-rata | float | 0 – 30 (cm) |
| Jumlah Daun rata-rata | integer | 0 – 50 (helai) |

**Format output:** [✓] CSV / [✓] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | ESP32 disconnect, sensor error, program crash | 1. Dokumentasikan error lengkap di log.
2. Restart sistem & sensor.
3. Re-run dengan catatan "retry after crash".
4. Jika berulang, analisis penyebab (kabel / power) |
| Hasil ekstrem (outlier) | Efisiensi energi >110% atau negatif | 1. Periksa sensor (kalibrasi ulang).
2. Dokumentasikan sebagai outlier.
3. Analisis sensitivitas (apakah karena cuaca simulasi?).
4. Tetap simpan, jangan hapus. |
| Waktu eksekusi anomali | Run jauh lebih lambat dari biasanya | 1. Cek thermal throttling Ryzen 7 (gunakan HWMonitor).
2. Tutup aplikasi latar belakang.
3. Catat di log: "thermal throttling detected". |
| Inkonsistensi dengan run lain | Satu run efisiensi jauh lebih rendah | 1. Bandingkan log cuaca & status baterai.
2. Dokumentasikan sebagai variabilitas alami.
3. Sertakan dalam analisis sensitivitas. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
> Ya, beberapa kali di tugas kuliah atau proyek kecil saya pernah melaporkan hasil dari single run saja (misalnya testing satu kali prototipe IoT atau satu kali training model). Hasilnya terlihat bagus di layar, tapi sebenarnya sangat rentan.
**Yang akan dilakukan berbeda:**
> Mulai sekarang saya akan selalu menjalankan minimal 5 run per skenario dengan seed berbeda seperti yang direncanakan di Execution Plan. Setiap run akan dicatat lengkap dengan timestamp, konfigurasi, dan anomali.
