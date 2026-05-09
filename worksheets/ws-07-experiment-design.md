# WS-07: Experimental Design & Validity

> **Bab 7 — Experimental Design & Validity**

---

## Ringkasan Materi

### Correlation ≠ Causality

Kausalitas membutuhkan 3 syarat:
1. **Covariance** — X dan Y bergerak bersama
2. **Temporal precedence** — X berubah sebelum Y
3. **Elimination of alternatives** — Tidak ada faktor lain yang menjelaskan Y

Controlled experiment adalah satu-satunya metode yang bisa membuktikan kausalitas.

### Empat Jenis Validitas

| Jenis | Pertanyaan | Ancaman Umum |
|-------|-----------|-------------|
| **Internal** | Apakah hubungan IV→DV nyata? | Confounding variable, selection bias |
| **External** | Apakah bisa digeneralisasi? | Dataset terlalu spesifik |
| **Construct** | Apakah mengukur konsep yang benar? | Metrik tidak sesuai |
| **Conclusion** | Apakah kesimpulan statistik valid? | Sample size kecil, uji salah |

Internal dan external validity sering berkonflik: semakin terkontrol (internal kuat) → semakin artificial (external lemah).

### Tiga Tipe Eksperimen dalam Riset TI

| Tipe | Deskripsi | Kapan Digunakan |
|------|----------|----------------|
| **Comparison Study** | Metode A vs B pada kondisi identik | Membandingkan pendekatan berbeda |
| **Ablation Study** | Full system → lepas komponen satu per satu | Mengukur kontribusi tiap komponen |
| **Parameter Study** | Variasikan satu parameter, amati dampak | Uji sensitifitas/robustness |

### Fairness dalam Perbandingan

Perbandingan yang adil = **kondisi identik** untuk semua metode: dataset sama, preprocessing sama, tuning effort sebanding, environment sama, metrik sama.

Contoh tidak adil: Transformer (30 fitur tambahan + Bayesian optimization) vs RF (default params) → hasilnya misleading.

### Threats to Validity = Diidentifikasi Sebelum Eksperimen

Ancaman validitas harus diidentifikasi **sebelum** eksperimen dan mitigasinya dirancang sebagai bagian dari desain — bukan ditulis sebagai boilerplate setelah selesai.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan testing | Memastikan sistem memenuhi requirement | Membuktikan hubungan kausal antar variabel |
| Baseline | Versi sebelumnya (last release) | Metode tervalidasi dari literatur |
| Kegagalan | Bug → fix → release | H₀ tidak ditolak → tetap kontribusi ilmiah |
| Sukses | 100% test pass | Evidence valid — mendukung atau menolak hipotesis |

### Istilah Penting

- **Causality** — Hubungan sebab-akibat (covariance + temporal + elimination)
- **Controlled Experiment** — Ubah satu variabel, kontrol sisanya, amati efek
- **Fairness** — Semua metode diuji pada kondisi yang benar-benar identik
- **Threats to Validity** — Faktor yang bisa melemahkan kesimpulan jika tidak dimitigasi
- **Conclusion Validity** — Validitas statistik: power, sample size, uji yang tepat

---

## Template A.7 — Desain Eksperimen Lengkap

```
EXPERIMENT DESIGN

Research Question : Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem (waktu operasi 24 jam tanpa gangguan) dibandingkan dengan baseline sistem IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil dengan variasi intensitas cahaya matahari?
Hypothesis        : H₁ — Desain integrasi IoT holistik menghasilkan efisiensi energi lebih tinggi (≥8%) dan kestabilan operasional yang lebih baik dibandingkan baseline.
Tipe Eksperimen   : [v] Comparison  [ ] Ablation  [ ] Parameter

Kondisi Eksperimen:
| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control |   Sistem IoT solar sederhana (seperti common practice di literatur)        |    Baseline (otomasi dasar tanpa holistic scheduler)      |      Setpoint suhu & kelembaban sama, durasi pengujian sama, sensor sama       |
| Treatment |      Sistem IoT holistik dengan adaptive energy management   |     Holistic Design (dengan scheduler adaptif + battery management)     |     Sama dengan baseline        |

Fairness Checklist:
  [v] Dataset identik untuk semua kondisi
  [v] Preprocessing setara
  [v] Tuning effort setara
  [v] Environment identik
  [v] Metrik evaluasi sama

Threat Analysis:
| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal    |  Fluktuasi cuaca yang tidak terkendali memengaruhi kedua sistem secara berbeda               |      Pengujian simultan atau bergantian di waktu yang sama, randomisasi urutan pengujian, serta analisis sensitivitas cuaca    |
| External    |     Hasil prototipe skala kecil sulit digeneralisasi ke instalasi komersial            |     Melakukan pengujian di minimal 2 skala berbeda dan mendokumentasikan batasan skalabilitas     |
| Construct   |        Efisiensi energi diukur, tetapi tidak mencerminkan manfaat agronomis         |   Menggunakan secondary metric: pertumbuhan tanaman (tinggi & jumlah daun)       |
| Conclusion  |        Sample size pengujian terlalu kecil sehingga power statistik rendah         |    Melakukan pengujian minimal 8–12 minggu dengan multiple runs dan perhitungan power analysis      |

Statistical Plan:
  Uji statistik   : Independent t-test atau Mann-Whitney U test (tergantung normalitas data)
  Justifikasi      : Cocok untuk membandingkan dua kelompok independen (baseline vs treatment) pada metrik ratio
  Alpha            : 0.05
  Effect size min  : Cohen’s d ≥ 0.5 (medium effect) atau peningkatan minimal 8% pada efisiensi energi
```

---

## Latihan 1 — Desain Eksperimen

Susun desain eksperimen berdasarkan RQ, variabel, dan sistem dari WS-04 sampai WS-06.

**RQ:** Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem dibandingkan baseline?
**Tipe eksperimen:** [v] Comparison / [ ] Ablation / [ ] Parameter

| Kondisi | Deskripsi | IV Value | CV Settings |
|---------|-----------|----------|-------------|
| Control | Baseline sistem IoT solar sederhana | Baseline Design | Sensor, setpoint, lokasi, durasi sama |
| Treatment | Sistem dengan integrasi holistik & adaptive scheduler | Holistic IoT-Solar Design | Sama dengan control |

---

## Latihan 2 — Fairness Checklist

Evaluasi apakah desain eksperimen di Latihan 1 sudah fair.

| Kriteria | Status | Detail |
|----------|--------|--------|
| Dataset identik | ✅ | Data sensor diambil dari lingkungan dan periode waktu yang sama |
| Preprocessing setara | ✅ | Log data diproses dengan script yang sama |
| Tuning effort setara | ✅ | Kedua sistem dioptimasi dengan effort yang sebanding |
| Environment identik | ✅ | Pengujian dilakukan secara paralel atau bergantian di lokasi yang sama |
| Metrik evaluasi sama | ✅ | Semua metrik dihitung dengan formula dan tool yang identik |

**Ada yang tidak fair?** [ ] Ya / [v] Tidak
> Jika ya, bagaimana cara memperbaikinya? ________________

---

## Latihan 3 — Threat Analysis

Identifikasi ancaman validitas untuk desain eksperimen ini.

| Threat Type | Ancaman Spesifik | Mitigasi |
|-------------|-----------------|----------|
| Internal | Fluktuasi cuaca yang tidak terkendali memengaruhi kedua sistem secara berbeda | Pengujian simultan atau bergantian di waktu yang sama, randomisasi urutan pengujian, serta analisis sensitivitas cuaca |
| External | Hasil prototipe skala kecil sulit digeneralisasi ke instalasi komersial | Melakukan pengujian di minimal 2 skala berbeda dan mendokumentasikan batasan skalabilitas |
| Construct | Efisiensi energi diukur, tetapi tidak mencerminkan manfaat agronomis | Menggunakan secondary metric: pertumbuhan tanaman (tinggi & jumlah daun) |
| Conclusion | Sample size pengujian terlalu kecil sehingga power statistik rendah | Melakukan pengujian minimal 8–12 minggu dengan multiple runs dan perhitungan power analysis |
 
**Ancaman mana yang paling sulit dimitigasi?** External Validity (generalizability)
**Mengapa?**
> Karena riset ini menggunakan prototipe skala kecil di lingkungan simulasi. Sulit sepenuhnya merepresentasikan kondisi lapangan yang sangat beragam (ukuran lahan, jenis tanaman, cuaca ekstrem jangka panjang). Mitigasi terbaik yang bisa dilakukan adalah transparansi batasan dan merekomendasikan replikasi di skala yang lebih besar.

---

## Refleksi

> Sebuah paper melaporkan "metode kami mengalahkan semua baseline." Apa 3 pertanyaan pertama yang harus diajukan untuk mengevaluasi klaim ini?

**Jawaban:**
1. Apa baseline yang digunakan dan apakah kondisi eksperimennya benar-benar identik dengan metode yang diklaim lebih baik?
2. Apakah ada confounding variable (misalnya tuning hyperparameter, durasi pelatihan, atau hardware) yang tidak disebutkan?
3. Berapa lama pengujian dilakukan dan apakah hasilnya konsisten di berbagai kondisi (atau hanya di kondisi ideal)?
