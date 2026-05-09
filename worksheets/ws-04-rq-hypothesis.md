# WS-04: Research Question & Hypothesis

> **Bab 4 — Research Question, Contribution & Hypothesis**

---

## Ringkasan Materi

### RQ Bukan Pertanyaan Biasa

Research Question yang baik secara implisit mengandung cetak biru eksperimen: subjek, baseline, metrik, domain, dataset.

| Kualitas | Contoh |
|----------|--------|
| **Buruk** | "Bagaimana pengaruh deep learning terhadap deteksi malware?" |
| **Baik** | "Apakah CNN menghasilkan F1-Score lebih tinggi dari RF pada CIC-MalMem-2022?" |

Perbedaan: RQ yang baik menyebutkan **metode spesifik**, **metrik terukur**, **baseline**, dan **dataset**.

### Tiga Jenis RQ

| Jenis | Pola | Kebutuhan |
|-------|------|-----------|
| **Comparison** | A vs B → mana lebih baik? | ≥ 2 metode, metrik sama |
| **Improvement** | A' vs A → modifikasi lebih baik? | Pre/post, bukti perbaikan |
| **Exploratory** | Faktor X₁...Xₙ → pengaruh terhadap Y? | Multi-variabel, korelasi/regresi |

### Contribution Statement

Tiga jenis kontribusi: **Improvement** (metode terbukti lebih baik), **Comparison** (perbandingan sistematis yang belum ada), **Novel Approach** (pendekatan baru). Kontribusi harus terhubung langsung dengan gap — kontribusi tanpa gap = klaim tanpa justifikasi.

### Hypothesis H₀ / H₁

- **H₀** (Null) = Tidak ada perbedaan signifikan — asumsi default, harus dibuktikan salah
- **H₁** (Alternative) = Ada perbedaan signifikan — diterima hanya jika H₀ ditolak
- Harus **falsifiable**, mengandung **metrik terukur**, dirumuskan **SEBELUM eksperimen**

### Rantai Operasionalisasi

```
RQ → Variable → Metric → Data → Analysis
```

Jika rantai ini tidak lengkap, RQ belum mature. Bi-directional: RQ yang tidak bisa jadi hipotesis testable harus direvisi mundur.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan pertanyaan | Apa yang harus dibangun? | Apa yang harus dibuktikan? |
| Bentuk jawaban | Sistem yang berfungsi | Bukti empiris terukur |
| Sukses diukur oleh | User satisfaction, uptime | Signifikansi statistik, effect size |
| Jika gagal | Debug dan perbaiki | Laporkan, analisis mengapa |

### Istilah Penting

- **Research Question (RQ)** — Pertanyaan spesifik: variabel terukur + metrik + konteks
- **Contribution Statement** — Apa yang diketahui setelah riset selesai yang sebelumnya belum ada
- **H₀ / H₁** — Null vs Alternative Hypothesis
- **Falsifiability** — Kondisi hipotesis ditolak harus bisa didefinisikan sebelum eksperimen
- **Operationalization** — Proses mewujudkan konsep abstrak menjadi variabel terukur

---

## Template A.4 — RQ-Contribution-Hypothesis

```
RQ-CONTRIBUTION-HYPOTHESIS

Gap Statement  : Mayoritas penelitian IoT + energi surya pada hidroponik hanya dilakukan di lingkungan laboratorium dengan pengujian jangka pendek dan minim evaluasi outcome pertumbuhan tanaman serta adaptasi terhadap konteks daerah terpencil dengan fluktuasi cuaca.

Research Question:
  Tipe         : [ ] Comparison  [v] Improvement  [ ] Exploratory
  Formulasi    : Apakah desain integrasi IoT holistik berbasis panel surya yang dikembangkan dapat meningkatkan efisiensi penggunaan energi dan kestabilan operasional sistem hidroponik cerdas dibandingkan pendekatan baseline IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil?
  Variabel IV  : Desain integrasi sistem (Proposed Holistic IoT-Solar Design vs Baseline)
  Variabel DV  : Efisiensi energi (%) dan kestabilan operasional (jam operasional tanpa gangguan)
  Metrik       : Efisiensi energi harian, waktu operasional 24 jam, akurasi kontrol lingkungan (suhu & kelembaban), serta indikator pertumbuhan tanaman (tinggi tanaman, jumlah daun)
  Dataset      : Data sensor real-time dari prototipe selama minimal 8–12 minggu pengujian (termasuk variasi cuaca)
  Baseline     : Sistem IoT hidroponik dengan panel surya dan otomasi dasar (seperti Wardhana et al., 2025)

Quality Check RQ:
  [v] Variabel spesifik
  [v] Metrik jelas
  [v] Baseline ada
  [v] Konteks disebutkan
  [v] Memerlukan eksperimen (bukan hanya survei literatur)

Contribution Statement:
  Apa yang baru diketahui : Penelitian ini akan memberikan bukti empiris mengenai efektivitas desain integrasi IoT holistik dengan manajemen energi surya adaptif pada konteks hidroponik di Indonesia, termasuk evaluasi jangka menengah dan indikator agronomis.
  Jenis kontribusi        : [v] Improvement  [ ] Comparison  [ ] Novel approach
  Gap yang diisi          : Context Gap dan Method Gap

Hypothesis Pair:
  H₀ : Tidak terdapat perbedaan yang signifikan pada efisiensi energi dan kestabilan operasional antara desain integrasi IoT holistik yang diusulkan dengan baseline sistem IoT solar sederhana.
  H₁ : Desain integrasi IoT holistik yang diusulkan menghasilkan efisiensi energi yang lebih tinggi (minimal +8%) dan kestabilan operasional yang lebih baik dibandingkan baseline pada pengujian selama 8 minggu.
  Threshold              : α = 0.05 (95% confidence level)
  Justifikasi threshold  : Standar statistik yang umum digunakan dalam penelitian eksperimental bidang teknik dan pertanian cerdas untuk menyeimbangkan antara risiko kesalahan tipe I dan kekuatan statistik.
```

---

## Latihan 1 — Dari Gap ke RQ

Gunakan gap yang ditemukan di WS-03. Transformasikan menjadi Research Question.

**Gap dari WS-03:** Context Gap + Method Gap (kurangnya integrasi holistik dan pengujian kontekstual di daerah terpencil)

**RQ versi pertama (tulis bebas):**
> “Bagaimana cara membuat sistem hidroponik IoT berbasis solar yang lebih baik?”

**Evaluasi RQ:**

| Komponen | Ada? | Isi |
|----------|------|-----|
| Metode spesifik | Tidak | Terlalu umum |
| Metrik terukur | Tidak | Belum ada metrik jelas |
| Baseline | Tidak | Tidak disebutkan |
| Dataset/konteks | Sebagian | Hanya “hidroponik” |

**Tipe RQ:** [ ] Comparison / [v] Improvement / [ ] Exploratory

**RQ versi revisi (setelah evaluasi):**
> “Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem (waktu operasi 24 jam tanpa gangguan) dibandingkan dengan baseline sistem IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil dengan variasi intensitas cahaya matahari?

---

## Latihan 2 — Hypothesis Pair

Rumuskan pasangan hipotesis dari RQ di Latihan 1.

| Komponen | Isi |
|----------|-----|
| H₀ | Tidak terdapat perbedaan yang signifikan pada efisiensi energi dan kestabilan operasional antara desain yang diusulkan dengan baseline. |
| H₁ | Desain integrasi IoT holistik yang diusulkan menghasilkan efisiensi energi lebih tinggi dan kestabilan operasional yang lebih baik dibandingkan baseline. |
| Metrik | Efisiensi energi (%), waktu operasional penuh (jam), deviasi suhu & kelembaban |
| Threshold | p-value < 0.05 dan effect size minimal sedang |
| Justifikasi threshold | Memberikan standar ilmiah yang ketat sekaligus realistis untuk penelitian prototipe |

**Apakah hipotesis ini falsifiable?** [v] Ya / [ ] Tidak
> Bagaimana cara membuktikannya salah? Dengan melakukan pengujian statistik (t-test atau ANOVA) dan menemukan bahwa tidak ada perbedaan signifikan atau bahkan desain yang diusulkan lebih buruk dari baseline pada metrik utama.

---

## Latihan 3 — Rantai Operasionalisasi

Lengkapi rantai dari RQ hingga metode analisis.

| Tahap | Isi |
|-------|-----|
| RQ | Apakah desain integrasi IoT holistik berbasis panel surya yang dikembangkan dapat meningkatkan efisiensi penggunaan energi dan kestabilan operasional sistem hidroponik cerdas dibandingkan pendekatan baseline IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil? |
| Variable (IV) | Jenis desain sistem (Proposed Holistic vs Baseline) |
| Variable (DV) | Efisiensi energi, kestabilan operasional, dan performa pertumbuhan tanaman |
| Metric | Persentase efisiensi energi, uptime 24 jam, rata-rata deviasi sensor, tinggi tanaman |
| Data source | Log sensor real-time, pengukuran multimeter, observasi pertumbuhan tanaman selama 8–12 minggu |
| Analysis method | Statistik deskriptif, independent t-test / Mann-Whitney, grafik perbandingan, analisis sensitivitas cuaca |

**Apakah rantai lengkap?** [v] Ya / [ ] Tidak
> Jika tidak, tahap mana yang perlu direvisi? ______________

---

## Refleksi

> Ambil satu judul skripsi/paper yang pernah dibaca. Coba ekstrak RQ-nya. Apakah RQ tersebut memenuhi semua komponen (metode, metrik, baseline, konteks)? Jika tidak, apa yang hilang?

**Judul:** Judul: Desain dan Prototipe Integrasi IoT dalam Pertanian Hidroponik Cerdas Berbasis Energi Terbarukan (Wardhana et al., 2025)
**RQ yang diekstrak:** “Bagaimana merancang prototipe sistem otomasi hidroponik berbasis IoT yang didukung panel surya untuk meningkatkan efisiensi energi?”
**Komponen yang hilang:** Tidak ada baseline yang jelas untuk perbandingan, Metrik utama kurang spesifik (hanya “efisien” tanpa target persentase atau statistical test), Konteks pengujian kurang mendalam (tidak menyebutkan durasi panjang atau variasi cuaca ekstrem), Belum ada hipotesis yang dapat difalsifikasi. Dari refleksi ini, saya semakin menyadari pentingnya merumuskan RQ dan hipotesis dengan ketat sejak awal agar riset tidak hanya “membuat sesuatu yang keren”, tetapi benar-benar menghasilkan pengetahuan yang kredibel dan bermanfaat.
