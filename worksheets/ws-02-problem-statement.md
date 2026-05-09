# WS-02: Problem Statement

> **Bab 2 — Problem Formulation & System Context**

---

## Ringkasan Materi

### Problem Formation Model

Masalah riset melewati 5 tahap transformasi. Melompat langsung dari Reality ke Variable adalah kesalahan paling umum.

```
Reality → Observed Issue (Symptom) → Diagnosed Problem (Root Cause)
→ Researchable Problem (Scoped) → Measurable Variable (Operationalized)
```

### Topic ≠ Problem ≠ Research Problem

| Level | Contoh | Status |
|-------|--------|--------|
| **Topik** | Keamanan IoT | Terlalu luas, tidak bisa diuji |
| **Problem** | MQTT tidak terenkripsi | Spesifik tapi belum riset |
| **Research Problem** | Belum ada studi membandingkan overhead TLS 1.3 vs DTLS pada MQTT di IoT RAM < 64KB | Bisa dirancang eksperimennya |

### Symptom vs Root Cause

Apa yang diamati (gejala) ≠ mengapa terjadi (akar masalah). Gunakan **5 Whys** atau **Fishbone Diagram** untuk menggali.

Contoh: "User meninggalkan checkout" (symptom) → "Waktu loading > 8 detik karena API call sequential" (root cause).

### System Thinking

Setiap masalah riset TI harus terikat pada komponen sistem: **Input → Process → Output → Outcome → Constraints → Stakeholders**.

### Problem Quality Check

Masalah riset yang layak harus memenuhi 5 kriteria:
- **Clarity** — Satu orang membaca akan paham
- **Measurability** — Ada metrik kuantitatif
- **Relevance** — Penting untuk domain
- **Testability** — Bisa gagal (falsifiable)
- **Impact** — Ada kontribusi jika terjawab

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Menyelesaikan masalah (*solve*) | Memahami dan membuktikan (*understand & prove*) |
| Masalah | Bug, error, fitur belum ada | Gap dalam pengetahuan |
| Scope | Selesaikan semua yang perlu | Batasi agar bisa dibuktikan |
| Output | Working system | Evidence, paper, replicable findings |

### Istilah Penting

- **Problem Statement** — Formulasi tertulis: konteks sistem + gap + dampak + justifikasi
- **System Context** — Deskripsi lengkap: input, proses, output, outcome, constraints, stakeholders
- **Problem Drift** — Masalah "bermutasi" dari pendahuluan ke metodologi karena statement awal tidak presisi
- **Solution-First Thinking** — Memulai dari solusi tanpa masalah yang jelas — berbahaya dalam riset
- **Operational Definition** — Definisi variabel yang cukup jelas agar peneliti lain bisa mengukur hal yang sama

---

## Template A.2 — Problem Statement Builder

```
PROBLEM STATEMENT BUILDER

Domain & Konteks
  Domain   : Smart Agriculture / Pertanian Hidroponik Berbasis IoT
  Konteks  : Pertanian hidroponik di wilayah dengan keterbatasan akses listrik konvensional dan kebutuhan efisiensi energi yang tinggi.

System Context
  Input       : Data lingkungan real-time (suhu, kelembaban, intensitas cahaya) dari sensor + energi dari panel surya.
  Process     : Pemrosesan data oleh mikrokontroler (Arduino/ESP), pengambilan keputusan otomatis, dan kontrol aktuator (pompa, kipas, lampu LED).
  Output      : Pengendalian lingkungan tanaman yang presisi dan operasional sistem yang sepenuhnya bergantung pada energi terbarukan.
  Outcome     : Peningkatan efisiensi energi, pengurangan biaya operasional, dan produktivitas hidroponik yang lebih berkelanjutan.
  Constraints : Keterbatasan kapasitas baterai, fluktuasi intensitas matahari, skalabilitas prototipe, dan biaya komponen awal.
  Stakeholders: Petani hidroponik (khususnya di daerah terpencil), peneliti pertanian cerdas, pemerintah/program ketahanan pangan, dan pengembang teknologi IoT.

Fenomena → Problem
  Fenomena yang diamati             : Tingginya ketergantungan hidroponik konvensional pada listrik PLN dan pemantauan manual yang intensif.
  Gejala (symptom) yang terukur     : Tingginya ketergantungan hidroponik konvensional pada listrik PLN dan pemantauan manual yang intensif.
  Masalah yang didiagnosis          : Kurangnya sistem hidroponik yang terintegrasi secara holistik antara IoT otomasi dan energi terbarukan (solar) yang mandiri dan stabil.
  Masalah riset (researchable)      : Belum optimalnya desain integrasi IoT dengan panel surya pada skala prototipe untuk mencapai kestabilan operasional 24 jam penuh dengan efisiensi energi yang tinggi di kondisi lingkungan nyata.
  Variabel yang terukur             : Efisiensi penggunaan energi (%), kestabilan sistem (jam operasional tanpa gangguan), konsumsi energi harian vs energi yang dihasilkan, serta akurasi kontrol lingkungan (suhu & kelembaban).

Problem Quality Check
  [v] Clarity — Apakah satu orang membaca akan paham?
  [v] Measurability — Apakah ada metrik kuantitatif?
  [v] Relevance — Apakah penting untuk domain?
  [v] Testability — Apakah bisa gagal?
  [v] Impact — Apakah ada kontribusi jika terjawab?

Problem Statement (1 paragraf):
  Di tengah meningkatnya kebutuhan pangan dan tantangan perubahan iklim, pertanian hidroponik menawarkan solusi efisien penggunaan air dan lahan. Namun, sistem hidroponik konvensional masih menghadapi masalah utama berupa biaya energi yang tinggi dan ketergantungan pada infrastruktur listrik yang tidak selalu tersedia, terutama di daerah terpencil. Meskipun telah banyak penelitian terpisah tentang IoT dan energi surya, masih terdapat gap dalam integrasi holistik yang menghasilkan sistem otomasi hidroponik cerdas yang benar-benar mandiri energi, stabil 24 jam, serta memiliki efisiensi energi yang terukur dan dapat direplikasi. Penelitian ini bertujuan untuk mengatasi masalah tersebut melalui pengembangan dan evaluasi prototipe sistem IoT berbasis panel surya, sehingga diharapkan dapat memberikan kontribusi pada pertanian berkelanjutan yang lebih inklusif dan ramah lingkungan.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Integrasi IoT dan Energi Terbarukan pada Pertanian Hidroponik

| Tahap | Hasil |
|-------|-------|
| Reality | Banyak petani hidroponik di daerah terpencil kesulitan mengoperasikan sistem karena pasokan listrik tidak stabil dan biaya energi mahal. |
| Observed Issue (Symptom) | Sistem hidroponik sering mati atau memerlukan genset/listrik konvensional, sehingga efisiensi rendah dan biaya operasional tinggi. |
| Diagnosed Problem (Root Cause) | Kurangnya integrasi yang matang antara otomasi IoT dengan sumber energi terbarukan yang andal dan murah. |
| Researchable Problem | Belum ada desain prototipe yang teruji secara komprehensif mengenai performa integrasi IoT + panel surya untuk mencapai kestabilan operasional penuh dengan efisiensi energi optimal. |
| Measurable Variable | Efisiensi energi (%), waktu operasional mandiri (jam/hari), akurasi sensor, dan konsumsi daya vs energi yang dihasilkan. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data sensor lingkungan (DHT22), intensitas cahaya, dan input energi dari panel surya. |
| Process | Pemrosesan data oleh mikrokontroler, logika otomatisasi, dan pengendalian aktuator. |
| Output | Tindakan otomatis (penyiraman, pencahayaan, ventilasi) + data monitoring real-time via aplikasi IoT. |
| Outcome | Pertumbuhan tanaman optimal + operasional sistem 100% dari energi terbarukan. |
| Constraints | Fluktuasi cuaca, kapasitas baterai terbatas, biaya komponen, dan skalabilitas. |
| Stakeholders | Petani kecil, peneliti pertanian, dan komunitas daerah terpencil. |

**Komponen mana yang paling relevan dengan masalah riset?** Process dan Constraints (khususnya integrasi energi dan kestabilan sistem).

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Problem statement sudah spesifik dan mudah dipahami. |
| Measurability | 4 | Sudah ada metrik (efisiensi energi, operasional 24 jam), tapi masih bisa ditambah metrik pertumbuhan tanaman. |
| Relevance | 5 | Sangat relevan dengan isu ketahanan pangan dan energi terbarukan di Indonesia. |
| Testability | 4 | Dapat diuji melalui prototipe, namun dipengaruhi variabel cuaca yang sulit dikendalikan sepenuhnya. |
| Impact | 5 | Memberikan solusi praktis bagi petani di daerah terpencil. |

**Skor total:** 23 / 25

**Problem statement versi final (1 paragraf):**
> Di tengah meningkatnya kebutuhan pangan dan tantangan perubahan iklim, pertanian hidroponik menawarkan solusi efisien penggunaan air dan lahan. Namun, sistem hidroponik konvensional masih menghadapi masalah utama berupa biaya energi yang tinggi dan ketergantungan pada infrastruktur listrik yang tidak selalu tersedia, terutama di daerah terpencil. Meskipun telah banyak penelitian terpisah tentang IoT dan energi surya, masih terdapat gap dalam integrasi holistik yang menghasilkan sistem otomasi hidroponik cerdas yang benar-benar mandiri energi, stabil 24 jam, serta memiliki efisiensi energi yang terukur dan dapat direplikasi. Penelitian ini bertujuan untuk mengatasi masalah tersebut melalui pengembangan dan evaluasi prototipe sistem IoT berbasis panel surya, sehingga diharapkan dapat memberikan kontribusi pada pertanian berkelanjutan yang lebih inklusif dan ramah lingkungan.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah saat coding (bug/error) biasanya bersifat konkret, langsung terlihat, dan solusinya lebih teknis — kita tinggal debug, cari penyebab, lalu perbaiki. Sedangkan masalah riset jauh lebih abstrak dan membutuhkan pendekatan yang lebih dalam. Kita harus membedakan antara gejala (symptom) dengan akar masalah (root cause), membatasi scope agar testable, serta memastikan masalah tersebut bermakna dan berkontribusi pada pengetahuan.
> Perbedaan fundamentalnya adalah: saat coding kita berorientasi membuat sesuatu jadi jalan, sedangkan dalam riset kita berorientasi memahami mengapa sesuatu terjadi dan membuktikan apakah solusi kita memang lebih baik secara ilmiah. Research mindset menuntut kita lebih sabar, kritis, dan sistematis dalam mendefinisikan masalah sebelum terburu-buru ke solusi.
