# WS-16: Presentation & Defense (UAS)

> **Bab 16 — Presentasi & Pertahanan Ilmiah**

---

## Ringkasan Materi

### Scientific Defense Model

```
Research Work → Presentation → Questioning → Defense → Evaluation → Acceptance
```

### Presentasi ≠ Ringkasan Paper

| Paper | Presentasi |
|-------|-----------|
| Dibaca (self-paced) | Didengar (presenter-paced) |
| Detail lengkap | Ide kunci + highlight |
| Tabel numerik detail | Grafik visual + angka kunci |
| Pembaca bisa re-read | Audiens dengar sekali |

**Prinsip:** Presentasi membutuhkan **reformulasi**, bukan kompresi. Medium berbeda = pendekatan berbeda.

### Claim-Evidence-Reasoning (CER)

Setiap jawaban defense harus memiliki:
1. **Claim** — Pernyataan yang dijawab
2. **Evidence** — Data/fakta pendukung
3. **Reasoning** — Logika yang menghubungkan evidence ke claim

**Contoh:**
| Pertanyaan | Bad Answer | Good Answer (CER) |
|-----------|-----------|-------------------|
| "Kenapa hanya 3 dataset?" | "Tiga sudah cukup" | "3 dataset mewakili variasi: small-clean, medium-clean, medium-noisy [E]. Generalisasi perlu validasi lanjut — listed as limitation [R]" |
| "Hasil DS-3 menurun?" | "Itu outlier" | "Ya, karena distribusi heavy-tail melanggar asumsi Gaussian [E]. Ini menunjukkan boundary condition metode [R]" |
| "Effect size?" | "p=0.003, jadi signifikan" | "Cohen's d=1.2 (large effect) [E] — bukan hanya signifikan tapi substansial [R]" |

### Slide Design — One Slide, One Message

**Optimal 9-Slide Plan (15 menit):**

| # | Slide | Waktu | Pesan |
|---|-------|-------|-------|
| 1 | Title + context | 1 min | Apa ini tentang apa |
| 2 | Problem + motivation | 2 min | Mengapa penting |
| 3 | Gap + RQ | 1.5 min | Apa yang belum terjawab |
| 4 | Method overview | 2 min | Bagaimana dijawab (diagram) |
| 5 | Key result — tabel | 2 min | Temuan utama |
| 6 | Key result — grafik | 2 min | Pola visual |
| 7 | Interpretation + failure | 2 min | Apa artinya |
| 8 | Limitation + future | 1.5 min | Batasan & arah |
| 9 | Conclusion + contribution | 1 min | Closing message |

### Anticipatory Defense

Prediksi pertanyaan berdasarkan kategori:

| Kategori | Contoh Pertanyaan |
|---------|------------------|
| Problem | "Mengapa masalah ini penting?" |
| Gap | "Bagaimana dengan studi X yang sudah menjawab ini?" |
| Method | "Mengapa metode ini, bukan Y?" |
| Results | "Bagaimana menjelaskan anomali di DS-3?" |
| Generalization | "Apakah bisa diterapkan di domain lain?" |

### Tiga Prinsip Jawaban

1. **Direct** — Jawab dulu, elaborasi kemudian
2. **Data-based** — Tunjuk evidence spesifik
3. **Honest** — Akui limitasi jika memang ada

### Jebakan Kognitif

1. "Presentasi = semua yang ada di paper" → terlalu padat
2. "Slide cantik = presentasi bagus" → konten > estetika
3. "Tidak bisa jawab = gagal" → "I don't know, but..." menunjukkan kejujuran
4. "Tidak perlu latihan — saya paham riset saya" → latihan = menemukan celah

---

## Template A.16 — Defense Preparation Sheet

```
DEFENSE PREPARATION

Slide Deck Plan:
  Total slides   : 11 slide
  Time per slide : ±1,5 menit
  Total time     : ±15 menit

Slide Outline:
| # | Pesan Utama | Visual | Waktu |
|---|-------------|--------|-------|
| 1 | Judul penelitian dan identitas peneliti | Cover + ilustrasi hidroponik IoT | 1 menit |
| 2 | Latar belakang dan motivasi penelitian | Diagram permasalahan energi hidroponik | 2 menit |
| 3 | Research Gap, Research Question, dan Tujuan Penelitian | Tabel gap penelitian dan RQ | 1,5 menit |
| 4 | Metodologi Penelitian | TDiagram alur penelitian (NASA POWER → PV Model → Battery → Scheduler) | 2 menit |
| 5 | Dataset dan Setup Eksperimen | Diagram dataset NASA POWER dan konfigurasi sistem | 1,5 menit |
| 6 | Hasil Eksperimen | Tabel Rule-Based vs Adaptive Scheduler | 2 menit |
| 7 | Grafik Hasil | Grafik perbandingan efisiensi dan SOC | 2 menit |
| 8 | Analisis dan Pembahasan | Diagram interpretasi hasil dan limitation | 1,5 menit |
| 9 | Kontribusi Penelitian | Diagram kontribusi ilmiah dan praktis | 1 menit |
| 10 | Kesimpulan | Ringkasan jawaban Research Question | 1 menit |
| 11 | Terima Kasih & Sesi Tanya Jawab | Slide "Questions?" | 0,5 menit |

Anticipatory Defense Matrix

| Kategori | Pertanyaan Potensial | Jawaban (CER) |
|----------|----------------------|---------------|
| Problem | Mengapa penelitian ini penting untuk dilakukan? | **Claim:** Sistem hidroponik cerdas membutuhkan pasokan energi yang stabil agar pompa, sensor, dan aktuator dapat beroperasi secara berkelanjutan. **Evidence:** Pada daerah terpencil, suplai listrik PLN tidak selalu tersedia sehingga penggunaan panel surya menjadi alternatif, namun produksi energi bersifat fluktuatif. **Reasoning:** Oleh karena itu diperlukan Adaptive Energy Scheduler agar penggunaan energi dapat diatur sesuai kondisi energi yang tersedia sehingga efisiensi sistem meningkat. |
| Gap | Apa perbedaan penelitian Anda dengan penelitian sebelumnya? | **Claim:** Penelitian sebelumnya lebih banyak menggunakan kontrol berbasis aturan tetap (Rule-Based). **Evidence:** Berdasarkan kajian literatur, belum banyak penelitian yang mengintegrasikan PV Model, Battery Model, Energy Demand Model, dan Adaptive Scheduler dalam satu sistem simulasi menggunakan dataset NASA POWER. **Reasoning:** Penelitian ini mengisi gap tersebut dengan membangun model simulasi energi yang lebih terintegrasi. |
| Method | Mengapa menggunakan dataset NASA POWER dibanding data sensor langsung? | **Claim:** NASA POWER dipilih karena menyediakan data historis yang lengkap dan dapat diakses secara terbuka. **Evidence:** Dataset yang digunakan mencakup 8784 data selama tahun 2024 dengan parameter radiasi matahari, suhu, kelembapan, dan kecepatan angin. **Reasoning:** Dataset tersebut memungkinkan eksperimen dilakukan secara konsisten dan dapat direproduksi tanpa harus melakukan pengukuran lapangan selama satu tahun penuh. |
| Results | Mengapa peningkatan efisiensi hanya sebesar 1,79%? | **Claim:** Adaptive Scheduler sudah menunjukkan peningkatan dibanding Rule-Based Scheduler, tetapi peningkatannya masih terbatas. **Evidence:** Hasil eksperimen menunjukkan Rule-Based Scheduler memiliki efisiensi rata-rata 40,40%, sedangkan Adaptive Scheduler mencapai 42,19% sehingga terjadi peningkatan sebesar 1,79%. **Reasoning:** Hal ini disebabkan algoritma yang digunakan masih berupa baseline sehingga penelitian lanjutan dapat meningkatkan performa menggunakan metode seperti Fuzzy Logic, Reinforcement Learning, atau Model Predictive Control. |
| Generalization | Apakah metode ini dapat diterapkan pada bidang lain? | **Claim:** Ya, konsep Adaptive Energy Scheduler bersifat umum dan tidak terbatas pada sistem hidroponik. **Evidence:** Model hanya memanfaatkan data produksi energi, kondisi baterai, dan kebutuhan beban sebagai dasar pengambilan keputusan. **Reasoning:** Dengan penyesuaian parameter, metode ini dapat diterapkan pada smart greenhouse, smart irrigation, microgrid, maupun sistem IoT berbasis energi terbarukan lainnya. |

Latihan:
Latihan 1: 15 Juli 2026
Catatan timing & feedback:
- Durasi presentasi: 15 menit.
- Penyampaian materi sesuai alokasi waktu.
- Perlu memperjelas penjelasan mengenai Adaptive Scheduler dan kontribusi penelitian.

Latihan 2: 17 Juli 2026
Catatan timing & feedback:
- Durasi presentasi: 14 menit 30 detik.
- Transisi antar slide lebih baik.
- Perlu meningkatkan kontak mata dan mengurangi membaca slide.

Latihan 3: 19 Juli 2026
Catatan timing & feedback:
- Durasi presentasi: 15 menit.
- Jawaban terhadap pertanyaan penguji lebih sistematis menggunakan pendekatan Claim–Evidence–Reasoning (CER).
- Perlu menyiapkan jawaban yang lebih kuat mengenai alasan peningkatan efisiensi yang masih sebesar 1,79% dibanding target awal penelitian.
```

---

## Latihan 1 — Slide Outline

Rencanakan presentasi 15 menit untuk riset Anda.

| # | Pesan Utama | Visual yang Digunakan | Waktu |
|---|-------------|----------------------|-------|
| 1 | Judul penelitian dan konteks hidroponik cerdas | Cover, logo universitas, gambar hidroponik berbasis IoT | 1 menit |
| 2 | Permasalahan penelitian | Diagram ketergantungan listrik PLN dan fluktuasi energi surya | 2 menit |
| 3 | Research Gap dan Research Question | Tabel literature mapping dan gap penelitian | 1,5 menit |
| 4 | Metodologi penelitian | Flowchart Design Science Research dan alur sistem | 2 menit |
| 5 | Dataset dan preprocessing | Diagram NASA POWER, preprocessing, PV Model | 1,5 menit |
| 6 | Hasil eksperimen | Tabel Rule-Based vs Adaptive Scheduler | 2 menit |
| 7 | Analisis hasil | Grafik efisiensi dan SOC | 2 menit |
| 8 | Keterbatasan dan penelitian selanjutnya | Diagram limitation dan future work | 1,5 menit |
| 9 | Kesimpulan | Ringkasan kontribusi penelitian | 1,5 menit |

**Total waktu estimasi:** 15 menit

---

## Latihan 2 — Anticipatory Defense

Prediksi 5 pertanyaan yang mungkin diajukan penguji, lalu siapkan jawaban CER.

| # | Kategori | Pertanyaan | Claim | Evidence | Reasoning |
|---|----------|-----------|-------|----------|-----------|
| 1 | Problem | Mengapa penelitian ini penting untuk dilakukan? | Sistem hidroponik cerdas memerlukan pengelolaan energi yang efisien agar dapat beroperasi secara berkelanjutan. | Sistem hidroponik bergantung pada pompa, sensor, dan aktuator yang membutuhkan pasokan listrik stabil, sedangkan produksi energi panel surya bersifat fluktuatif. | Adaptive Energy Scheduler dikembangkan agar penggunaan energi dapat menyesuaikan kondisi energi yang tersedia sehingga efisiensi sistem meningkat dan operasional tetap stabil. |
| 2 | Method | Mengapa menggunakan dataset NASA POWER, bukan data sensor secara langsung? | NASA POWER menyediakan data historis yang lengkap, terbuka, dan dapat direproduksi. | Penelitian menggunakan dataset NASA POWER tahun 2024 sebanyak 8784 data yang mencakup radiasi matahari, suhu, kelembapan, dan kecepatan angin. | Dataset tersebut memungkinkan simulasi dilakukan secara konsisten tanpa harus melakukan pengukuran lapangan selama satu tahun, sehingga penelitian lebih efisien dan mudah direplikasi. |
| 3 | Method | Mengapa menggunakan Adaptive Scheduler dibandingkan Rule-Based Scheduler? | Adaptive Scheduler mampu mengambil keputusan berdasarkan beberapa kondisi sistem secara bersamaan. | Scheduler memanfaatkan informasi Solar Radiation, State of Charge (SOC), Temperature, dan Load untuk menentukan strategi pengelolaan energi. | Berbeda dengan Rule-Based yang menggunakan aturan tetap, Adaptive Scheduler lebih fleksibel dalam menyesuaikan keputusan terhadap perubahan kondisi lingkungan dan energi. |
| 4 | Results | Mengapa peningkatan efisiensi hanya sebesar 1,79%? | Adaptive Scheduler sudah memberikan peningkatan dibanding Rule-Based, namun algoritma yang digunakan masih merupakan model dasar. | Hasil eksperimen menunjukkan Rule-Based Scheduler memperoleh efisiensi rata-rata 40,40%, sedangkan Adaptive Scheduler memperoleh 42,19%, sehingga terjadi peningkatan rata-rata 1,79%. | Peningkatan yang belum besar disebabkan scheduler masih menggunakan pendekatan berbasis skor sederhana dan belum menerapkan optimasi lanjutan seperti Fuzzy Logic, Reinforcement Learning, atau Model Predictive Control. Hal ini menjadi keterbatasan sekaligus peluang pengembangan penelitian berikutnya. |
| 5 | Generalization | Apakah metode ini dapat diterapkan pada sistem selain hidroponik? |Ya, konsep Adaptive Energy Scheduler bersifat umum dan dapat diterapkan pada berbagai sistem energi terbarukan.  | Model hanya memerlukan data produksi energi, kapasitas baterai, dan kebutuhan beban sebagai dasar pengambilan keputusan. | Dengan penyesuaian parameter dan karakteristik beban, metode ini dapat diterapkan pada smart greenhouse, smart irrigation, microgrid, smart building, maupun sistem IoT berbasis energi terbarukan lainnya. |

---

## Latihan 3 — Simulasi Q&A

Minta teman/kolega mengajukan 3 pertanyaan tentang riset Anda. Catat pertanyaan dan evaluasi jawaban Anda.

| # | Pertanyaan | Jawaban Saya | Evaluasi |
|---|-----------|-------------|---------|
| 1 | Mengapa menggunakan NASA POWER dibandingkan data sensor langsung? |Karena NASA POWER menyediakan data historis yang lengkap dan konsisten sehingga cocok untuk simulasi penelitian. | [✓] Direct [✓] Data-based [✓] Honest |
| 2 | Mengapa hanya lima kali eksperimen? | Lima kali eksperimen dilakukan sebagai validasi awal sesuai ruang lingkup penelitian. Penelitian lanjutan dapat menambah jumlah eksperimen untuk meningkatkan kekuatan statistik. | [✓] Direct [✓] Data-based [✓] Honest |
| 3 | Apa kontribusi utama penelitian? | Kontribusi utama adalah pengembangan desain Adaptive Energy Scheduler yang mengintegrasikan PV Model, Battery Model, dan Energy Demand Model pada sistem hidroponik cerdas. | [✓] Direct [✓] Data-based [✓] Honest |

**Pertanyaan yang paling sulit dijawab:**
> Mengapa peningkatan efisiensi hanya sebesar 1,79%, sedangkan pada proposal penelitian ditargetkan minimal 8%?

**Apa yang perlu disiapkan lebih baik:**
> Peningkatan sebesar 1,79% merupakan hasil dari implementasi versi awal Adaptive Scheduler dengan mekanisme pengambilan keputusan berbasis skor sederhana. Target 8% pada proposal adalah target penelitian yang ingin dicapai. Hasil saat ini menunjukkan metode yang dikembangkan sudah memberikan peningkatan dibandingkan baseline, tetapi belum mencapai target yang diharapkan. Hal ini menjadi salah satu keterbatasan penelitian dan sekaligus membuka peluang pengembangan lebih lanjut dengan algoritma yang lebih adaptif, misalnya Fuzzy Logic, Reinforcement Learning, atau Model Predictive Control.
---

## Refleksi

> Dari seluruh proses WS-01 sampai WS-16 — dari paradigma riset hingga presentasi — bagian mana yang paling mengubah cara Anda berpikir tentang riset? Apa satu hal yang akan selalu Anda terapkan di riset berikutnya?
> Selama mengikuti WS-01 sampai WS-16, saya memahami bahwa penelitian bukan hanya menghasilkan program yang dapat berjalan, tetapi juga membangun argumen ilmiah yang didukung oleh data, metode yang dapat direproduksi, serta analisis yang objektif. Proses mulai dari identifikasi masalah, penyusunan proposal, pengembangan model, pelaksanaan eksperimen, validasi data, analisis hasil, hingga penyusunan presentasi telah mengubah cara saya memandang penelitian sebagai proses yang sistematis dan dapat dipertanggungjawabkan.

**Insight terbesar:**
> Penelitian yang baik tidak diukur dari seberapa rumit algoritma yang digunakan, tetapi dari seberapa jelas masalah yang diselesaikan, seberapa valid metode yang diterapkan, serta seberapa kuat bukti yang mendukung kesimpulan penelitian.

**Yang akan selalu diterapkan:**
> Pada penelitian berikutnya saya akan selalu memulai dengan merumuskan research gap dan research question yang jelas, mendokumentasikan seluruh proses eksperimen secara sistematis, serta memastikan setiap kesimpulan yang disampaikan didukung oleh data yang dapat diverifikasi dan direproduksi.
