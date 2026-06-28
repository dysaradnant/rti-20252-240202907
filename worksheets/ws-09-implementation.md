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
  CPU     : AMD Ryzen 7 7435HS (16 CPUs, ~3.1 GHz)
  RAM     : 16 GB DDR5
  GPU     : NVIDIA GeForce RTX (jika tersedia) / Integrated AMD Radeon Graphics
  Storage : Minimal 100 GB SSD (untuk logging data)

Software:
  OS        : Windows 11 Home Single Language 64-bit (Build 26200)
  Runtime   : Python 3.10+
  Framework : Python (analisis & logging), MicroPython / ESP-IDF (untuk ESP32)

Dependencies:
| Library | Version | Sumber | Hash/Checksum |
|---------|---------|--------|---------------|
| pandas | 2.0+ | PyPI | Analisis log sensor & performa |
| scipy / statsmodels | Latest | PyPI | Uji statistik (t-test, Mann-Whitney)) |
| matplotlib / seaborn | Latest | PyPI | Visualisasi tren efisiensi & uptime |
| PyYAML | Latest | PyPI | Config-driven architecture |
| requests / urequests | Latest | PyPI | Komunikasi IoT (Blynk / MQTT) |

Konfigurasi:
  Config file     : config.yaml (energy thresholds, scheduler logic, setpoint lingkungan)
  Random seed     : 42 (untuk simulasi cuaca dan logging)
  Hyperparameters : Setpoint suhu 25–28°C, kelembaban 60–70%, prioritas aktuator di scheduler

Reproducibility Check:
  [✓] Dependency terdokumentasi (requirements.txt / environment.yml)
  [✓] Seed ditetapkan di semua level (Python, NumPy, framework)
  [✓] Config di version control
  [✓] README instruksi reproduksi lengkap
```

---

## Latihan 1 — Environment Specification

Dokumentasikan environment untuk eksperimen Anda (boleh environment saat ini atau yang direncanakan).

| Komponen | Spesifikasi |
|----------|------------|
| CPU | AMD Ryzen 7 7435HS (16 CPUs, ~3.1 GHz) |
| RAM | 16 GB DDR5 |
| GPU | NVIDIA GeForce RTX (jika tersedia) / Integrated AMD Radeon Graphics |
| OS | Windows 11 Home Single Language 64-bit (Build 26200) |
| Runtime |Python 3.10+ |
| Framework | Python (analisis), MicroPython / ESP-IDF (ESP32) |
| Random Seed | 42 |

**Dependencies (minimal 5):**

| Library | Version | Alasan Dibutuhkan |
|---------|---------|-------------------|
| pandas | 2.0+ | Analisis log data sensor & performa |
| scipy | Latest | Uji statistik |
| matplotlib/seaborn | Latest | Visualisasi tren |
| PyYAML | Latest | Config-driven architecture |
| requests / urequests | Latest | Komunikasi IoT |

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
> - **Thermal throttling** — CPU/GPU overheating pada run berturut-turut → clock speed turun → waktu eksekusi berubah
> - **Background process** — antivirus scan, update OS, atau cloud sync aktif saat run berlangsung
> - **Cache dari run sebelumnya** — hasil tersimpan di memori/disk sehingga run berikutnya tidak menjalankan komputasi penuh
> - **Random state tidak dikontrol di semua level** — Python seed di-set, tapi NumPy/PyTorch/TensorFlow punya seed independen

___________________________________________________

**Checklist kontrol yang sudah diterapkan:**
- [✓] Random seed di-set di semua level
- [✓] Tidak ada background process yang mengganggu
- [✓] Cache dibersihkan antar-run
- [✓] Config file yang sama untuk semua run

---

## Latihan 3 — README Eksperimen

Tulis README minimum untuk eksperimen Anda (6 komponen wajib).

```
# Judul Eksperimen: Evaluasi Adaptive Energy Scheduler pada Sistem Hidroponik IoT

## 1. Environment
> CPU: AMD Ryzen 7 7435HS (16 core, ~3.1 GHz)
> RAM: 16 GB
> OS: Windows 11 Home Single Language 64-bit (Build 26200)
> Runtime: Python 3.10+
> Python (analisis), MicroPython/ESP-IDF (ESP32)

## 2. Installation
> ```bash
# Buat environment baru
conda env create -f environment.yml
conda activate hydroponic-iot

# Atau dengan pip
pip install -r requirements.txt

## 3. Data
> Data sensor real-time (DHT22, power meter, intensitas cahaya) selama 7 hari × 8 jam/hari.
> Format: CSV + JSON log (timestamp, suhu, kelembaban, energi, uptime).
> Variasi simulasi cuaca dilakukan secara acak setiap hari.

## 4. Execution
> python run_experiment.py --config config.yaml --mode holistic --duration 8
# Untuk baseline:
python run_experiment.py --config config.yaml --mode baseline --duration 8

## 5. Configuration
> File utama: config.yaml (energy thresholds, scheduler logic, setpoint suhu/kelembaban)
> Random seed: 42 (untuk reproducibility)
> Parameter kunci: scheduler_mode: adaptive, energy_priority: [pompa, lampu, kipas]

## 6. Expected Output
> Log file: logs/2026-06-28_holistic.csv (kolom: timestamp, energi_produced, energi_consumed, uptime, deviasi_suhu, deviasi_kelembaban)
> Grafik: plots/efisiensi_harian.png, plots/uptime_trend.png
> Ringkasan: summary.txt berisi mean, std, effect size, dan statistik uji
```

---

## Refleksi

> Apakah eksperimen Anda saat ini bisa direproduksi oleh orang lain tanpa bantuan Anda? Komponen apa yang masih hilang?

**Level saat ini:** [✓] Repeatability / [ ] Reproducibility / [ ] Belum keduanya
**Komponen yang belum terdokumentasi:**
> Instruksi flash firmware ESP32 (versi MicroPython/ESP-IDF yang digunakan + langkah detail).
> Contoh file config.yaml lengkap dengan semua parameter.
> Skrip otomatis untuk membersihkan cache dan restart sistem antar sesi harian.
> Versi library yang exact di environment.yml (saat ini masih Latest di beberapa package).
