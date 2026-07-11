# WS-13: Data Preprocessing

> **Bab 13 — Preprocessing & Persiapan Data untuk Analisis**

---

## Ringkasan Materi

### Data Refinement Pipeline

```
Raw Data → Cleaning → Transformation → Normalization → Processed Data → Analysis Ready
```

Setiap tahap memiliki tujuan berbeda. **Preprocessing bukan langkah teknis biasa** — setiap keputusan preprocessing adalah keputusan riset yang bisa mengubah kesimpulan.

### Empat Prinsip Preprocessing

| Prinsip | Deskripsi |
|---------|----------|
| **Consistency** | Metode sama untuk data yang sama |
| **Transparency** | Setiap langkah terdokumentasi |
| **Reproducibility** | Orang lain bisa mengulang dengan hasil sama |
| **Minimal Distortion** | Ubah sesedikit mungkin; jika normalisasi tidak perlu, jangan lakukan |

### Cleaning Triad

| Masalah | Strategi | Risiko |
|---------|---------|--------|
| **Missing values** | | |
| — Listwise deletion | Missing < 5%, random | Data loss |
| — Mean/median imputation | Sedikit missing, dist. normal | Mengurangi variabilitas |
| — Model-based imputation | Banyak missing, pola sistematis | Introduces dependency |
| — Flag & separate | Missing karena alasan substantif | Kompleksitas analisis |
| **Duplikat** | Identifikasi → verifikasi → hapus | False positive (data mirip ≠ duplikat) |
| **Error format** | Standardisasi tipe, encoding | Kehilangan informasi saat konversi |

### Normalisasi — Kapan & Metode Mana

| Metode | Formula | Output | Sensitif Outlier? |
|--------|---------|--------|-------------------|
| Min-max | (x-min)/(max-min) | [0, 1] | Ya |
| Z-score | (x-mean)/std | Unbounded | Lebih robust |
| Robust scaling | (x-median)/IQR | Unbounded | Paling robust |

**Kunci:** Parameter normalisasi harus dihitung dari **training set saja** — bukan seluruh data. Pelanggaran = **data leakage**.

### Data Leakage Prevention

Data leakage terjadi ketika informasi dari test set "bocor" ke preprocessing:
- Normalisasi parameter dari seluruh dataset ← **SALAH**
- Cross-validation dilakukan sebelum split ← **SALAH**
- Feature selection menggunakan label test set ← **SALAH**

### Jebakan Kognitif

1. "Preprocessing cuma teknis — tidak perlu detail" → bisa ubah kesimpulan
2. "Lebih banyak preprocessing = lebih bersih = lebih baik" → over-processing distorsi data
3. "Normalisasi selalu diperlukan" → belum tentu, tergantung metode analisis
4. "Imputation sama untuk semua situasi" → strategi harus sesuai konteks

---

## Template A.13 — Preprocessing Documentation Log

```
PREPROCESSING LOG

Dataset           : NASA POWER Hourly Dataset 2024
Jumlah data awal  : 8784 records

Cleaning:
| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing Value | 0 | Tidak ada tindakan | Dataset lengkap, tidak ditemukan nilai kosong |
| Duplikat | 0 | Tidak ada tindakan | Tidak ditemukan data duplikat |
| Error Format | 0 | Validasi format kolom | Seluruh kolom sesuai format numerik yang dibutuhkan |

Transformation:
| Transformasi | Variabel | Detail | Alasan |
|-------------|----------|--------|--------|
| Rename Kolom | ALLSKY_SFC_SW_DWN | Menjadi Solar | Mempermudah penulisan kode dan analisis |
| Rename Kolom | T2M | Menjadi Temperature | Nama lebih deskriptif |
| Rename Kolom | RH2M | Menjadi Humidity | Memudahkan interpretasi |
| Rename Kolom | WS10M | Menjadi Wind | Konsisten dengan variabel lain |
| Datetime Parsing | YEAR, MO, DY, HR | Digabung menjadi kolom Datetime | Memudahkan analisis berdasarkan waktu |
| Sorting Data | Datetime | Data diurutkan berdasarkan waktu | Menjamin urutan kronologis eksperimen |

Feature Engineering
| Variabel Baru | Rumus | Tujuan |
|-------------|----------|--------|
| TempCorrection | 1 − β(T−25) | Koreksi performa panel terhadap suhu |
| PV_Power_W |  Panel × Solar × TempCorrection | Menghitung daya panel surya |
| PV_Energy_Wh | PV_Power_W × 1 jam | Menghitung energi panel surya |
| Pump_Wh | Duty Cycle × Pump Power | Estimasi konsumsi energi pompa |
| Fan_Wh | Duty Cycle × Pump Power | Estimasi konsumsi energi kipas |
| LED_Wh | Duty Cycle × Pump Power | Estimasi konsumsi energi lampu |
| Load_Wh | Duty Cycle × Pump Power | Total kebutuhan energi |
| Charge_Wh | PV − Load | Energi yang mengisi baterai |
| Discharge_Wh | Load − PV | Energi yang digunakan baterai |
| SOC | Battery State of Charge | Persentase kapasitas baterai |

Normalization:
  Metode    : Tidak dilakukan normalisasi.
  Alasan    : Pada penelitian ini seluruh variabel diproses menggunakan rumus fisik dan simulasi energi sehingga mempertahankan satuan asli (Wh, Watt, °C, %, W/m²) lebih penting dibandingkan melakukan normalisasi. Selain itu metode yang digunakan bukan algoritma machine learning berbasis jarak (misalnya KNN atau SVM) sehingga normalisasi tidak menjadi kebutuhan utama
  Parameter Normalisasi : Tidak digunakan.

Leakage Check:
  [x] Parameter normalisasi dari training set saja
  [✓] Tidak ada informasi test set dalam preprocessing
  [✓] Cross-validation dilakukan setelah preprocessing

Jumlah data akhir : 8784 records
Script tersedia   : [✓] Ya → path: experiment_final_part1.py, experiment_final_part2.py, experiment_final_part3.py, experiment_final_part4.py | [ ] Belum
```

---

## Latihan 1 — Cleaning Plan

Periksa dataset Anda (atau dataset contoh) dan dokumentasikan masalah yang ditemukan.

| Masalah | Jumlah Kasus | Penanganan | Justifikasi |
|---------|-------------|------------|-------------|
| Missing Value | 0 | Tidak ada tindakan | Dataset lengkap, tidak ditemukan nilai kosong |
| Duplikat | 0 | Tidak ada tindakan | Tidak ditemukan data duplikat |
| Error Format | 0 | Validasi format kolom | Seluruh kolom sesuai format numerik yang dibutuhkan |

**Jumlah data sebelum cleaning:** 8784
**Jumlah data setelah cleaning:** 8784
**Persentase data yang hilang/berubah:** 0%

---

## Latihan 2 — Normalisasi Decision

Tentukan apakah data Anda perlu normalisasi, dan jika ya, metode apa yang tepat.

| Variabel | Range Asli | Distribusi | Outlier? | Metode Normalisasi | Alasan |
|----------|-----------|-----------|----------|-------------------|--------|
| Solar | 0 – >1000 W/m² | Tidak normal | Ada variasi alami | Tidak dilakukan | Mempertahankan nilai fisik |
| Temperature | ±20 – 35 °C | Hampir normal | Tidak signifikan | Tidak dilakukan | Digunakan langsung dalam rumus koreksi suhu |
| Humidity | 0 –100 % | Normal | Tidak | Tidak dilakukan | Sudah dalam satuan persentase |
| Wind | >0 m/s | Normal | Tidak | Tidak dilakukan | Digunakan sebagai variabel lingkungan |
| PV Energy | 0 –100 Wh | Turunan hasil simulasi | Tidak | Tidak dilakukan | Merupakan output model |
| SOC | 20–100 % | Normal | Tidak | Tidak dilakukan | Merupakan output model |


**Apakah normalisasi diperlukan?** [ ] Ya / [✓] Tidak
**Justifikasi:**
> Penelitian ini menggunakan pendekatan simulasi berbasis model energi (PV Model, Energy Demand Model, Battery Model, dan Scheduler). Oleh karena itu, mempertahankan satuan asli setiap variabel lebih tepat agar hasil simulasi tetap memiliki makna fisik dan mudah diinterpretasikan. Normalisasi justru berpotensi menghilangkan interpretasi langsung terhadap besaran energi, suhu, maupun radiasi matahari.

**Leakage check:**
- [✓] Parameter dihitung dari training set saja
- [✓] Normalisasi diterapkan setelah train-test split

---

## Latihan 3 — Preprocessing Report

Buat ringkasan preprocessing lengkap — dokumentasi yang cukup bagi orang lain untuk mereplikasi.

```
PREPROCESSING SUMMARY

1. Dataset: NASA POWER Hourly Dataset Tahun 2024
2. Data awal: 8784 records, 8 features
3. Cleaning:
   - Missing values: 0 kasus, metode: Tidak diperlukan
   - Duplikat: 0 kasus, metode: Tidak diperlukan
   - Error: 0 kasus, metode: Validasi struktur dataset
4. Transformation: Dilakukan beberapa transformasi:Rename variabel, Pembuatan kolom Datetime, Pengurutan data berdasarkan waktu, Perhitungan PV Power, Perhitungan PV Energy, Perhitungan Energy Demand, Perhitungan Battery SOC
5. Normalisasi: Tidak dilakukan, Karena penelitian menggunakan simulasi berbasis model fisik sehingga mempertahankan satuan asli dianggap lebih tepat dibandingkan melakukan normalisasi._
6. Data akhir: 8784 records, 18+ fitur setelah penambahan hasil feature engineering.
7. Leakage check: [✓] Lulus / [ ] Ada masalah
```

---

## Refleksi

> Apakah Anda pernah melakukan normalisasi "karena biasa dilakukan" tanpa mempertimbangkan apakah benar-benar diperlukan? Apa risiko over-preprocessing?

> Pada awalnya saya menganggap bahwa normalisasi merupakan langkah yang harus selalu dilakukan sebelum analisis data. Setelah mempelajari proses preprocessing pada penelitian ini, saya memahami bahwa keputusan preprocessing harus disesuaikan dengan tujuan penelitian dan karakteristik metode yang digunakan. Karena penelitian ini menggunakan simulasi berbasis model energi, mempertahankan satuan asli seperti Watt, Wh, °C, %, dan W/m² lebih penting agar hasil simulasi tetap memiliki makna fisik dan mudah diinterpretasikan. Selain itu, saya juga menyadari bahwa preprocessing bukan sekadar proses teknis, tetapi merupakan bagian penting dari metodologi penelitian. Setiap langkah, mulai dari validasi dataset, pembersihan data, transformasi variabel, hingga pengecekan data leakage, harus didokumentasikan secara jelas agar penelitian dapat direproduksi oleh peneliti lain dan hasil yang diperoleh dapat dipertanggungjawabkan secara ilmiah.
> ___________________________________________________
