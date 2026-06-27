# WS-08: Proposal Integration (UTS)

> **Bab 8 — Proposal & Checkpoint**

---

## Ringkasan Materi

### Proposal = Satu Argumen Utuh

Proposal riset bukan kumpulan bab yang independen. Ia adalah **satu argumen** yang mengalir dari masalah ke rencana solusi. Jika satu koneksi putus, seluruh proposal kehilangan koherensi.

### Integration Map — 6 Koneksi Kritis

```
Problem (Bab 2) → Gap (Bab 3) → RQ & H (Bab 4) → Metrik (Bab 5) → Sistem (Bab 6) → Eksperimen (Bab 7)
```

| Koneksi | Pertanyaan Verifikasi |
|---------|----------------------|
| Problem → Gap | Apakah gap muncul dari analisis literatur terhadap masalah? |
| Gap → RQ | Apakah RQ langsung menjawab gap yang teridentifikasi? |
| RQ → Metrik | Apakah setiap variabel di RQ punya metrik terdefinisi? |
| Metrik → Sistem | Apakah setiap metrik bisa diukur oleh komponen sistem? |
| Sistem → Eksperimen | Apakah desain eksperimen menggunakan sistem sebagai instrumen? |

### Koherensi Vertikal + Horizontal

- **Vertikal** — Alur logis atas-ke-bawah (problem → experiment). Setiap section menjawab pertanyaan yang diangkat section sebelumnya dan memunculkan pertanyaan baru.
- **Horizontal** — Konsistensi terminologi (nama variabel di RQ = di hipotesis = di metrik = di desain)

**Operasionalisasi Red Thread** (benang merah):
```
Bab 2 (Problem) → | memperkenalkan masalah X + evidensi |
                          ↓ menimbulkan pertanyaan: "apa akar gap-nya?"
Bab 3 (Gap)     → | menjawab pertanyaan tadi + membuka "lalu apa yang perlu diteliti?" |
                          ↓
Bab 4 (RQ/H)    → | menjawab gap dengan pertanyaan spesifik + prediksi terukur |
                          ↓
Bab 5-7 (Method)→ | menjawab RQ melalui desain eksperimen yang tepat |
```
Jika ada lompatan (section B tidak menjawab pertanyaan section A), red thread putus.

### Jebakan Kognitif

| Jebakan | Deskripsi |
|---------|----------|
| "Selling" Introduction | Menulis promosi, bukan menyajikan data dan gap |
| Copy-paste Methodology | Menyalin deskripsi tekstbook tanpa menyesuaikan ke RQ |
| Optimistic Timeline | Meremehkan waktu implementasi; selalu tambah buffer 30-50% |
| No Possibility of Failure | Mengimplikasikan hasil pasti sukses — proposal jujur mengakui H₀ mungkin tidak ditolak |

### Struktur Proposal

1. **Pendahuluan** — Latar belakang + problem statement (Bab 1-2)
2. **Tinjauan Pustaka** — Literature review + gap + baseline (Bab 3)
3. **RQ / Kontribusi / Hipotesis** — (Bab 4)
4. **Metodologi** — Metrik + sistem + desain eksperimen (Bab 5-7)
5. **Timeline & Output**

### Istilah Penting

- **Integration Map** — Diagram 6 koneksi kritis antar komponen proposal
- **Vertical Coherence** — Alur logis atas-ke-bawah
- **Horizontal Coherence** — Konsistensi terminologi di semua bagian
- **Checkpoint** — Titik self-assessment sebelum transisi dari desain ke eksekusi

---

## Template A.8 — Integration Checklist

```
PROPOSAL INTEGRATION CHECKLIST

Koneksi Vertikal (Flow Atas-Bawah):
  [✓] Problem → Gap: masalah terdokumentasi di literatur
  [✓] Gap → RQ: pertanyaan menjawab gap spesifik
  [✓] RQ → Hypothesis: hipotesis memprediksi jawaban
  [✓] Hypothesis → Metric: metrik mengukur variabel dalam hipotesis
  [✓] Metric → System: komponen sistem menghasilkan/mengukur metrik
  [✓] System → Experiment: desain eksperimen menggunakan sistem

Koneksi Horizontal (Konsistensi):
  [✓] Istilah sama di semua bagian
  [✓] Variabel di RQ = variabel di hipotesis = metrik di desain
  [✓] Scope tidak berubah dari masalah ke eksperimen

Cognitive Trap Checklist:
  [✓] Tidak ada paragraf "promosi" di pendahuluan (hanya data & gap)
  [✓] Metodologi disesuaikan ke RQ, bukan copy-paste textbook
  [✓] Timeline sudah ditambah buffer 30-50% dari estimasi awal
  [✓] Proposal mengakui kemungkinan H0 tidak ditolak (honest uncertainty)
  [✓] Tidak ada klaim "pasti berhasil" atau "meningkatkan signifikan"

Rubrik Self-Assessment:
| Kriteria     | 1 (Lemah)                                        | 2 (Cukup)                                     | 3 (Baik)                                           | Skor |
|------------- |--------------------------------------------------|-----------------------------------------------|----------------------------------------------------|------|
| Koherensi    | >2 koneksi vertikal terputus                     | 1-2 koneksi lemah, argumen masih bisa diikuti | Semua 6 koneksi terhubung, red thread jelas        |   3  |
| Specificity  | Variabel/metrik masih abstrak, tidak ada angka   | Sebagian metrik terdefinisi numerik           | Semua metrik + threshold + unit pengukuran jelas   |   3  |
| Feasibility  | Timeline >6 bulan tanpa memperhitungkan sumber   | Timeline 3-6 bulan dengan asumsi tertentu     | Timeline 1-3 bulan realistis dengan rencana detail |   3  |
| Rigor        | Baseline tidak jelas atau straw man              | 1-2 baseline dengan justifikasi partial       | 2+ baseline SOTA + justifikasi pemilihan lengkap   |   3  |
```

---

## Latihan 1 — Kompilasi Proposal Mini

Kumpulkan hasil dari WS-02 sampai WS-07 menjadi satu ringkasan proposal.

| Komponen | Sumber | Isi (1-2 kalimat) |
|----------|--------|-------------------|
| Problem Statement | WS-02 | Pertanian hidroponik menawarkan solusi efisien penggunaan lahan dan air, namun masih menghadapi biaya energi tinggi dan ketergantungan listrik konvensional yang tidak stabil di daerah terpencil. Akar masalahnya adalah kurangnya integrasi holistik antara otomasi IoT dengan manajemen energi surya yang adaptif terhadap fluktuasi cuaca. |
| Gap | WS-03 | Dari 7 paper yang ditinjau, terdapat Context Gap (6 dari 7 paper hanya diuji di laboratorium, bukan simulasi daerah terpencil dengan fluktuasi cuaca ekstrem) dan Method Gap (5 dari 7 paper hanya integrasi parsial, belum ada pendekatan holistik dengan manajemen energi adaptif disertai evaluasi agronomis). |
| RQ | WS-04 | Apakah desain integrasi IoT holistik dengan Adaptive Energy Scheduler berbasis panel surya mampu meningkatkan efisiensi penggunaan energi minimal 8% dan kestabilan operasional dibandingkan baseline sistem IoT solar sederhana (rule-based) pada prototipe hidroponik cerdas yang diuji selama 7 hari (8 jam/hari) di bawah variasi simulasi intensitas cahaya matahari kondisi daerah terpencil? |
| Hipotesis | WS-04 | H₀: Tidak ada perbedaan signifikan pada efisiensi energi dan kestabilan operasional antara desain holistik dengan adaptive scheduler dan baseline rule-based. H₁: Desain holistik dengan adaptive scheduler menghasilkan efisiensi energi minimal 8% lebih tinggi dan kestabilan operasional yang lebih baik (α = 0.05). |
| Variabel & Metrik | WS-05 | IV = Desain Sistem (Holistic Adaptive vs Rule-based Baseline); DV = Efisiensi Penggunaan Energi (%) dan Kestabilan Operasional (Uptime %); Secondary Metrics = Deviasi suhu/kelembaban dan pertumbuhan tanaman (tinggi & jumlah daun). |
| Sistem | WS-06 | Sistem dirancang modular dengan komponen utama: Energy Harvesting & Storage, Sensor Layer, Actuator Layer, Adaptive Energy Scheduler (core innovation), dan IoT Monitoring Layer. Arsitektur configuration-driven memungkinkan variable isolation. |
| Desain Eksperimen | WS-07 | Tipe eksperimen: Comparison Study dengan elemen Ablation Study. Baseline (A): Sistem IoT solar rule-based. Treatment (B): Sistem IoT holistik dengan Adaptive Energy Scheduler. Pengujian dilakukan selama 7 hari (8 jam/hari) dengan variasi simulasi cuaca. Analisis menggunakan Independent t-test / Mann-Whitney U Test (α=0.05). |

---

## Latihan 2 — Integration Checklist

Verifikasi 6 koneksi kritis. Isi dengan merujuk tabel di Latihan 1.

| Koneksi | Status | Bukti |
|---------|--------|-------|
| Problem → Gap | ✓ | Problem (biaya energi tinggi & ketidakstabilan di daerah terpencil) langsung dihubungkan dengan Context Gap (6 dari 7 paper hanya uji lab) dan Method Gap (5 dari 7 paper hanya integrasi parsial). |
| Gap → RQ | ✓ | RQ secara spesifik menanyakan apakah desain holistik dengan Adaptive Energy Scheduler dapat meningkatkan efisiensi energi dan kestabilan di kondisi daerah terpencil, langsung menjawab kedua gap. |
| RQ → Hypothesis | ✓ | H₁ memprediksi peningkatan efisiensi energi minimal 8% dan kestabilan operasional yang lebih baik, sesuai dengan metrik yang disebutkan di RQ. |
| Hypothesis → Metric | ✓ | Metrik utama (efisiensi energi %, uptime, deviasi lingkungan, pertumbuhan tanaman) langsung mengukur variabel yang ada di hipotesis. |
| Metric → System | ✓ | Komponen sistem (Adaptive Energy Scheduler, Sensor Layer, Actuator Layer) dirancang khusus untuk menghasilkan dan mengukur metrik tersebut. |
| System → Experiment | ✓ | Desain eksperimen (comparison study selama 7 hari × 8 jam/hari dengan variasi simulasi cuaca) menggunakan sistem modular untuk menguji IV (holistic vs baseline). |

**Koneksi mana yang paling lemah?** Tidak ada koneksi yang lemah — semua sudah sangat kuat dan saling terhubung.
**Bagaimana cara memperkuatnya?**
> Sudah sangat baik. Untuk lebih kuat lagi, bisa ditambahkan visual flowchart yang menghubungkan semua elemen di proposal akhir.

**Konsistensi horizontal — apakah istilah dan scope konsisten?** [✓] Ya / [ ] Tidak
> Jika tidak, di bagian mana terjadi inkonsistensi? Tidak ada inkonsistensi. Istilah kunci (Adaptive Energy Scheduler, holistic design, baseline rule-based, efisiensi energi, daerah terpencil) digunakan secara konsisten dari Problem hingga Eksperimen. Scope juga tetap fokus pada fluktuasi energi di daerah terpencil.

---

## Latihan 3 — Rubrik Self-Assessment

Evaluasi proposal mini menggunakan rubrik.

| Kriteria | Skor (1-3) | Justifikasi |
|----------|-----------|-------------|
| Koherensi | 3 | Semua 6 koneksi vertikal sangat kuat dan saling terhubung (Problem → Gap → RQ → Hypothesis → Metric → System → Experiment). Red thread dari fluktuasi energi di daerah terpencil hingga eksperimen sangat jelas. |
| Specificity | 3 | Semua metrik sudah terdefinisi numerik dan operasional (efisiensi energi ≥8%, uptime 24 jam, deviasi suhu/kelembaban, pertumbuhan tanaman) beserta unit dan cara ukur. |
| Feasibility | 3 | Timeline 7 hari × 8 jam/hari sangat realistis untuk mahasiswa, dengan buffer persiapan dan analisis yang memadai. |
| Rigor | 3 | Baseline jelas (rule-based), ada 2+ referensi SOTA, justifikasi pemilihan lengkap, serta mitigasi validitas yang komprehensif. |

**Skor total:** 12 / 12

**Apakah proposal siap untuk fase eksekusi?** [✓] Ya / [ ] Belum
> Jika belum, apa yang perlu diperbaiki? Tidak ada yang perlu diperbaiki secara signifikan. Proposal sudah sangat siap untuk fase eksekusi.

---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-08, bagian mana yang paling mudah dan paling sulit? Mengapa? Apa yang akan dilakukan berbeda jika mengulang dari awal?

**Bagian termudah:** Problem Statement & Gap — Karena paper yang diunggah sudah memberikan konteks yang jelas, sehingga mudah mengidentifikasi akar masalah dan gap dari literatur.
**Bagian tersulit:** Desain Eksperimen & Validitas — Karena harus memastikan fairness, isolasi variabel, dan mitigasi ancaman validitas secara detail agar klaim ilmiah tetap kuat, terutama di durasi yang pendek.
**Yang akan dilakukan berbeda:**
> Saya akan lebih awal membuat tabel mapping besar (Problem–Gap–RQ–Metric–System–Experiment) sejak WS-02 agar konsistensi horizontal lebih mudah dijaga sepanjang proses. Selain itu, saya akan langsung memutuskan durasi eksperimen yang realistis sejak awal agar tidak perlu revisi berulang.
