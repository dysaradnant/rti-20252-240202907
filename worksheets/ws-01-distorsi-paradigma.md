# WS-01: Distorsi & Paradigma

> **Bab 1 — Research Mindset in IT**

---

## Ringkasan Materi

### Research Trust Model

Pengetahuan ilmiah tidak muncul langsung dari kenyataan. Ia melewati **6 tahap transformasi** yang masing-masing rawan distorsi:

```
Reality → Data → Processing → Analysis → Inference → Knowledge
```

Etika mencegah distorsi yang disengaja (fabrikasi, cherry-picking). Validitas mendeteksi distorsi yang tidak disengaja (confounding variable, sampling bias).

### Tiga Jenis Validitas

| Jenis | Pertanyaan | Contoh Ancaman |
|-------|-----------|----------------|
| **Internal Validity** | Apakah hubungan kausal benar ada? | Confounding variable |
| **External Validity** | Apakah bisa digeneralisasi? | Dataset terlalu homogen |
| **Construct Validity** | Apakah mengukur hal yang benar? | Metrik tidak sesuai klaim |

### Paradigma Riset

Mata kuliah ini menggunakan pendekatan **Positivist** (fenomena TI bisa diukur objektif melalui eksperimen terkontrol) diperkuat **Design Science Research** (DSR). Penting untuk membedakan keduanya:

| Paradigma | Cara Kerja | Contoh di TI |
|-----------|-----------|---------------|
| **Positivis** | Uji hipotesis dengan eksperimen terkontrol | Apakah CNN lebih akurat dari RF pada dataset X? |
| **Design Science Research** | Bangun artefak (sistem/model/framework) untuk menguji proposisi | Dapatkah arsitektur hybrid CNN+LSTM membuktikan peningkatan recall ≥5%? |
| **Interpretivis** | Pahami makna melalui konteks & kualitatif | Bagaimana peneliti manafsirkan anomali data sensor IoT? |

Dalam DSR, artefak **bukan tujuan akhir** — ia adalah instrumen untuk menghasilkan pengetahuan. Pertanyaan riset tetap harus difalsifikasi.

### Mode Berpikir Peneliti

**Curious** (mempertanyakan fenomena) → **Critical** (mengevaluasi klaim berdasarkan bukti) → **Systematic** (merancang investigasi terstruktur dan reproducible).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan | Membuat sistem yang bekerja | Menghasilkan pengetahuan yang valid |
| Pertanyaan khas | "Bagaimana membuatnya jalan?" | "Apakah klaim ini benar?" |
| Ukuran sukses | Sistem berfungsi, client puas | Hipotesis terjawab, temuan tervalidasi |
| Kegagalan | Harus dihindari | Harus dilaporkan (negative result = kontribusi) |

### Istilah Penting

- **Research Mindset** — Pola pikir yang menuntut bukti dan mempertanyakan asumsi
- **Research Ethics** — Prinsip perilaku: kejujuran, objektivitas, keterbukaan, akuntabilitas
- **HARKing** — Hypothesizing After Results are Known — merumuskan hipotesis setelah melihat data
- **Falsifiability** — Hipotesis harus bisa dibuktikan salah

---

## Template A.1 — Research Mindset Self-Assessment

```
Nama Peneliti    : Dysar Adnant Ilham Nur Asnawi
Tanggal          : 21 April 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Bagaimana distribusi dan ukuran dataset yang digunakan, apakah mencakup skenario ekstrem, serta metode evaluasi apa yang dipakai untuk menghasilkan akurasi 95%?
   - Data yang dibutuhkan untuk verifikasi: Confusion matrix, precision, recall, F1-score, spesifikasi sensor, serta log data mentah sebelum preprocessing

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [X] Design Science  [ ] Mixed
   - Alasan: Riset ini menggunakan pendekatan Design Science karena berfokus pada pembangunan dan evaluasi artefak berupa sistem otomasi hidroponik berbasis IoT untuk menyelesaikan masalah efisiensi pertanian secara       praktis.
3. Identifikasi distorsi:
   - Asumsi tersembunyi: Sistem dianggap akan selalu mendapatkan paparan sinar matahari yang konstan untuk panel surya dan tidak mempertimbangkan variabilitas cuaca ekstrem dalam jangka panjang
   - Sumber bias potensial: Penempatan sensor suhu yang mungkin terlalu dekat dengan komponen elektronik yang panas, dan bias dataset (misalnya hanya diuji di satu lokasi)
   - Langkah mitigasi: Melakukan kalibrasi sensor secara berkala dengan alat ukur standar industri dan menggunakan teknik shielding pada sensor dan melakukan pengujian di berbagai kondisi lingkungan.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi: Log waktu respons (latensi) pengiriman data dari sensor ke dashboard dan pembacaan asli parameter lingkungan, hasil pengujian yang gagal juga dilaporkan
   - Batasan yang diakui sejak awal: Keterbatasan generalisasi sistem yaitu kapasitas baterai pada panel surya yang mungkin mempengaruhi stabilitas sistem saat cuaca mendung berkepanjangan.
```

---

## Latihan 1 — Identifikasi Distorsi

Pilih satu paper riset di bidang TI yang mengklaim "metode X meningkatkan performa." Telusuri setiap tahap Research Trust Model.

> **Panduan pencarian paper:** Gunakan [IEEE Xplore](https://ieeexplore.ieee.org), [ACM Digital Library](https://dl.acm.org), atau Google Scholar. Pilih paper **tahun 2020 ke atas**, di topik yang Anda minati: deteksi anomali, klasifikasi citra, NLP, keamanan siber, IoT, dsb.
>
> **Contoh domain TI:** "Deteksi anomali lalu-lintas jaringan menggunakan CNN — akurasi meningkat 94% vs baseline SVM 87%." Distorsi potensial: apakah dataset normal/anomali seimbang? Apakah hanya diuji pada satu vendor traffic?

**Paper yang dipilih:**
> Judul: Desain dan Prototipe Integrasi IoT dalam Pertanian Hidroponik Cerdas Berbasis Energi Terbarukan
> Penulis (Tahun): Agus Salim Wardhana, Muhammad Ferdiansyah, Siti Kholifah K (2025)
> Sumber/Link DOI: https://journal.stmiki.ac.id/index.php/jimik/article/view/1134

| Tahap | Apa yang Dilakukan | Potensi Distorsi |
|-------|-------------------|-----------------|
| Reality → Data | Mengambil data suhu dan kelembapan menggunakan sensor DHT22 pada sistem hidroponik berbasis IoT. | Sensor Accuracy Limitation: Sensor DHT22 memiliki keterbatasan akurasi dan presisi, yang dapat menyebabkan perbedaan antara kondisi nyata dan data yang tercatat. |
| Data → Processing | Data dari sensor dikirim melalui mikrokontroler (Arduino Uno) ke platform IoT untuk monitoring. | Transmission Reliability: Jurnal tidak membahas stabilitas pengiriman data, sehingga ada potensi kehilangan atau keterlambatan data yang tidak terdeteksi. |
| Processing → Analysis | Sistem membandingkan data sensor dengan parameter tertentu untuk mengontrol aktuator seperti pompa dan kipas. | Parameter Rigidity: Penentuan parameter kontrol tidak dijelaskan fleksibilitasnya, sehingga berpotensi tidak optimal jika kondisi lingkungan berubah. |
| Analysis → Inference | Menyimpulkan bahwa sistem mampu berjalan dengan memanfaatkan energi dari panel surya. | Context Limitation: Kesimpulan diambil tanpa pembahasan kondisi cuaca ekstrem atau jangka panjang, sehingga validitasnya terbatas pada kondisi tertentu. |
| Inference → Knowledge | Menyatakan bahwa sistem meningkatkan efisiensi dan dapat mengurangi penggunaan listrik konvensional. | Measurement Validity: Klaim efisiensi tidak didukung oleh metrik kuantitatif yang rinci (misalnya pertumbuhan tanaman atau perbandingan sebelum–sesudah). |

**Distorsi paling besar di tahap:** Inference → Knowledge

**Dua distorsi spesifik yang teridentifikasi:**
1. Measurement Validity Bias: Klaim peningkatan efisiensi tidak didukung dengan indikator kuantitatif yang jelas seperti hasil panen, pertumbuhan tanaman, atau perbandingan performa sebelum dan sesudah sistem diterapkan.
2. Contextual Limitation Bias: Evaluasi sistem energi surya tidak mempertimbangkan variasi kondisi lingkungan seperti cuaca mendung atau musim hujan, sehingga hasil tidak dapat digeneralisasi.
---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Peneliti wajib melaporkan hasil apa adanya. Menghapus outlier hanya untuk mencapai signifikansi statistik termasuk praktik tidak etis (p-hacking). Kedua hasil (dengan dan tanpa outlier) harus disajikan, disertai alasan metodologis jika outlier dipertimbangkan untuk dikeluarkan.|
| Transparansi | Peneliti harus menjelaskan secara terbuka: kriteria identifikasi outlier, metode deteksi (misalnya Z-score atau IQR), serta dampaknya terhadap hasil analisis. Tidak boleh ada data yang dihilangkan tanpa penjelasan eksplisit dalam metode penelitian. |
| Peer review | Reviewer akan mempertanyakan alasan penghapusan outlier. Jika tidak ada justifikasi kuat (misalnya kesalahan pengukuran atau data corrupt), maka tindakan tersebut bisa dianggap manipulasi data. Hal ini berpotensi menyebabkan penolakan paper atau revisi besar. |

**Keputusan akhir dan justifikasi:**
> Outlier tidak boleh dihapus hanya untuk membuat hasil menjadi signifikan. Peneliti harus melaporkan hasil analisis secara lengkap (dengan dan tanpa outlier) serta memberikan justifikasi metodologis yang jelas jika ada data yang dikeluarkan. Keputusan ini menjaga integritas ilmiah, menghindari bias, dan memastikan hasil penelitian dapat dipercaya serta direplikasi.

---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Pengembangan sistem otomasi hidroponik berbasis IoT dengan integrasi panel surya untuk meningkatkan efisiensi

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 — Cocok karena melibatkan pengukuran data sensor (suhu, kelembapan) dan pengujian performa sistem secara kuantitatif | 1 — Tidak fokus pada makna sosial atau interpretasi manusia | 5 — Sangat sesuai karena membangun dan mengevaluasi artefak berupa sistem IoT |
| Jenis data yang dikumpulkan | Data numerik dari sensor, log sistem, performa energi | Data kualitatif seperti wawancara pengguna (tidak dominan di riset ini) | Hasil uji sistem, efisiensi energi, performa aktuator, keberhasilan otomasi |
| Limitasi paradigma | Terbatas pada aspek terukur, kurang menangkap konteks penggunaan di lapangan | Tidak relevan untuk evaluasi sistem teknis berbasis perangkat | Fokus pada artefak, sehingga terkadang kurang mendalam dalam analisis teoritis atau generalisasi luas |

**Paradigma yang dipilih:** Design Science
**Alasan:** Pendekatan Design Science dipilih karena penelitian ini berfokus pada perancangan, implementasi, dan evaluasi artefak berupa sistem otomasi hidroponik berbasis IoT. Tujuan utama bukan hanya memahami fenomena, tetapi memberikan solusi praktis terhadap masalah efisiensi pertanian dengan memanfaatkan teknologi dan energi terbarukan. Evaluasi dilakukan melalui performa sistem yang dibangun, sehingga paradigma ini paling dominan dan relevan.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Kini, saya akan mempertanyakan: bagaimana kualitas dan distribusi data yang digunakan, apakah terdapat bias atau outlier yang mempengaruhi hasil, metode evaluasi apa yang dipakai (misalnya confusion matrix, precision, recall), serta apakah klaim tersebut didukung oleh pengujian yang cukup dan dapat digeneralisasi. Selain itu, saya juga akan melihat apakah ada keterbatasan yang diakui peneliti dan apakah hasil penelitian transparan serta dapat direplikasi.
