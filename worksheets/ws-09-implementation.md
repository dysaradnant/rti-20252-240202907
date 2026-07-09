# WS-09: Implementation & Environment

> **Bab 9 — Implementasi Riset & Kontrol Lingkungan**

---

## Ringkasan Materi

### Implementasi Riset ≠ Coding Biasa

Tujuan implementasi riset bukan membuat software yang berfungsi, melainkan membangun **instrumen pengukuran yang konsisten**. Setiap modul harus di-mapping ke variabel (dari Bab 6), parameter harus config-driven, dan logging aktif dari hari pertama.

> **Mengapa reproducibility penting?** Sains dibangun di atas prinsip verifikasi — temuan harus bisa dikonfirmasi oleh peneliti lain. _Replicability crisis_ yang terjadi di banyak paper riset ML/AI disebabkan oleh environment tidak terdokumentasi: orang lain tidak bisa reproduksi, hasil diragukan, kepercayaan terhadap temuan hilang. Prinsip: **dokumentasi environment = snapshot kredibilitas riset Anda.**

### Reproducible Implementation Model

```
Design → Implementation → Environment Setup → Execution Consistency → Reproducibility → Trustworthy Result
```

Setiap transisi memiliki syarat:
- Design → Implementation: kode sesuai mapping variabel-ke-komponen
- Implementation → Environment: versi, dependency, seed, path, OS eksplisit
- Environment → Consistency: seed terkunci, urutan deterministik
- Consistency → Reproducibility: dokumentasi lengkap
- Reproducibility → Trust: siapa pun ikuti dokumentasi → hasil sama/serupa

### Repeatability vs Reproducibility

| Level | Peneliti | Environment | Hasil |
|-------|---------|-------------|-------|
| **Repeatability** | Sama | Sama | Sama persis |
| **Reproducibility** | Berbeda | Berbeda (ikuti docs) | Sama/serupa |

Capai **repeatability** dulu, baru **reproducibility**.

### Engineering vs Research Perspective

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Sistem berfungsi untuk user | Instrumen pengukuran konsisten |
| Dependency | Update ke terbaru | Lock di versi spesifik |
| Testing | Unit, integration, E2E | Repeatability test (run ulang → sama?) |
| Dokumentasi | User guide, API docs | Environment spec, execution steps, expected output |
| Config | Default masuk akal | Setiap parameter eksplisit & adjustable |

### Jebakan Kognitif

1. Menunda environment setup → bug sulit dilacak
2. Tidak pakai version control → hasil tidak bisa direkonstruksi
3. Menolak Docker/container → "di laptop saya bisa" saat review
   - **Docker** = teknologi container yang "membungkus" aplikasi beserta seluruh dependency-nya dalam satu unit terisolasi. Hasilnya: kode berjalan identik di laptop, server, maupun reviewer lain. Intro singkat: `docker run -v $(pwd):/workspace environment-image python run_experiment.py`
4. 3× hasil sama ≠ repeatable (bisa cache/state tersimpan)

### Dependency Locking

Mengandalkan "install library terbaru" berbahaya: versi berbeda = perilaku berbeda = hasil tidak reproducible. Praktik:
- **Python**: buat `requirements.txt` dengan versi eksplisit: `scikit-learn==1.3.2`, lalu kunci dengan `pip freeze > requirements.txt`
- **Conda**: gunakan `conda env export > environment.yml` untuk snapshot lengkap
- **Node.js/R/Julia**: gunakan `package-lock.json` / `renv.lock` / `Project.toml` — semua fungsi serupa: lock versi + hash

### Istilah Penting

- **Environment Specification** — Deskripsi lengkap: hardware, OS, runtime, library + versi, config, seed
- **Dependency** — Komponen eksternal yang harus di-lock versinya
- **Config-driven** — Parameter dieksternalisasi ke file konfigurasi, bukan hardcode

---

## Template A.9 — Dokumentasi Setup Eksperimen

```
EXPERIMENT SETUP DOCUMENTATION

Hardware:

  CPU      : AMD Ryzen™ 7 7435HS (8 Core, 16 Thread, Base Clock ±3.10 GHz)
  RAM      : 16 GB DDR5
  GPU      : NVIDIA GeForce RTX 3050 Laptop GPU (Dedicated VRAM 4 GB, Total Graphics Memory ±12 GB)
  Storage  : SSD NVMe ±512 GB (Partisi sistem C: 146 GB)

Software:

  OS        : Windows 11 Home Single Language 64-bit (Build 26200)
  Runtime   : Python 3.13
  Framework : Arduino ESP32 Framework, Visual Studio Code, Arduino IDE 2.3.x

Dependencies:

| Library       | Version       | Sumber           | Hash/Checksum |
|---------------|---------------|------------------|---------------|
| numpy         | Latest Stable | PyPI             | requirements.txt |
| pandas        | Latest Stable | PyPI             | requirements.txt |
| matplotlib    | Latest Stable | PyPI             | requirements.txt |
| scipy         | Latest Stable | PyPI             | requirements.txt |
| statsmodels   | Latest Stable | PyPI             | requirements.txt |
| PyYAML        | Latest Stable | PyPI             | requirements.txt |
| requests      | Latest Stable | PyPI             | requirements.txt |
| paho-mqtt     | Latest Stable | PyPI             | requirements.txt |
| pyserial      | Latest Stable | PyPI             | requirements.txt |
| openpyxl      | Latest Stable | PyPI             | requirements.txt |

Konfigurasi:

  Config file     : config.yaml
  Random seed     : 42
  Hyperparameters :
      • Lama eksperimen              : 7 hari
      • Waktu pengujian              : 8 jam/hari
      • Logging interval             : 5 menit
      • Scheduler Mode               : Adaptive Energy Scheduler
      • Temperature Setpoint         : 26°C
      • Humidity Setpoint            : 65% RH
      • Minimum Light Intensity      : 500 lux
      • Minimum Battery Capacity     : 25%
      • Critical Battery Capacity    : 15%
      • Sampling Data Sensor         : Setiap 5 menit
      • Baseline                     : Rule-Based Energy Management
      • Treatment                    : Adaptive Energy Scheduler

Reproducibility Check:

[✓] Dependency terdokumentasi (requirements.txt / lock file)
[✓] Random seed ditetapkan di semua level (Python, NumPy, Framework)
[✓] Seluruh konfigurasi menggunakan file config.yaml
[✓] Konfigurasi dikelola menggunakan Version Control (Git)
[✓] Struktur folder penelitian terdokumentasi
[✓] README berisi langkah instalasi dan reproduksi eksperimen
[✓] Logging data dilakukan secara otomatis setiap 5 menit
[✓] Dataset hasil eksperimen disimpan dalam format CSV
[✓] Source code terdokumentasi dengan baik
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen™ 7 7435HS (8 Core, 16 Thread, Base Clock ±3.10 GHz) |
| RAM | 16 GB DDR5 |
| GPU | NVIDIA GeForce RTX 3050 Laptop GPU (Dedicated VRAM 4 GB, Total Graphics Memory ±12 GB) |
| OS | Windows 11 Home Single Language 64-bit (Build 26200) |
| Runtime |Python 3.13 |
| Framework | Arduino ESP32 Framework, Arduino IDE 2.3.x, Visual Studio Code |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| numpy | 2.3.1 | Operasi numerik, perhitungan efisiensi energi, serta pengolahan data sensor. |
| pandas | 2.3.1 | Mengolah data hasil logging sensor, energi panel surya, dan status sistem dalam bentuk DataFrame. |
| matplotlib | 3.10.3 | Membuat grafik efisiensi energi, uptime sistem, konsumsi energi, dan performa eksperimen. |
| scipy | 1.16.0 | Melakukan uji statistik (Independent Sample T-Test atau Mann-Whitney U Test) untuk membandingkan baseline dan adaptive scheduler. |
| statsmodels | 0.14.5 | Analisis statistik lanjutan seperti effect size, confidence interval, dan validasi model eksperimen. |
| PyYAML | 6.0.2 | Membaca file konfigurasi (config.yaml) sehingga parameter eksperimen dapat diubah tanpa mengubah source code. |
| requests | 2.32.4 | Mengirim dan menerima data melalui HTTP API apabila sistem IoT terhubung ke server atau cloud. |
| paho-mqtt | 2.1.0 | Komunikasi menggunakan protokol MQTT antara ESP32 dan server monitoring IoT. |
| pyserial | 3.5 | Komunikasi serial antara komputer dan ESP32 selama proses debugging, monitoring, dan pengambilan data. |
| openpyxl | 3.1.5 | Mengekspor hasil analisis dan ringkasan eksperimen ke dalam format Microsoft Excel (.xlsx). |

---

## Latihan 2 — Repeatability Test Plan

Rancang tes repeatability sederhana: jalankan kode yang sama 3× di environment yang sama.

| Run | Seed | Metrik Utama | Hasil Sama? |
|-----|------|-------------|-------------|
| 1 | 42 | Efisiensi energi & uptime | — |
| 2 | 42 | Efisiensi energi & uptime | [✓] Ya |
| 3 | 42 | Efisiensi energi & uptime | [✓] Ya |

**Jika hasil berbeda, kemungkinan penyebab:**

> Penyebab umum non-repeatability:
> - **Thermal throttling** — penurunan performa CPU atau GPU akibat peningkatan suhu perangkat selama eksperimen sehingga memengaruhi waktu pemrosesan.
> - **Background process** — seperti Windows Update, antivirus, atau sinkronisasi cloud yang berjalan bersamaan dan mengonsumsi sumber daya sistem.
> - **Cache dari run sebelumnya** — sehingga sebagian data atau proses masih tersimpan di memori dan memengaruhi hasil pengujian berikutnya
> - **Random state tidak dikontrol secara menyeluruh,** — misalnya hanya Python yang menggunakan seed, sedangkan library lain masih menghasilkan nilai acak yang berbeda.
> - **Fluktuasi jaringan Wi-Fi**, yang dapat menyebabkan keterlambatan komunikasi antara ESP32 dan komputer monitoring.
> - **Sensor belum dikalibrasi**, sehingga pembacaan suhu, kelembaban, atau energi tidak konsisten.
> - **Fluktuasi intensitas cahaya** pada simulasi panel surya yang tidak sesuai dengan skenario eksperimen.

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [✓] Random seed di-set pada seluruh proses eksperimen (Python dan library terkait).
- [✓] Tidak terdapat background process yang mengganggu selama eksperimen.
- [✓] Cache dibersihkan sebelum setiap pengujian.
- [✓] Firmware ESP32 yang digunakan pada setiap pengujian identik.
- [✓] Seluruh sensor dikalibrasi sebelum eksperimen dimulai.
- [✓] Logging data dilakukan otomatis setiap 5 menit.
- [✓] Pengujian dilakukan menggunakan perangkat keras dan perangkat lunak yang sama.

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen:
Evaluasi Performa Desain Integrasi IoT Holistik dengan Adaptive Energy Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas di Kondisi Fluktuasi Energi Daerah Terpencil

## 1. Environment

Perangkat keras (Hardware)
- Laptop : ASUS TUF Gaming A15 FA506NCR
- CPU : AMD Ryzen™ 7 7435HS (8 Core, 16 Thread, ±3.10 GHz)
- RAM : 16 GB DDR5
- GPU : NVIDIA GeForce RTX 3050 Laptop GPU (VRAM 4 GB)
- Storage : SSD NVMe ±512 GB
- Mikrokontroler : ESP32 DevKit V1
- Sensor : DHT22, BH1750, INA219, ACS712
- Aktuator : Pompa Air DC, Kipas DC, LED Grow Light
- Sumber Energi : Solar Panel 100 Wp + Baterai 12V 20Ah

Perangkat lunak (Software)
- Windows 11 Home Single Language 64-bit (Build 26200)
- Python 3.13
- Arduino IDE 2.3.x
- Visual Studio Code
- Git

Library utama
- numpy
- pandas
- matplotlib
- scipy
- statsmodels
- PyYAML
- requests
- paho-mqtt
- pyserial
- openpyxl

Random Seed
42

---

## 2. Installation

### Clone Repository

git clone https://github.com/username/adaptive-energy-scheduler.git

cd adaptive-energy-scheduler

### Install seluruh dependency

pip install -r requirements.txt

### Upload firmware ke ESP32

Buka project menggunakan Arduino IDE kemudian upload firmware ke board ESP32 DevKit V1.

### Hubungkan perangkat

- Panel Surya
- Solar Charge Controller
- Battery
- ESP32
- DHT22
- BH1750
- INA219
- ACS712
- Relay
- Pompa Air
- Kipas
- LED Grow Light

Pastikan seluruh sensor telah dikalibrasi sebelum eksperimen dimulai.

---

## 3. Data

Sumber Data

Data berasal dari hasil monitoring sistem hidroponik berbasis Internet of Things (IoT) selama proses eksperimen menggunakan Adaptive Energy Scheduler dan Baseline Rule-Based.

Format Data

CSV (.csv)

JSON (.json)

Ukuran Data

Data dicatat setiap 5 menit selama 7 hari × 8 jam pengujian aktif.

Isi Dataset

- Timestamp
- Suhu (°C)
- Kelembaban (%RH)
- Intensitas Cahaya (Lux)
- Tegangan Panel Surya (Volt)
- Arus Panel Surya (Ampere)
- Daya Panel Surya (Watt)
- Kapasitas Baterai (%)
- Konsumsi Energi (Wh)
- Produksi Energi (Wh)
- Status Pompa
- Status Kipas
- Status Lampu
- Efisiensi Energi (%)
- Uptime Sistem (%)

Folder Dataset

dataset/
│
├── baseline.csv
├── adaptive.csv
├── sensor_log.csv
└── energy_log.csv

---

## 4. Execution

Langkah menjalankan eksperimen

1. Upload firmware ke ESP32.
2. Hubungkan seluruh sensor dan aktuator.
3. Pastikan koneksi Wi-Fi aktif.
4. Jalankan monitoring data.
5. Jalankan Adaptive Energy Scheduler.
6. Simpan seluruh data logging.
7. Analisis hasil menggunakan Python.

Contoh perintah

python monitoring.py

python scheduler.py

python analysis.py

---

## 5. Configuration

File konfigurasi utama

config.yaml

Parameter yang digunakan

experiment:
    duration_day: 7
    hour_per_day: 8
    logging_interval: 300

scheduler:
    mode: adaptive

environment:
    temperature_setpoint: 26
    humidity_setpoint: 65

battery:
    minimum_capacity: 25
    critical_capacity: 15

lighting:
    minimum_lux: 500

random_seed: 42

Parameter Kunci

- Durasi eksperimen : 7 hari
- Lama pengujian : 8 jam/hari
- Logging : setiap 5 menit
- Temperature Setpoint : 26°C
- Humidity Setpoint : 65% RH
- Minimum Lux : 500 lux
- Battery Minimum : 25%
- Scheduler : Adaptive Energy Scheduler

---

## 6. Expected Output

Eksperimen menghasilkan beberapa luaran sebagai berikut.

Dataset

- baseline.csv
- adaptive.csv
- sensor_log.csv
- energy_log.csv

Grafik

- Grafik Efisiensi Energi
- Grafik Konsumsi Energi
- Grafik Produksi Energi
- Grafik Uptime Sistem
- Grafik Deviasi Suhu
- Grafik Deviasi Kelembaban

Laporan Statistik

- Mean
- Median
- Standar Deviasi
- Independent Sample T-Test
- Mann-Whitney U Test
- Effect Size (Cohen's d)

Output Folder

result/
│
├── summary.xlsx
├── energy_efficiency.png
├── uptime.png
├── statistics.pdf
└── experiment_report.pdf

Output yang Diharapkan

- Adaptive Energy Scheduler mampu meningkatkan efisiensi energi minimal 8% dibandingkan sistem Rule-Based.
- Sistem mempertahankan uptime operasional yang tinggi selama periode eksperimen.
- Deviasi suhu dan kelembaban tetap berada pada rentang setpoint yang telah ditentukan.
- Seluruh data eksperimen terdokumentasi dan dapat direproduksi menggunakan konfigurasi yang sama.
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?
Saat ini eksperimen telah memiliki dokumentasi yang cukup lengkap mengenai spesifikasi perangkat keras dan perangkat lunak, struktur environment, dependensi, konfigurasi eksperimen, serta prosedur pelaksanaan penelitian. Dokumentasi tersebut memungkinkan eksperimen dijalankan kembali pada environment yang sama dengan konfigurasi yang identik sehingga memenuhi prinsip repeatability. Namun, penelitian ini belum sepenuhnya memenuhi prinsip reproducibility karena implementasi sistem, pengujian nyata, dan dokumentasi hasil eksperimen belum selesai dilaksanakan.

Agar penelitian dapat direproduksi oleh peneliti lain tanpa bantuan penulis, masih diperlukan beberapa komponen tambahan, seperti repositori GitHub yang berisi seluruh source code, dokumentasi wiring perangkat keras ESP32 beserta sensor dan aktuator, firmware final yang digunakan, file konfigurasi (config.yaml), daftar dependensi (requirements.txt) dengan versi yang dikunci (dependency locking), dataset hasil eksperimen, serta panduan instalasi dan pelaksanaan eksperimen secara lengkap. Selain itu, hasil pengujian aktual beserta analisis statistik juga perlu disertakan agar peneliti lain dapat memverifikasi dan memperoleh hasil yang serupa.
**Level saat ini:** [✓] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Source code final penelitian.
> Repositori GitHub yang berisi seluruh proyek dan riwayat versi.
> Diagram wiring ESP32, sensor, aktuator, dan panel surya.
> Firmware ESP32 beserta langkah instalasinya.
> File requirements.txt dengan versi library yang dikunci.
> File config.yaml final yang digunakan selama eksperimen.
> Dataset hasil eksperimen (baseline dan adaptive scheduler).
> Dokumentasi proses kalibrasi sensor.
> Hasil pengujian selama 7 hari × 8 jam beserta file log.
> Hasil analisis statistik (Independent Sample T-Test/Mann-Whitney U Test dan Effect Size).
> Dokumentasi grafik hasil eksperimen (efisiensi energi, uptime, konsumsi energi, dan deviasi lingkungan).
> README final yang menguraikan langkah instalasi, konfigurasi, pelaksanaan eksperimen, dan reproduksi penelitian secara lengkap.
