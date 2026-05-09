# WS-03: Literature Mapping & Gap

> **Bab 3 — Literature Review, Research Gap & Baseline**

---

## Ringkasan Materi

### Literature Review = Positioning, Bukan Ringkasan

Literature review bukan merangkum paper satu per satu. Pendekatan yang benar adalah **concept-centric** — organisasi berdasarkan tema, metode, atau variabel. Tujuan: menemukan **pola, kontradiksi, dan gap**.

**Perbandingan pendekatan Author-centric vs Concept-centric:**

| Aspek | Author-centric (Hindari) | Concept-centric (Gunakan) |
|-------|--------------------------|---------------------------|
| Struktur | Per penulis/paper ("Rahman et al. menyatakan...") | Per konsep/metode ("Pendekatan berbasis transformer") |
| Tujuan | Ringkasan isi paper | Perbandingan metode & identifikasi gap |
| Contoh paragraph | "Rahman (2023) pakai CNN. Lee (2022) pakai LSTM. Zhang (2021) pakai RF." | "Tiga pendekatan dominan: CNN digunakan oleh 4 paper untuk representasi fitur visual; LSTM untuk data sekuensial; RF sebagai baseline klasik." |
| Hasil akhir | Daftar paper | Peta pengetahuan + gap yang teridentifikasi |

### Empat Jenis Research Gap

| Jenis Gap | Deskripsi | Contoh |
|-----------|----------|--------|
| **Performance Gap** | Performa belum memadai | Akurasi deteksi hanya 78% pada kasus tertentu |
| **Method Gap** | Pendekatan belum diterapkan | Belum ada yang pakai transformer untuk task ini |
| **Data Gap** | Dataset terbatas/tidak representatif | Semua studi pakai dataset sintetis |
| **Context Gap** | Belum diuji pada konteks berbeda | Belum ada evaluasi di negara berkembang |

Gap terkuat = kombinasi 2+ jenis.

### Systematic Search Strategy

1. **Database utama**: IEEE Xplore, ACM DL, Scopus
   - Akses IEEE/ACM melalui jaringan kampus atau VPN institusi
   - Alternatif bebas biaya: Google Scholar, ResearchGate ([researchgate.net](https://www.researchgate.net)), arXiv ([arxiv.org](https://arxiv.org))
2. **Boolean query** yang terdokumentasi eksplisit
   - Contoh: `("anomaly detection" OR "intrusion detection") AND ("deep learning" OR "neural network") NOT ("medical imaging")`
   - Gunakan tanda kutip untuk frasa eksak; AND/OR/NOT mengontrol scope
3. **Snowballing** — dua arah:
   - **Backward snowballing**: buka daftar referensi di paper kunci → telusuri paper yang dikutip
   - **Forward snowballing**: di Google Scholar, klik "Cited by" di bawah paper kunci → temukan paper yang mengutipnya
   - Ulangi 1–2 tingkat untuk membangun cakupan komprehensif
4. Klaim "belum ada penelitian" harus didukung **bukti pencarian**

### Baseline Selection — 3 Kriteria

| Kriteria | Pertanyaan |
|----------|-----------|
| **Relevan** | Apakah menyelesaikan masalah yang sama? |
| **Representatif** | Apakah mewakili common practice? |
| **State-of-the-Art** | Apakah terbaru/terbaik? |

Membandingkan deep learning 2024 dengan decision tree sederhana tanpa justifikasi = **straw man comparison** (perbandingan tidak jujur).

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan baca literatur | Mencari solusi yang sudah ada | Memahami apa yang belum terjawab |
| Cara membaca paper | Tutorial, how-to | Metode, limitasi, gap |
| Baseline | Framework terpopuler | State-of-the-art yang rigorous |
| Dokumentasi pencarian | Tidak diperlukan | Wajib (reproducible) |

### Istilah Penting

- **Concept-centric** — Organisasi literatur berdasarkan konsep/metode, bukan per penulis
- **Snowballing** — Backward (telusuri referensi) + Forward (cari yang mengutip paper kunci)
- **Research Position** — Pernyataan eksplisit posisi riset terhadap studi sebelumnya
- **Straw man comparison** — Memilih baseline lemah agar metode sendiri terlihat lebih baik

---

## Template A.3 — Literature Mapping & Gap Identification

```
LITERATURE MAPPING

Topik      : Integrasi IoT dan Energi Terbarukan (Panel Surya) pada Sistem Hidroponik Cerdas
Database   : Google Scholar, IEEE Xplore, ResearchGate, Semantic Scholar
Query      : ("hydroponic" OR "hidroponik") AND ("IoT" OR "Internet of Things") AND ("solar" OR "panel surya" OR "renewable energy" OR "photovoltaic")
Tahun      : 2019–2025
Hasil awal : 45 paper → Screening → 7 paper final

Literature Matrix (concept-centric):

| Study | Tahun | Method | Data | Result | Limitation |
|-------|-------|--------|------|--------|------------|
| Wardhana et al. | 2025 | Arduino Uno + ESP, DHT22, Blynk, Panel Surya 100Wp |Prototipe lab + uji lapangan singkat (4 minggu) | Operasional 24 jam penuh, efisiensi energi 69-74% | Pengujian pendek, tidak ada metrik pertumbuhan tanaman, fluktuasi cuaca belum dieksplorasi mendalam |
| Khare et al. | 2023 | IoT + Solar + AI (prediksi) | Prototipe greenhouse | Peningkatan efisiensi & otomasi | Fokus AI masih simulasi, integrasi energi kurang detail |
| Don Chua et al. | 2024 | PV 45Wp + IoT irrigation | City farming hydroponic | Dapat suplai 19W pump + LED | Skala kecil, hanya irigasi, belum full otomasi lingkungan |
| Alfita et al. | 2024 | Vertical Aquaponic + Renewable + AI | Prototipe vertical farming | Sistem mandiri energi | Kombinasi aquaponic (bukan pure hidroponik), evaluasi AI masih awal |
| A’Ffan et al. | 2022 | PV + IoT soil moisture & humidity | Hydroponic plant | Monitoring & kontrol dasar | Tidak ada pengujian jangka panjang dan skalabilitas |
| Mohan et al. | 2021 | IoT Onion Farming + Solar | Hydroponic monitoring | Monitoring real-time | Fokus spesifik tanaman bawang, kurang general |
| Nugraha et al. | 2025 | ESP32 + Sensor pH/TDS + Solar 50Wp | Prototipe nutrisi otomatis | Akurasi sensor >96% | Belum integrasi kontrol lingkungan lengkap (suhu, cahaya, kipas) |
Pola yang ditemukan:
  Metode dominan     : Mikrokontroler low-cost (Arduino/ESP32) + platform IoT (Blynk) + panel surya skala kecil.
  Dataset umum       : Prototipe laboratorium atau uji lapangan singkat (mingguan).
  Limitasi berulang  : Pengujian jangka pendek, kurangnya evaluasi performa tanaman jangka panjang, minim analisis robustness terhadap cuaca ekstrem, dan skalabilitas masih rendah.

GAP IDENTIFICATION

Gap 1: [Jenis: Context Gap]
  Deskripsi    : Mayoritas penelitian dilakukan di lingkungan laboratorium atau kondisi ideal, sedangkan aplikasi di daerah terpencil Indonesia dengan intensitas matahari fluktuatif dan keterbatasan infrastruktur belum banyak dieksplorasi secara mendalam.
  Bukti        : Hampir semua studi hanya melaporkan hasil positif dalam waktu singkat tanpa pengujian musim hujan/panjang.
  Signifikansi : Sangat penting bagi Indonesia sebagai negara agraris dengan banyak wilayah rural yang belum teraliri listrik stabil.

Gap 2: [Jenis: Performance & Method Gap]
  Deskripsi    : Belum ada desain yang mengintegrasikan secara holistik otomasi IoT lengkap (suhu, kelembaban, pencahayaan, irigasi, keamanan) dengan manajemen energi surya yang adaptif dan evaluasi komprehensif terhadap pertumbuhan tanaman.
  Bukti        : Kebanyakan fokus pada salah satu aspek (monitoring atau irigasi saja), jarang yang mengukur outcome agronomis (tinggi tanaman, hasil panen).
  Signifikansi : Diperlukan untuk membuktikan bahwa sistem tidak hanya “bekerja”, tetapi benar-benar memberikan nilai tambah produktivitas dan keberlanjutan.

Baseline Selection:
| Baseline | Relevansi | Representatif | Source |
|----------|-----------|---------------|--------|
| Sistem IoT Hidroponik dengan Panel Surya (Arduino/ESP + Blynk | Mirip arsitektur dasar yang akan dikembangkan | Paling umum digunakan di literatur Indonesia & Asia Tenggara | Wardhana et al. (2025), Nugraha et al. (2025) |
| Sistem irigasi IoT Solar-powered sederhana | Mewakili pendekatan minimalis yang fokus energi | Banyak dipakai sebagai starting point | Don Chua et al. (2024), Al-Ali et al. (2019) |
```

---

## Latihan 1 — Concept-Centric Literature Table

Gunakan topik riset dari WS-02. Cari minimal 5 paper relevan menggunakan database akademik.

> **Panduan pencarian:**
> - Database: IEEE Xplore, ACM DL, Google Scholar, atau ResearchGate
> - Tulis query Boolean yang digunakan: contoh `("object detection" OR "image classification") AND ("edge computing") NOT ("medical")`. Dokumentasikan query secara eksplisit.
> - Akses gratis: buka Google Scholar → cari judul paper → klik [PDF] jika tersedia, atau akses lewat campus VPN

**Topik riset:** Integrasi IoT dan Energi Terbarukan (Panel Surya) pada Sistem Hidroponik Cerdas
**Query pencarian:** ("hydroponic" OR "hidroponik") AND ("IoT" OR "Internet of Things") AND ("solar" OR "panel surya" OR "renewable energy" OR "photovoltaic")
**Database:** Google Scholar, IEEE Xplore, ResearchGate, Semantic Scholar

| # | Study | Tahun | Method | Dataset | Result | Limitasi |
|---|-------|-------|--------|---------|--------|----------|
| 1 | Wardhana et al. | 2025 | Arduino Uno + ESP, DHT22, Blynk, Panel Surya 100Wp |Prototipe lab + uji lapangan singkat (4 minggu) | Operasional 24 jam penuh, efisiensi energi 69-74% | Pengujian pendek, tidak ada metrik pertumbuhan tanaman, fluktuasi cuaca belum dieksplorasi mendalam |
| 2 | Khare et al. | 2023 | IoT + Solar + AI (prediksi) | Prototipe greenhouse | Peningkatan efisiensi & otomasi | Fokus AI masih simulasi, integrasi energi kurang detail |
| 3 | Don Chua et al. | 2024 | PV 45Wp + IoT irrigation | City farming hydroponic | Dapat suplai 19W pump + LED | Skala kecil, hanya irigasi, belum full otomasi lingkungan |
| 4 | Alfita et al. | 2024 | Vertical Aquaponic + Renewable + AI | Prototipe vertical farming | Sistem mandiri energi | Kombinasi aquaponic (bukan pure hidroponik), evaluasi AI masih awal |
| 5| A’Ffan et al. | 2022 | PV + IoT soil moisture & humidity | Hydroponic plant | Monitoring & kontrol dasar | Tidak ada pengujian jangka panjang dan skalabilitas |
| 6 | Mohan et al. | 2021 | IoT Onion Farming + Solar | Hydroponic monitoring | Monitoring real-time | Fokus spesifik tanaman bawang, kurang general |
| 7 | Nugraha et al. | 2025 | ESP32 + Sensor pH/TDS + Solar 50Wp | Prototipe nutrisi otomatis | Akurasi sensor >96% | Belum integrasi kontrol lingkungan lengkap (suhu, cahaya, kipas) |

**Pola yang terlihat — Metode dominan:** Mikrokontroler low-cost + IoT cloud sederhana.
**Limitasi yang berulang:** Pengujian jangka pendek dan kurangnya fokus pada outcome tanaman serta adaptasi konteks lokal.
---

## Latihan 2 — Gap Identification

Berdasarkan tabel di Latihan 1, identifikasi gap.

| Jenis Gap | Ditemukan? | Gap Statement |
|-----------|-----------|---------------|
| Performance Gap | [ ] Ya / [v] Tidak | - |
| Method Gap | [v] Ya / [ ] Tidak | Belum ada pendekatan yang mengintegrasikan otomasi IoT secara lengkap (suhu, kelembaban, pencahayaan, irigasi, dan keamanan) dengan manajemen energi surya yang adaptif serta evaluasi komprehensif terhadap pertumbuhan tanaman. |
| Data Gap | [ ] Ya / [v] Tidak | |
| Context Gap | [v] Ya / [ ] Tidak | Mayoritas penelitian hanya diuji di lingkungan laboratorium atau kondisi ideal dalam waktu singkat, sedangkan pengujian di konteks daerah terpencil dengan fluktuasi cuaca ekstrem (musim hujan/panjang) di Indonesia masih sangat terbatas. |

**Gap utama yang dipilih:** ontext Gap + Method Gap (Kombinasi)
**Mengapa gap ini penting (bukan sekadar "belum ada yang meneliti")?**
> Gap ini penting karena meskipun banyak prototipe IoT + solar sudah dikembangkan, solusi yang ada masih kurang siap diterapkan di lapangan nyata oleh petani kecil di daerah terpencil Indonesia. Sistem yang hanya diuji dalam kondisi ideal sering gagal ketika dihadapkan pada variabilitas cuaca dan keterbatasan infrastruktur. Mengisi gap ini akan menghasilkan desain yang lebih robust, kontekstual, dan berdampak nyata terhadap ketahanan pangan serta efisiensi energi di tingkat grassroots, bukan hanya sekadar tambahan literatur.

---

## Latihan 3 — Baseline Selection

Pilih 2 baseline dari literatur yang sudah dibaca.

| # | Baseline | Mengapa Relevan | Mengapa Representatif | Apakah SOTA? | Sumber |
|---|----------|----------------|----------------------|-------------|--------|
| 1 | Sistem IoT Hidroponik berbasis Arduino/ESP + Panel Surya + Blynk (otomasi dasar) | Memiliki arsitektur dan komponen yang mirip dengan yang akan dikembangkan | Pendekatan paling umum di literatur Indonesia terkini | Bukan (Common Practice| Wardhana et al. (2025), Nugraha et al. (2025) |
| 2 | Sistem irigasi otomatis berbasis solar-powered IoT sederhan | Fokus pada integrasi energi terbarukan dengan kontrol dasar hidroponik | Mewakili pendekatan minimalis yang banyak digunakan sebagai starting point | Bukan | Don Chua et al. (2024), Alfita et al. (2024) |

**Apakah pemilihan baseline ini bisa dianggap straw man?** [ ] Ya / [v] Tidak
> Justifikasi:Tidak, karena saya memilih baseline yang paling relevan dan representatif di literatur saat ini, bukan sistem yang jelas lebih lemah. Perbandingan akan dilakukan secara adil menggunakan metrik yang sama (efisiensi energi, kestabilan operasional 24 jam, dan kemampuan adaptasi lingkungan) sehingga hasil perbandingan lebih kredibel dan ilmiah.

---

## Refleksi

> Apa perbedaan antara "belum ada yang meneliti ini" (klaim tanpa bukti) dengan research gap yang valid? Bagaimana cara membuktikan bahwa sebuah gap benar-benar ada?

**Jawaban:**
> Perbedaan mendasar antara klaim “belum ada yang meneliti ini” dengan research gap yang valid adalah pada kedalaman bukti dan signifikansinya. Klaim “belum ada” biasanya muncul karena pencarian literatur yang dangkal atau terlalu sempit — peneliti hanya tidak menemukan paper yang persis sama. Sedangkan research gap yang valid adalah ketika kita menemukan pola limitasi yang berulang di banyak studi berkualitas, lalu mengidentifikasi peluang perbaikan yang jelas dan bermakna.
> Cara membuktikan bahwa sebuah gap benar-benar ada: Melakukan pencarian sistematis yang didokumentasikan dengan baik (query, database, rentang tahun), Menggunakan tabel literature mapping untuk menunjukkan pola dan limitasi yang konsisten, Menjelaskan mengapa mengisi gap tersebut penting secara ilmiah (pengetahuan baru) dan praktis (dampak nyata), Menunjukkan bahwa gap tersebut bukan sekadar kekosongan, melainkan hambatan bagi kemajuan di bidang tersebut, Dengan begitu, literature review kita menjadi fondasi yang kuat, bukan sekadar formalitas.
