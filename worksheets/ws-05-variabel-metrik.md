# WS-05: Variabel & Metrik

> **Bab 5 — Metric, Measurement & Data**

---

## Ringkasan Materi

### Measurement Alignment Model

Setiap pengukuran yang valid harus bisa ditelusuri melalui rantai ini tanpa lompatan logis:

```
Problem → Concept → Variable → Metric → Data → Result
```

### Operationalization = Keputusan Desain

Menerjemahkan konsep abstrak menjadi variabel terukur bukan proses mekanis. "Code quality" yang diukur via SonarQube code smells membawa asumsi implisit. Setiap operasionalisasi harus didokumentasikan dan dijustifikasi.

### Empat Tipe Data (NOIR)

| Tipe | Ciri | Contoh | Operasi Valid |
|------|------|--------|---------------|
| **Nominal** | Kategori, tanpa urutan | Jenis algoritma (RF, SVM, CNN) | Modus, chi-square |
| **Ordinal** | Urutan, interval tidak sama | Skala Likert (1-5) | Median, Spearman |
| **Interval** | Jarak bermakna, tanpa nol absolut | Suhu Celsius | Mean, Pearson, t-test |
| **Ratio** | Jarak bermakna + nol absolut | Waktu eksekusi (ms) | Semua operasi |

Tipe data menentukan uji statistik yang valid. Kebanyakan metrik performa TI = ratio; persepsi pengguna = ordinal.

### Kriteria Pemilihan Metrik

- **Representative** — Mewakili konsep yang diteliti
- **Sensitive** — Cukup peka menangkap perbedaan bermakna (hindari ceiling effect)
- **Feasible** — Bisa dikumpulkan dalam batasan waktu dan biaya

### Pre-registration

Metrik harus ditentukan **sebelum** eksperimen. Memilih metrik setelah melihat data = **p-hacking**. Metrik tambahan yang ditemukan kemudian dilaporkan sebagai *exploratory*, bukan *confirmatory*.

### Primary vs Secondary Metric

- **Primary Metric** — Langsung terikat ke hipotesis, menentukan kesimpulan
- **Secondary Metric** — Pendukung, dilaporkan di samping primary; statusnya suplementer

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Pemilihan metrik | Berdasarkan kebiasaan/tool yang ada | Berdasarkan construct validity |
| Anomali | Dihapus untuk laporan bersih | Diinvestigasi — bisa jadi temuan |
| Kapan dipilih | Setelah sistem jadi (monitoring) | Sebelum eksperimen (by design) |

### Istilah Penting

- **Operationalization** — Transformasi konsep abstrak menjadi variabel terukur
- **Construct Validity** — Sejauh mana pengukuran benar-benar mengukur konsep yang dimaksud
- **Measurement Scale** — Klasifikasi data (NOIR) yang menentukan analisis valid
- **Multi-metric Evaluation** — Menggunakan beberapa metrik untuk menangkap konsep kompleks

---

## Template A.5 — Definisi Variabel, Metrik & Justifikasi

```
VARIABLE & METRIC DEFINITION

Research Question: Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem (waktu operasi 24 jam tanpa gangguan) dibandingkan dengan baseline sistem IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil dengan variasi intensitas cahaya matahari?

| Variabel | Tipe | Konsep | Metrik | Skala | Satuan | Cara Mengukur | Justifikasi |
|----------|------|--------|--------|-------|--------|---------------|-------------|
| Desain Sistem | IV | Jenis arsitektur & integrasi sistem | Kategori sistem (Holistic IoT-Solar Design vs Baseline) | Nominal | - | Implementasi dua prototipe secara paralel | Variabel utama yang dimanipulasi untuk melihat pengaruh terhadap performa |
| Efisiensi Penggunaan Energi | DV | Kemampuan sistem memanfaatkan energi terbarukan secara optimal | (Energi dihasilkan panel surya – Energi dikonsumsi sistem) / Energi dihasilkan × 100% | Ratio | % | Multimeter + data logger setiap jam selama pengujian | Metrik primer yang langsung mengukur tujuan keberlanjutan energi |
| Kestabilan Operasional | DV | Keandalan sistem dalam beroperasi tanpa gangguan | Persentase waktu operasional tanpa gangguan (uptime) dalam 24 jam | Ratio | % & Jam | Data log mikrokontroler (timestamp aktif/non-aktif) | Mengukur reliabilitas sistem di kondisi nyata |
| Akurasi Kontrol Lingkungan | Secondary / DV pendukung | Presisi pengendalian suhu & kelembaban | Rata-rata deviasi absolut dari nilai setpoint optimal | Ratio | °C & %RH | Sensor DHT22 yang dikalibrasi | Menunjukkan kualitas otomasi IoT yang berdampak pada pertumbuhan tanaman |
| Pertumbuhan Tanaman | Secondary Outcome | Produktivitas agronomis | Tinggi tanaman & jumlah daun per tanaman | Ratio | cm & helai | Pengukuran manual mingguan dengan penggaris digital | Membuktikan bahwa peningkatan teknis juga memberikan manfaat praktis |

Alignment Check:
  RQ → Concept → Variable → Metric → Data → Result
  [v] Setiap langkah terdokumentasi
  [v] Tidak ada "lompatan logis"
  [v] Metrik mengukur apa yang dimaksud (construct validity)
```

---

## Latihan 1 — Operationalization Chain

Gunakan RQ dari WS-04. Definisikan variabel dan metriknya.

**RQ:** Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem dibandingkan baseline?

| Variabel | Tipe | Konsep Abstrak | Metrik Konkret | Skala (NOIR) | Satuan |
|----------|------|---------------|----------------|-------------|--------|
| Desain Sistem | IV | Kualitas integrasi IoT dan manajemen energi | Holistic Design vs Baseline | Nominal | — |
| Efisiensi Energi | DV | Optimalisasi penggunaan energi terbarukan | Persentase efisiensi harian | Ratio | % |
| Kestabilan Operasional | DV |Keandalan sistem | Uptime 24 jam | Ratio |  % / Jam |
| Kontrol Lingkungan | DV Pendukung | Presisi otomasi | Deviasi suhu & kelembaban | Ratio | °C / %RH |

**Apakah ada lompatan logis dalam rantai?** [ ] Ya / [v] Tidak
> Jika ya, di mana? ____________________________________

---

## Latihan 2 — Evaluasi Metrik

Evaluasi metrik DV yang dipilih di Latihan 1 menggunakan 3 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Representative | 5 | Langsung mewakili konsep keberlanjutan energi yang menjadi inti masalah riset |
| Sensitive | 4 | Sangat sensitif terhadap perubahan desain (pengelolaan baterai, scheduling aktuator, dll.) |
| Feasible | 4 | Dapat diukur dengan peralatan yang tersedia (multimeter + data logger), meski memerlukan pengamatan rutin |

**Apakah perlu secondary metric?** [v] Ya / [ ] Tidak
> Jika ya, apa dan mengapa? Ya, diperlukan Akurasi Kontrol Lingkungan dan Pertumbuhan Tanaman. Karena efisiensi energi saja belum cukup — kita juga harus memastikan bahwa sistem tidak hanya hemat energi, tetapi juga menghasilkan lingkungan yang optimal bagi tanaman (construct validity yang lebih lengkap).

**Contoh kasus ceiling effect untuk metrik ini:**
> Jika baseline sudah mencapai efisiensi >95%, maka sulit mendeteksi improvement yang bermakna (ceiling effect). Oleh karena itu, pengujian dilakukan dalam kondisi variasi cahaya matahari yang realistis agar metrik tetap sensitif.

---

## Latihan 3 — Data Quality Check

Bayangkan data yang akan dikumpulkan dari eksperimen. Evaluasi 4 dimensi kualitas data.

| Dimensi | Pertanyaan | Jawaban | Strategi Mitigasi |
|---------|-----------|---------|------------------|
| Completeness | Apakah semua data point terkumpul? | Kemungkinan ada missing data saat sensor gagal atau koneksi IoT terputus | Logging redundan (local SD card + cloud), alarm notifikasi |
| Consistency | *Apakah ada kontradiksi internal?* | Mungkin terjadi inkonsistensi antar sensor | Kalibrasi rutin sensor & validasi silang antar perangkat |
| Validity | *Apakah benar-benar mengukur yang dimaksud?* | Ya, jika sensor ditempatkan pada posisi representatif | Dokumentasi prosedur pengukuran dan kalibrasi |
| Representativeness | *Apakah sampel mewakili populasi target?* | Prototipe skala kecil, pengujian simulasi cuaca | Melakukan pengujian di minimal 2–3 siklus cuaca berbeda (cerah, mendung, hujan) |

---

## Refleksi

> Mengapa memilih metrik setelah melihat data dianggap p-hacking? Apa bedanya dengan eksplorasi data yang sah?

**Jawaban:**
> Memilih atau mengubah metrik setelah melihat data disebut p-hacking karena peneliti cenderung “mencari” metrik yang menghasilkan hasil signifikan, sehingga meningkatkan risiko kesimpulan palsu (false positive). Ini merusak integritas ilmiah karena hipotesis seolah-olah terbukti padahal hanya “dibuat cocok” dengan data, Sedangkan eksplorasi data yang sah adalah ketika kita terbuka mencari pola baru atau insight tambahan setelah analisis konfirmatori utama selesai, dan melaporkannya secara transparan sebagai analisis eksploratori (bukan sebagai bukti utama hipotesis). Perbedaannya terletak pada preregistration metrik primer dan transparansi pelaporan.
Saya menyadari bahwa disiplin dalam memilih metrik sejak awal adalah salah satu bentuk etika riset yang paling penting.
