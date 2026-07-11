# WS-14: Analysis, Interpretation & Failure Analysis

> **Bab 14 — Analisis Data, Interpretasi & Failure Analysis**

---

## Ringkasan Materi

### Data → Knowledge Model

```
Data → Analysis → Interpretation → Explanation → Knowledge
```

Tiga level yang berbeda:
- **Analysis** — "Apa yang terjadi?" (deskriptif + inferensial)
- **Interpretation** — "Apa artinya?" (konteks RQ + literatur)
- **Failure Analysis** — "Mengapa tidak berhasil?" (boundary conditions)

### Beyond p-value

**Statistical significance ≠ practical significance.** Selalu laporkan:
1. p-value (signifikansi statistik)
2. Effect size (besarnya efek)
3. Confidence interval (rentang ketidakpastian)

| Effect Size (Cohen's d) | Interpretasi |
|-------------------------|-------------|
| < 0.2 | Small |
| 0.2 – 0.8 | Medium |
| > 0.8 | Large |

### Pemilihan Uji Statistik

| Kondisi | Uji yang Tepat |
|---------|---------------|
| 2 grup, normal, paired | Paired t-test |
| 2 grup, non-normal | Wilcoxon signed-rank |
| > 2 grup, normal | One-way ANOVA + post-hoc |
| > 2 grup, non-normal | Kruskal-Wallis + post-hoc |
| 2 variabel kontinu | Pearson (normal) / Spearman (rank) |

### Failure Analysis as Contribution

Hipotesis yang ditolak adalah **temuan yang berharga**:

| Dataset | New (F1) | Baseline (F1) | p-value | Cohen's d |
|---------|---------|--------------|---------|-----------|
| DS-1 (small, clean) | 94.2±1.1 | 89.3±1.5 | <0.001 | **3.7** |
| DS-4 (medium, noisy) | 78.3±3.2 | 82.1±2.8 | 0.008 | **-1.3** |
| DS-5 (large, noisy) | 71.6±4.1 | 80.5±3.0 | <0.001 | **-2.5** |

**Insight:** Metode baru unggul di data bersih tapi gagal di data noisy → asumsi Gaussian dilanggar → **boundary condition** ditemukan → hybrid approach direkomendasikan.

**Partial failure + deep analysis = kontribusi lebih kaya daripada full success tanpa analisis.**

### Limitation Types

| Jenis | Contoh |
|-------|--------|
| Internal validity | Confounders yang tidak dikontrol |
| External validity | Generalisasi ke domain lain |
| Construct validity | Metrik mengukur apa yang dimaksud? |
| Statistical limitation | Sample size, asumsi distribusi |

### Jebakan Kognitif

1. "Signifikan statistik = penting secara praktis" → cek effect size
2. "Hipotesis tidak didukung → cari sudut baru" → p-hacking
3. "Kegagalan tidak perlu dilaporkan detail" → missed insight
4. "Limitasi cukup disebutkan, tidak perlu dianalisis" → kedalaman hilang

---

## Template A.14 — Analysis & Interpretation Report

```
ANALYSIS & INTERPRETATION

1. Statistik Deskriptif:
   | Skenario | Mean | Std | Median | Min | Max | n |
   |----------|------|-----|--------|-----|-----|---|
   | Rule-Based Scheduler | 40.40 | 0.14 | 40.46 | 40.17 | 40.50 | 5 |
   | Adaptive Energy Scheduler | 42.19 | 0.07 | 42.22 | 42.07 | 42.24 | 5 |

2. Ringkasan Statistik
   | Parameter | Nilai |
   |-----------|-------|
   | Rule Mean | 40.40 % |
   | Adaptive Mean | 42.19 % |
   | Mean Improvement | 1.79 % |
   | Rule Std | 0.14 |
   | Adaptive Std | 0.07 |
   | Dataset | NASA POWER 2024 |
   | Jumlah Data | 8784 |

3. Uji Hipotesis: H0 : Adaptive Energy Scheduler tidak memberikan peningkatan efisiensi dibandingkan Rule-Based Scheduler. H1 : Adaptive Energy Scheduler memberikan peningkatan efisiensi dibandingkan Rule-Based Scheduler.
   Uji yang digunakan  : Paired t-test (direncanakan)
   Justifikasi          : Karena setiap run Rule-Based dibandingkan langsung dengan run Adaptive pada kondisi eksperimen yang sama sehingga data bersifat berpasangan (paired).
   Hasil
   | Parameter | Nilai |
   |-----------|-------|
   | p-value | Belum dihitung |
   | Effect Size | Belum dihitung |
   | Confidence Interval | Belum dihitung |

4. Keputusan:
   [ ] H₀ ditolak → H₁ diterima
   [ ] H₀ tidak ditolak
   ☑ Belum dapat diputuskan karena uji inferensial belum dilakukan.

5. Interpretasi:
   Hubungan ke RQ       : Hasil eksperimen menunjukkan bahwa Adaptive Energy Scheduler memiliki rata-rata efisiensi sebesar 42.19%, sedangkan Rule-Based Scheduler memperoleh rata-rata 40.40%. Selisih rata-rata sebesar 1.79% mengindikasikan adanya peningkatan performa pada metode adaptif dibandingkan metode berbasis aturan. Namun demikian, berdasarkan data yang tersedia saat ini, peningkatan tersebut baru dapat disimpulkan secara deskriptif. Untuk menyatakan apakah peningkatan tersebut signifikan secara statistik masih diperlukan pengujian inferensial.
   Practical significance: Secara praktis, peningkatan efisiensi sebesar 1.79% menunjukkan bahwa pendekatan adaptif mampu memanfaatkan energi panel surya sedikit lebih baik dibandingkan pendekatan Rule-Based pada konfigurasi simulasi yang digunakan. Walaupun peningkatannya relatif kecil, hasil ini menunjukkan bahwa konsep penjadwalan adaptif memiliki potensi untuk dikembangkan lebih lanjut melalui penyempurnaan algoritma pengambilan keputusan dan pengendalian beban.
   Perbandingan literatur: Hasil penelitian ini sejalan dengan berbagai penelitian mengenai Energy Management System yang menunjukkan bahwa metode adaptif cenderung memberikan efisiensi lebih baik dibandingkan metode berbasis aturan tetap. Akan tetapi, peningkatan efisiensi sangat dipengaruhi oleh model kontrol, karakteristik beban, kapasitas baterai, dan kondisi lingkungan yang digunakan dalam simulasi.

6. Limitation:
   | Jenis | Ancaman | Dampak | Mitigasi |
   |-------|---------|--------|----------|
   | Internal Validity | Scheduler masih sederhana | Peningkatan efisiensi belum maksimal | Mengembangkan algoritma adaptif yang lebih kompleks |
   | External Validity | Dataset hanya berasal dari satu lokasi NASA POWER| Generalisasi ke lokasi lain terbatas | Menguji dataset dari beberapa lokasi geografis |
   | Statistical | Jumlah eksperimen hanya 5 run | Analisis inferensial masih terbatas | Menambah jumlah run pada penelitian lanjutan |
   | Construct Validity | Hanya menggunakan efisiensi energi sebagai indikator utama | Belum mengevaluasi aspek lain seperti waktu respon atau stabilitas | Menambahkan metrik evaluasi lain |

6. Failure Analysis (jika H₀ tidak ditolak):
   Penyebab potensial  : Model Adaptive Scheduler masih menggunakan pendekatan berbasis skor sederhana. Beban listrik belum benar-benar dikendalikan secara dinamis. Variasi antar-run hanya menggunakan perubahan parameter kecil sehingga karakteristik eksperimen masih relatif seragam.
   Boundary condition   : Adaptive Scheduler memberikan peningkatan pada konfigurasi simulasi yang digunakan, tetapi belum menunjukkan peningkatan yang besar ketika kondisi sistem relatif stabil dan variasi lingkungan terbatas.
   Insight              : Peningkatan efisiensi yang kecil menunjukkan bahwa Adaptive Scheduler masih memiliki ruang pengembangan, misalnya dengan: optimasi bobot keputusan, prediksi energi panel surya, prediksi beban listrik, penerapan logika fuzzy, reinforcement learning, atau Model Predictive Control (MPC).
```

---

## Latihan 1 — Pemilihan Uji Statistik

Tentukan uji statistik yang tepat untuk eksperimen Anda.

| Pertanyaan | Jawaban |
|-----------|---------|
| Berapa grup yang dibandingkan? | 2 (Rule-Based dan Adaptive Scheduler) |
| Apakah data berpasangan (paired)? | Ya |
| Apakah distribusi normal? (uji normalitas) | Belum diuji |
| **Uji yang dipilih:** | Paired t-test (apabila data normal) atau Wilcoxon Signed-Rank Test (apabila tidak normal) |
| **Justifikasi:** | Data berasal dari lima run pada kondisi eksperimen yang sama sehingga bersifat berpasangan. |

**Effect size yang akan dilaporkan:** [✓] Cohen's d / [ ] Eta-squared / [ ] Lainnya: ____

---

## Latihan 2 — Interpretasi Hasil

Gunakan data berikut (atau data riil Anda) untuk berlatih interpretasi.

**Data:**
| Model | Accuracy (mean ± std) | n |
|-------|----------------------|---|
| Rule-Based Scheduler | 40.40 ± 0.14 % | 5 |
| Adaptive Energy Scheduler | 42.19 ± 0.07 % | 5 |

Catatan: Uji statistik inferensial (misalnya paired t-test atau Wilcoxon signed-rank test) belum dilakukan pada penelitian ini. Oleh karena itu, bagian p-value, Cohen's d, dan Confidence Interval belum dapat dilaporkan sebagai hasil nyata.

| Aspek | Interpretasi |
|-------|--------------|
| Signifikansi Statistik | Belum dihitung sehingga belum dapat disimpulkan |
| Effect Size | Belum dihitung |
| Practical Significance | Adaptive Scheduler memberikan peningkatan efisiensi rata-rata sebesar 1.79%. |
| Hubungan dengan RQ | Adaptive Scheduler menunjukkan performa lebih baik dibanding Rule-Based Scheduler. |
| Perbandingan Literatur | Sejalan dengan penelitian EMS yang menunjukkan metode adaptif cenderung lebih efisien. |

---

## Latihan 3 — Failure Analysis

Latih kemampuan failure analysis: hipotesis TIDAK didukung. Apa yang bisa dipelajari?

**Skenario:** Metode baru Anda mendapat F1 = 83.2%, baseline = 84.7%. p = 0.12 (tidak signifikan).

| Pertanyaan | Jawaban |
|-----------|---------|
| Apakah ini "gagal"? | Tidak. Adaptive Scheduler tetap memberikan peningkatan meskipun belum besar. |
| Kemungkinan penyebab? | Algoritma adaptif masih sederhana dan belum mengubah konsumsi beban secara dinamis. |
| Boundary condition? | Efektivitas terbatas pada konfigurasi simulasi dengan variasi parameter kecil. |
| Insight yang bisa diambil? | Adaptive Scheduler perlu dikembangkan agar mampu mengontrol beban secara lebih adaptif terhadap perubahan lingkungan. |
| Apakah layak dilaporkan? Mengapa? | Ya. Hasil ini menunjukkan batas kemampuan metode yang digunakan dan memberikan arah pengembangan penelitian selanjutnya. |

**Limitation terkait:**
| Jenis | Ancaman | Dampak |
|-------|---------|--------|
| Statistical | Jumlah run hanya 5 | Kekuatan uji statistik masih rendah |
| Algorithmic | Adaptive Scheduler sederhana | Peningkatan efisiensi belum optimal |
| Dataset | Satu lokasi NASA POWER | Generalisasi terbatas |

---

## Refleksi

> Apakah "failure" dalam riset benar-benar gagal, atau justru kontribusi? Bagaimana failure analysis mengubah cara Anda melihat hasil negatif?

> Melalui proses analisis ini saya memahami bahwa hasil penelitian tidak hanya dinilai dari besar kecilnya peningkatan performa, tetapi juga dari bagaimana hasil tersebut dianalisis dan dijelaskan. Peningkatan efisiensi sebesar 1.79% memang belum besar, namun tetap memberikan informasi bahwa pendekatan adaptif memiliki potensi untuk meningkatkan pengelolaan energi dibandingkan metode Rule-Based pada konfigurasi yang digunakan.
> Selain itu, saya menyadari bahwa failure analysis bukan berarti menunjukkan kegagalan penelitian, melainkan membantu mengidentifikasi batas kemampuan metode yang dikembangkan. Dengan mengetahui penyebab peningkatan yang masih terbatas, penelitian lanjutan dapat difokuskan pada penyempurnaan algoritma, penambahan skenario eksperimen, serta evaluasi menggunakan lebih banyak dataset sehingga kontribusi ilmiahnya menjadi lebih kuat.
