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
Tanggal          : 9 Mei 2026

1. Ketika membaca klaim "metode X 95% akurat":
   - Pertanyaan pertama saya: Pada kondisi dan dataset seperti apa? Apakah ada pengukuran yang objektif dan reproducible?
   - Data yang dibutuhkan untuk verifikasi: Detail metodologi (ukuran sampel, durasi pengujian, kondisi lingkungan, metrik evaluasi, baseline perbandingan, dan ketersediaan data mentah atau kode).

2. Posisi paradigma:
   - Pendekatan: [ ] Positivis  [ ] Interpretivis  [X] Design Science  [ ] Mixed
   - Alasan: Topik saya lebih berorientasi pada pembuatan artefak (sistem/prototipe) yang dapat menyelesaikan masalah praktis sekaligus menghasilkan pengetahuan. Saya ingin menguji apakah desain tertentu memang memberikan peningkatan kinerja yang nyata, bukan hanya menguji hipotesis teoretis semata.
3. Identifikasi distorsi:
   - Asumsi tersembunyi:Sering kali kita mengasumsikan bahwa hasil di lingkungan laboratorium atau pengujian terbatas akan langsung berlaku di dunia nyata.
   - Sumber bias potensial: Selektivitas pelaporan (hanya menampilkan hasil terbaik), kurangnya uji jangka panjang, dan generalisasi yang terlalu luas dari sampel kecil.
   - Langkah mitigasi: Selalu melaporkan both kondisi sukses dan gagal, melakukan pengujian di berbagai skenario, dan secara transparan menyebutkan batasan (limitations) sejak awal.

4. Komitmen etika:
   - Data yang tidak akan dimanipulasi:Saya tidak akan menghapus outlier tanpa alasan yang jelas dan dokumentasi yang kuat, serta tidak akan “mempercantik” hasil hanya untuk terlihat lebih impresif.
   - Batasan yang diakui sejak awal: Saya akan secara jujur menyatakan rentang kondisi di mana sistem saya bekerja optimal dan di mana ia masih memiliki kelemahan.
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
| Reality → Data | Observasi masalah petani hidroponik + studi literatur + pengukuran di lapangan terbatas | Sampling hanya di lokasi tertentu (mungkin tidak representatif wilayah lain dengan cuaca berbeda) |
| Data → Processing | Pengolahan data sensor DHT22, konsumsi energi, dll. | Tidak dijelaskan secara rinci teknik preprocessing atau penanganan missing value/noise |
| Processing → Analysis | Perhitungan efisiensi energi, stabilitas sistem | Pengujian hanya selama 4 minggu (2 periode), belum cukup untuk melihat degradasi jangka panjang |
| Analysis → Inference | Menarik kesimpulan bahwa sistem “100% mandiri energi” dan “sangat stabil” | Generalisasi berlebihan dari prototipe skala kecil ke aplikasi komersial |
| Inference → Knowledge | Klaim kontribusi inovatif integrasi IoT + solar + otomasi | Cherry-picking hasil positif; sedikit pembahasan kegagalan atau kondisi buruk (misalnya hari mendung berkepanjangan) |

**Distorsi paling besar di tahap:** Inference → Knowledge

**Dua distorsi spesifik yang teridentifikasi:**
1. Overgeneralization — Hasil pengujian pada prototipe kecil selama 4 minggu langsung diklaim cocok untuk “daerah terpencil dengan akses listrik terbatas” tanpa uji di lokasi yang beragam.
2. Lack of long-term evaluation — Tidak ada data degradasi panel surya, baterai, atau sensor setelah 6–12 bulan penggunaan nyata.
---

## Latihan 2 — Analisis Kasus Etika

Skenario: Seorang peneliti menemukan bahwa jika 3 data point outlier dihapus, hasil eksperimennya menjadi signifikan. Dengan outlier, hasilnya tidak signifikan.

| Perspektif | Analisis |
|------------|---------|
| Kejujuran ilmiah | Harus melaporkan kedua analisis (dengan dan tanpa outlier) serta memberikan justifikasi ilmiah yang kuat jika outlier memang dihapus (bukan sekadar karena “membuat hasil bagus”).|
| Transparansi | Semua keputusan pemrosesan data harus didokumentasikan di bagian metode atau appendix agar orang lain dapat mereplikasi. |
| Peer review | Reviewer akan sangat kritis terhadap penghapusan data. Lebih baik jujur daripada risikonya dicurigai p-hacking atau HARKing. |

**Keputusan akhir dan justifikasi:**
> Saya akan melaporkan kedua versi hasil (dengan dan tanpa outlier), menjelaskan alasan ilmiah penghapusan (jika ada), dan menyertakannya sebagai analisis sensitivitas. Kejujuran jauh lebih berharga daripada signifikansi statistik yang “dipaksakan”. Negative result atau hasil yang “kurang sempurna” juga merupakan kontribusi ilmiah yang berharga.
---

## Latihan 3 — Posisi Paradigma

**Topik riset:** Integrasi IoT dan Energi Terbarukan pada Sistem Hidroponik Cerdas

> **Skala 1–5:** 1 = tidak sesuai sama sekali dengan topik ini, 5 = sangat sesuai dan dominan digunakan pada riset bertopik serupa.

| Kriteria | Positivis | Interpretivis | Design Science |
|----------|-----------|---------------|----------------|
| Kesesuaian dengan topik (1–5) | 4 | 2 | 5 |
| Jenis data yang dikumpulkan | Metrik numerik, log eksperimen | Wawancara, observasi kualitatif | Hasil uji artefak, komparasi kinerja |
| Limitasi paradigma | Kurang menangkap aspek kontekstual pengguna nyata | Sulit mengukur improvement yang konkret | Sulit mengklaim generalisasi luas tanpa banyak iterasi |

**Paradigma yang dipilih:** Design Science Research
**Alasan:** Topik ini sangat cocok dengan DSR karena tujuannya adalah membangun dan mengevaluasi artefak (prototipe sistem) untuk memecahkan masalah praktis sekaligus menghasilkan pengetahuan desain (design principles) yang dapat digunakan oleh peneliti lain.

---

## Refleksi

> Sebelum membaca materi ini, apakah pernah mempertanyakan klaim "95% akurat"? Setelah memahami rantai distorsi, pertanyaan apa yang sekarang akan diajukan saat membaca paper?

**Jawaban:**
> Kini, saya akan mempertanyakan: “95% akurat dibandingkan apa? Apa baseline-nya dan apakah baseline tersebut sudah fair? ,Pada dataset dan kondisi lingkungan seperti apa klaim ini diuji? Apakah hanya di lingkungan ideal/laboratorium?, Berapa ukuran sampelnya? Berapa lama pengujian dilakukan? Apakah ada pengujian jangka panjang?, Apa saja batasan (limitations) yang diakui penulis? Apakah ada potensi confounding variable atau bias sampling?, Apakah hasil negatif atau kegagalan juga dilaporkan, atau hanya sisi positif yang ditonjolkan?.
Saya sekarang sadar bahwa klaim angka yang impresif harus selalu disertai bukti yang transparan dan reproducible. Pemahaman ini membantu saya tidak hanya menjadi konsumen ilmu yang lebih baik, tetapi juga calon peneliti yang lebih jujur dan teliti.
