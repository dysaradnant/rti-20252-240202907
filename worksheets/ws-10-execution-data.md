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
| 1 | Baseline Rule-Based | 42 | Config Default | Planned | Hari-1 | baseline_run01.csv |
| 2 | Baseline Rule-Based | 123 | Config Default | Planned | Hari-2 | baseline_run02.csv |
| 3 | Baseline Rule-Based | 256 | Config Default | Planned | Hari-3 | baseline_run03.csv |
| 4 | Baseline Rule-Based | 512 | Config Default | Planned | Hari-4 | baseline_run04.csv |
| 5 | Baseline Rule-Based | 1024 | Config Default | Planned | Hari-5 | baseline_run05.csv |
| 6 | Adaptive Scheduler | 42 | Adaptive Mode | Planned | Hari-1 | adaptive_run01.csv |
| 7 | Adaptive Scheduler | 123 | Adaptive Mode | Planned | Hari-2 | adaptive_run02.csv |
| 8 | Adaptive Scheduler | 256 | Adaptive Mode | Planned | Hari-3 | adaptive_run03.csv |
| 9 | Adaptive Scheduler | 512 | Adaptive Mode | Planned | Hari-4 | adaptive_run04.csv |
|10 | Adaptive Scheduler |1024 | Adaptive Mode | Planned | Hari-5 | adaptive_run05.csv |

Jumlah Run per Skenario : 5 Run
Jumlah Skenario         : 2
Total Run               : 10 Run

DATA LOG (per run):
  Run ID    : run_01
  Timestamp : 2026-07-10 08:00:00
  Skenario  : Adaptive Energy Scheduler
  Seed      : 42
  Input     : Temperatur Awal, Kelembaban Awal, Intensitas Cahaya, Tegangan Panel Surya, Arus Panel, Kapasitas Baterai, Status Pompa, Status Lampu, Status Kipas
  Output    : Temperatur Akhir, Kelembaban Akhir, Efisiensi Energi, Total Produksi Energi, Total Konsumsi Energi, Persentase Uptime, Deviasi Temperatur, Deviasi Kelembaban, Status Scheduler, Response Time Scheduler
  Metadata  : Lama Eksekusi, CPU Usage, RAM Usage, GPU Usage, Wi-Fi RSSI, Jumlah Error, Warning, Exception, Status Run
  Anomali   : Tidak Ada / Ada
  Catatan   : Catatan khusus (thermal throttling, restart, perubahan manual, dll)
```

---

## Latihan 1 — Execution Plan

Susun execution plan untuk eksperimen Anda. Tentukan skenario, jumlah run, dan seed sebelum eksekusi.

| Run # | Skenario | Seed | Parameter | Status | Waktu | Output File |
|-------|----------|------|-----------|--------|-------|-------------|
| 1 | Baseline Rule-Based | 42 | Config Default | Planned | Hari-1 | baseline_run01.csv |
| 2 | Baseline Rule-Based | 123 | Config Default | Planned | Hari-2 | baseline_run02.csv |
| 3 | Baseline Rule-Based | 256 | Config Default | Planned | Hari-3 | baseline_run03.csv |
| 4 | Baseline Rule-Based | 512 | Config Default | Planned | Hari-4 | baseline_run04.csv |
| 5 | Baseline Rule-Based | 1024 | Config Default | Planned | Hari-5 | baseline_run05.csv |
| 6 | Adaptive Scheduler | 42 | Adaptive Mode | Planned | Hari-1 | adaptive_run01.csv |
| 7 | Adaptive Scheduler | 123 | Adaptive Mode | Planned | Hari-2 | adaptive_run02.csv |
| 8 | Adaptive Scheduler | 256 | Adaptive Mode | Planned | Hari-3 | adaptive_run03.csv |
| 9 | Adaptive Scheduler | 512 | Adaptive Mode | Planned | Hari-4 | adaptive_run04.csv |
|10 | Adaptive Scheduler |1024 | Adaptive Mode | Planned | Hari-5 | adaptive_run05.csv |


**Total skenario:** 2
**Run per skenario:** 5
**Total run keseluruhan:** 10

---

## Latihan 2 — Data Log Terstruktur

Desain format data log untuk eksperimen Anda. Tentukan field apa saja yang akan dicatat.

**Identitas:**
| Field | Contoh |
|-------|--------|
| Run ID | run_01 |
| Experiment ID | EXP-2026-001 |
| Timestamp | 2026-07-10 08:00:00 |
| Tanggal | 10 Juli 2026 |
| Hari Pengujian | Hari-1 |
| Skenario| Adaptive Scheduler |
| Operator | Dysar |

**Konfigurasi:**
| Field | Contoh |
|-------|--------|
| Random Seed | 42 |
| Firmware Version | v1.0 |
| Code Version | Git Commit a1b2c3 |
| Config File | config.yaml |
| Scheduler Mode | Adaptive |
| Temperature Setpoint | 26°C |
| Humidity Setpoint | 65% RH |
| Minimum Lux | 500 lux |
| Minimum Battery | 500 lux |
| Critical Battery |15% |
| Logging Interval | 300 detik |
| Sampling Rate | 5 menit |

**Hasil:**
| Metrik | Tipe Data | Range Valid |
|--------|----------|-------------|
| Suhu | float | 15–45°C |
| Kelembaban | float |20–100% RH |
| Intensitas Cahaya | 0–100000 lux |
| Tegangan Panel | float | 0–24 Volt |
| Arus Panel | float | 0–10 Ampere |
| Daya Panel | float | 0–200 Watt |
| Kapasitas Baterai | float | 0–100% |
| Konsumsi Energi | float | ≥0 Wh |
| Produksi Energi | float | ≥0 Wh |
| Efisiensi Energi | float | 0–100% |
| Deviasi Suhu | float | ±10°C |
| Deviasi Kelembaban | float | ±20% RH |
| Response Time Scheduler | float | 0–10 detik |
| Uptime Sistem | float | 0–100% |

**Format output:** [✓] CSV / [✓] JSON / [ ] Database / [ ] Lainnya: ____

---

## Latihan 3 — Anomaly Protocol

Rencanakan bagaimana menangani anomali. Untuk setiap jenis, tentukan langkah yang diambil.

| Jenis Anomali | Contoh | Tindakan |
|---------------|--------|----------|
| Run gagal (crash) | ESP32 restart, aplikasi Python berhenti, koneksi MQTT terputus | Dokumentasikan penyebab, periksa log sistem, perbaiki penyebab, kemudian lakukan re-run dengan konfigurasi yang sama. |
| Hasil ekstrem (outlier) | Efisiensi energi mencapai 100% atau 0% secara tidak wajar | Verifikasi data sensor, cek konfigurasi, bandingkan dengan run lain. Jika terbukti kesalahan sistem, lakukan re-run; jika valid, tetap dicatat sebagai temuan. |
| Waktu eksekusi anomali | Waktu proses jauh lebih lama dibandingkan run lainnya | Periksa penggunaan CPU, RAM, jaringan, dan proses latar belakang. Catat penyebab dan tentukan apakah perlu mengulang eksperimen. |
| Inkonsistensi dengan run lain | Nilai efisiensi berbeda jauh padahal konfigurasi sama | Bandingkan log eksperimen, periksa random seed, firmware, konfigurasi, dan kondisi lingkungan. Jika ditemukan kesalahan teknis, lakukan re-run. |
| Sensor tidak merespons | DHT22 atau BH1750 gagal mengirim data | Kalibrasi ulang atau ganti sensor, dokumentasikan waktu kegagalan, kemudian ulangi run jika data utama tidak lengkap. |
| Gangguan komunikasi | Wi-Fi terputus, MQTT timeout | Dokumentasikan durasi gangguan, lakukan koneksi ulang, dan lanjutkan eksperimen jika data masih dapat dipulihkan. |
| Kapasitas baterai di bawah batas minimum | Baterai turun di bawah 15% sebelum eksperimen selesai | Catat kondisi sebagai bagian dari hasil eksperimen, evaluasi keputusan Adaptive Energy Scheduler, dan ulangi run hanya jika penyebabnya bukan bagian dari skenario penelitian. |
| Kesalahan konfigurasi | Nilai pada config.yaml berbeda dengan execution plan | Hentikan eksperimen, perbaiki konfigurasi, dokumentasikan perubahan, lalu jalankan ulang seluruh run terkait. |

**Prinsip:** Detect → Investigate → Document → Decide

---

## Refleksi

> Pernahkah Anda melaporkan hasil riset/tugas dari single run? Apa risikonya? Bagaimana multiple run mengubah kepercayaan terhadap hasil?

**Pengalaman sebelumnya:**
Pada beberapa tugas praktikum maupun proyek sebelumnya, hasil eksperimen umumnya diperoleh hanya dari satu kali pengujian (single run). Pendekatan tersebut cukup untuk menunjukkan bahwa sistem dapat berjalan sesuai fungsi yang diharapkan, namun belum cukup untuk membuktikan bahwa hasil yang diperoleh benar-benar konsisten dan dapat dipercaya. Dalam banyak kasus, hasil dari satu kali pengujian dapat dipengaruhi oleh kondisi lingkungan, performa perangkat keras, proses yang berjalan di latar belakang, maupun faktor acak (randomness) yang tidak dikendalikan.
**Yang akan dilakukan berbeda:**
Pada penelitian ini, pendekatan eksperimen dirancang berbeda dengan menerapkan prinsip multiple run sebagaimana direkomendasikan dalam WS-10. Setiap skenario eksperimen, yaitu Baseline (Rule-Based Energy Management) dan Adaptive Energy Scheduler, akan dijalankan sebanyak lima kali menggunakan random seed yang telah ditentukan sebelum eksperimen dimulai. Seluruh run dilakukan menggunakan konfigurasi perangkat keras, perangkat lunak, dan parameter eksperimen yang sama sehingga perbedaan hasil benar-benar mencerminkan perbedaan metode yang diuji.
