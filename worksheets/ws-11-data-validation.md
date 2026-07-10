# WS-11: Data Validation & Integrity

> **Bab 11 — Validasi Data & Integritas**

---

## Ringkasan Materi

### Data Trust Model

```
Raw Data → Data Cleaning → Consistency Check → Validation Process → Trusted Data
```

Data mentah belum bisa dipercaya. Harus melewati pipeline validasi sebelum siap untuk analisis statistik.

### Empat Pilar Data Quality

| Pilar | Deskripsi | Contoh Pelanggaran |
|-------|----------|-------------------|
| **Accuracy** | Nilai dalam range masuk akal | Akurasi = 1.5 (di luar [0,1]) |
| **Consistency** | Format seragam di semua run | Run 1: CSV, Run 2: JSON |
| **Completeness** | Tidak ada data hilang dari plan | 97 dari 100 run tercatat |
| **Validity** | Data sesuai desain eksperimen | Parameter baseline tercampur treatment |

### Proses Validasi Progresif

1. **Format validation** — Tipe file, header, kolom
2. **Range validation** — Nilai dalam batas logis
3. **Consistency validation** — Format seragam antar-run
4. **Logic validation** — Data cocok dengan desain eksperimen

Jika gagal di langkah awal → tidak perlu lanjut.

### Anomaly Detection — 3 Jenis

| Jenis | Deskripsi | Deteksi |
|-------|----------|---------|
| **Statistical outlier** | Nilai di luar distribusi normal | IQR: < Q1-1.5×IQR atau > Q3+1.5×IQR |
| **Contextual anomaly** | Normal absolut, abnormal dalam konteks | Run 1-10: ~91%, Run 11-20: ~88% |
| **Pattern anomaly** | Pola sistematis (bukan random) | Performa menurun berurutan |

**Prinsip:** Detect → Investigate → Document → Decide — **JANGAN langsung hapus.**

### Engineering vs Research Validation

| Aspek | Engineering | Research |
|-------|-----------|---------|
| Tujuan | Data sesuai spesifikasi bisnis | Data layak untuk analisis statistik |
| Missing data | Impute / set default | Investigasi penyebab → dokumentasi |
| Outlier | Bug → fix | Mungkin temuan → investigasi |
| Dokumentasi | Minimal (log error) | Komprehensif (anomali + keputusan) |

### Jebakan Kognitif

1. "Logging otomatis ≠ data benar" → bisa ada bug di logger
2. "Outlier = hapus" → bisa jadi temuan penting
3. "Dataset kecil tidak perlu validasi" → justru lebih rentan
4. "Mean normal = data benar" → [94, 95, 93, **44**, 94] → mean 84% terlihat wajar

---

## Template A.11 — Data Validation Checklist

```
DATA VALIDATION CHECKLIST

Completeness:
  [✓] Semua skenario tercakup
  [✓] Jumlah run sesuai rencana
  [✓] Tidak ada file output hilang
  Missing: 0 dari 5 data points

Format Consistency:
  [✓] Semua file format sama (CSV/JSON/...)
  [✓] Header konsisten
  [✓] Tipe data konsisten (numerik tetap numerik)

Range & Logic:
  [✓] Solar Radiation ≥ 0
  [✓] Temperature valid
  [✓] Humidity 0–100%
  [✓] SOC 20–100%
  [✓] Rule Efficiency 0–100%
  [✓] Adaptive Efficiency 0–100%
  [✓] Improvement
  Anomali ditemukan: Tidak ada anomali kritis.

Cross-Validation:
  [✓] Run identik → hasil mendekati
  [✓] Trend konsisten dengan ekspektasi teori

Keputusan:
  [✓] Data siap analisis
  [ ] Perlu cleaning
  [ ] Perlu re-run (skenario: ____)
```

---

## Latihan 1 — Completeness Check

Verifikasi apakah semua data yang direncanakan sudah terkumpul.

| Skenario | Run Direncanakan | Run Tercatat | Missing | Alasan |
|----------|-----------------|-------------|---------|--------|
| Adaptive Energy Scheduler | 5 | 5 | 0 | Semua eksperimen berhasil dijalankan. |


**Total expected:** 5 | **Total actual:** 5 | **Missing:** 0

**Keputusan untuk data missing:**
> Tidak ada missing. Semua run berhasil dicata

---

## Latihan 2 — Anomaly Investigation

Periksa data Anda untuk anomali. Gunakan metode IQR atau z-score.

**Dataset sampel (atau data Anda sendiri):**

| Run | Rule Efficiency (%) | Adaptive Efficiency (%) | Average SOC (%) |
|-----|-------------|--------------|-------------|
| 1 | 40.50 | 42.24 | 51.05 |
| 2 | 40.17 | 42.07 | 50.81 |
| 3 | 40.40 | 42.19 | 50.94 |
| 4 | 40.46 | 42.22 | 51.01 |
| 5 | 40.49 | 42.24 | 51.05 |

**Deteksi outlier:**
Rule Efficiency
- Q1 = 40.40 | Q3 = 40.49 | IQR = 0.09
- Batas bawah 40.40 - (1.5×0.09) = 40.655
- Batas atas 40.49 + (1.5×0.09) = 40.625
- Outlier terdeteksi: -

Adaptive Efficiency
- Q1 = 42.19 | Q3 = 42.24 | IQR = 0.05
- Batas bawah 42.19 - (1.5×0.05) = 42.19
- Batas atas 42.24 + (1.5×0.05) = 42.24
- Outlier terdeteksi: -

**Investigasi (untuk setiap outlier):**

| Outlier | Nilai | Kemungkinan Penyebab | Keputusan |
|---------|-------|---------------------|-----------|
|Tidak ada | - | Variasi antar-run masih berada dalam rentang normal | Seluruh data dipertahankan |

---

## Latihan 3 — Validation Report

Buat laporan validasi ringkas untuk dataset eksperimen Anda.

**1. Completeness:** 100% data berhasil dikumpulkan. Seluruh 5 eksperimen berhasil dijalankan sesuai execution plan dan menghasilkan seluruh file output yang dibutuhkan.
**2. Format:** [✓] Konsisten / [ ] Ada inkonsistensi: -
**3. Range check (anomali):** Seluruh variabel berada pada rentang yang valid. Solar Radiation ≥ 0, Temperature sesuai dataset NASA,  Humidity 0–100%, SOC 20–100%, Rule Efficiency 0–100%, Adaptive Efficiency 0–100%

Tidak ditemukan nilai yang melampaui batas logis.
**4. Logic check:** [✓]] Parameter sesuai plan / [ ] Ada ketidaksesuaian: ____

**Kesimpulan:** [✓]] Data siap analisis / [ ] Perlu tindakan: Re-run Run 4 jika diperlukan untuk mengurangi outlier

---

## Refleksi

> Apa perbedaan antara "data yang benar" dan "data yang dipercaya"? Mengapa proses validasi formal diperlukan meskipun data dikumpulkan secara otomatis?

> Pada awal penelitian, saya menganggap bahwa data yang dihasilkan secara otomatis oleh program sudah pasti benar. Namun setelah mempelajari proses validasi data, saya memahami bahwa data yang benar belum tentu dapat dipercaya apabila belum melalui proses pemeriksaan kelengkapan, konsistensi, rentang nilai, serta kesesuaian dengan desain eksperimen. Melalui proses validasi pada penelitian ini, seluruh output diperiksa mulai dari jumlah data, struktur file, konsistensi format, hingga pemeriksaan rentang nilai setiap variabel. Hasil validasi menunjukkan bahwa dataset memiliki 8784 data, tidak terdapat missing value, tidak terdapat duplicate record, seluruh variabel berada pada rentang yang valid, serta lima kali eksperimen berhasil menghasilkan output yang konsisten. Oleh karena itu, data dinyatakan layak digunakan untuk analisis statistik dan evaluasi performa Rule-Based Scheduler maupun Adaptive Energy Scheduler.
