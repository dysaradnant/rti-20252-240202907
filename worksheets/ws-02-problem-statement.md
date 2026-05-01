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
  Domain   : Internet of Things (IoT), Smart Agriculture, dan sistem otomasi energi terbarukan.
  Konteks  : Pengembangan sistem hidroponik otomatis pada area pertanian urban/off-grid yang memiliki keterbatasan pasokan listrik konvensional serta membutuhkan stabilitas lingkungan tanaman secara berkelanjutan.

System Context
  Input       : Pembacaan suhu dan kelembapan dari sensor DHT22 serta suplai energi dari panel surya dan baterai.
  Process     : Arduino Uno memproses data lingkungan, membandingkannya dengan nilai ambang tertentu, lalu mengontrol pompa air dan kipas secara otomatis.
  Output      : Status operasional aktuator (pompa/kipas), notifikasi kondisi sistem, dan monitoring data melalui dashboard IoT.
  Outcome     : Terjaganya kestabilan kondisi lingkungan hidroponik sehingga mendukung pertumbuhan tanaman secara optimal.
  Constraints : Kapasitas penyimpanan energi baterai, ketergantungan intensitas cahaya matahari, keterbatasan akurasi sensor, serta biaya implementasi perangkat.
  Stakeholders: Petani hidroponik skala rumah tangga/urban farming, peneliti smart agriculture, pengembang sistem IoT, dan pelaku UMKM pertanian.

Fenomena → Problem
  Fenomena yang diamati             : Budidaya hidroponik sering mengalami penurunan produktivitas akibat perubahan suhu ekstrem dan ketergantungan pada pengawasan manual.
  Gejala (symptom) yang terukur     : Peningkatan risiko kematian bibit tanaman hingga sekitar 30% pada kondisi lingkungan yang tidak stabil.
  Masalah yang didiagnosis          : Belum tersedianya sistem monitoring dan kontrol otomatis yang mampu bekerja secara real-time serta mandiri energi di lingkungan hidroponik.
  Masalah riset (researchable)      : Seberapa efektif integrasi sensor DHT22, kontrol berbasis threshold, dan panel surya dalam mempertahankan kestabilan suhu serta kelembapan pada sistem hidroponik otomatis?
  Variabel yang terukur             : Akurasi sensor suhu dan kelembapan, konsumsi daya sistem, waktu respons kontrol otomatis, serta kestabilan parameter lingkungan.

Problem Quality Check
  [ ] Clarity — Apakah satu orang membaca akan paham? Masalah terdefinisi jelas, spesifik, dan mudah dipahami.
  [ ] Measurability — Apakah ada metrik kuantitatif? Tersedia indikator kuantitatif seperti suhu, kelembapan, daya, dan respons waktu.
  [ ] Relevance — Apakah penting untuk domain? Relevan dengan pengembangan pertanian cerdas dan solusi off-grid.
  [ ] Testability — Apakah bisa gagal? Sistem dapat diuji keberhasilannya berdasarkan performa teknis.
  [ ] Impact — Apakah ada kontribusi jika terjawab? Berpotensi memberikan solusi aplikatif bagi pertanian modern berbiaya rendah.

Problem Statement (1 paragraf):
  Keterbatasan akses listrik serta ketidakstabilan kondisi lingkungan menjadi tantangan utama dalam pengelolaan sistem hidroponik, khususnya pada skala urban farming dan wilayah off-grid. Fluktuasi suhu dan kelembapan yang tidak terkontrol dapat menurunkan produktivitas tanaman dan meningkatkan risiko kegagalan panen. Oleh karena itu, penelitian ini berfokus pada pengembangan sistem otomasi hidroponik berbasis IoT menggunakan Arduino Uno, sensor DHT22, dan energi panel surya untuk menciptakan mekanisme pemantauan serta pengendalian lingkungan yang real-time, mandiri energi, dan efisien. Evaluasi dilakukan untuk mengukur efektivitas sistem dalam menjaga stabilitas parameter lingkungan secara berkelanjutan tanpa ketergantungan tinggi terhadap intervensi manual.
```

---

## Latihan 1 — Dari Topik ke Masalah Riset

Pilih satu topik di bidang TI yang diminati. Transformasikan melalui 5 tahap Problem Formation Model.

**Topik awal:** Sistem otomasi hidroponik berbasis Internet of Things (IoT) dengan energi surya

| Tahap | Hasil |
|-------|-------|
| Reality | Sistem hidroponik manual sering mengalami ketidakstabilan suhu dan kelembapan yang berdampak pada pertumbuhan tanaman. |
| Observed Issue (Symptom) | Tingkat kematian bibit tanaman dapat mencapai sekitar 30% saat terjadi cuaca ekstrem atau keterlambatan penyiraman manual. |
| Diagnosed Problem (Root Cause) | Kurangnya monitoring real-time dan tidak adanya kontrol otomatis mandiri energi menyebabkan respon terhadap perubahan lingkungan lambat. |
| Researchable Problem | Bagaimana efektivitas sistem hidroponik berbasis IoT dengan sensor DHT22 dan panel surya dalam menjaga kestabilan suhu serta kelembapan tanaman secara otomatis? |
| Measurable Variable | Akurasi sensor suhu/kelembapan, konsumsi energi sistem, waktu respons aktuator, kestabilan parameter lingkungan, dan tingkat keberhasilan pertumbuhan tanaman. |

**Apakah terjebak solution-first thinking?** [ ] Ya / [X] Tidak
> Jika ya, kembali ke tahap mana? ________________________

---

## Latihan 2 — System Context Decomposition

Gambarkan konteks sistem dari masalah riset di Latihan 1.

| Komponen | Deskripsi |
|----------|----------|
| Input | Data suhu dan kelembapan dari sensor DHT22, kondisi daya baterai, serta suplai energi dari panel surya. |
| Process | Arduino Uno memproses data sensor, membandingkannya dengan nilai ambang (threshold), lalu mengontrol pompa air dan kipas secara otomatis serta mengirim data ke dashboard IoT. |
| Output | Status aktuator (pompa/kipas aktif atau nonaktif), dashboard monitoring real-time, serta notifikasi kondisi lingkungan hidroponik. |
| Outcome | Stabilitas suhu dan kelembapan tanaman terjaga, efisiensi energi meningkat, serta pengurangan ketergantungan pada monitoring manual. |
| Constraints | Keterbatasan kapasitas baterai, ketergantungan pada intensitas sinar matahari, akurasi sensor DHT22, kestabilan koneksi internet, serta biaya implementasi perangkat. |
| Stakeholders | Petani hidroponik, pelaku urban farming, peneliti smart agriculture, pengembang sistem IoT, serta UMKM sektor pertanian. |

**Komponen mana yang paling relevan dengan masalah riset?** Process

---

## Latihan 3 — Problem Quality Check

Evaluasi problem statement yang sudah dibuat menggunakan 5 kriteria.

| Kriteria | Skor (1-5) | Justifikasi |
|----------|-----------|-------------|
| Clarity | 5 | Terdapat variabel kuantitatif yang jelas seperti suhu, kelembapan, konsumsi daya, waktu respons sistem, dan performa sensor. |
| Measurability | 5 | Sangat relevan dengan domain Smart Agriculture, IoT, dan solusi pertanian berkelanjutan, khususnya di lingkungan off-grid. |
| Relevance | 5 | Sistem dapat diuji secara objektif melalui performa teknis dan dapat dinyatakan gagal jika tidak memenuhi parameter lingkungan yang diharapkan. |
| Testability | 5 | Sistem dapat diuji secara objektif melalui performa teknis dan dapat dinyatakan gagal jika tidak memenuhi parameter lingkungan yang diharapkan. |
| Impact | 5 | Penelitian memiliki kontribusi praktis tinggi untuk meningkatkan efisiensi pertanian hidroponik dan menyediakan model implementasi murah serta mandiri energi. |

**Skor total:** 25 / 25

**Problem statement versi final (1 paragraf):**
> Keterbatasan akses energi listrik dan ketidakstabilan kondisi lingkungan merupakan tantangan utama dalam sistem pertanian hidroponik, terutama di wilayah dengan sumber daya terbatas. Fluktuasi suhu dan kelembapan yang tidak terkontrol dapat menyebabkan penurunan produktivitas hingga kegagalan panen. Oleh karena itu, penelitian ini berfokus pada pengembangan dan evaluasi sistem otomasi hidroponik berbasis Internet of Things (IoT) menggunakan sensor DHT22, Arduino Uno, dan energi panel surya untuk menciptakan pemantauan serta pengendalian lingkungan yang real-time, efisien, dan mandiri energi guna menjaga kestabilan pertumbuhan tanaman secara berkelanjutan.

---

## Refleksi

> Bandingkan "masalah" yang biasa ditemui saat coding (bug, error) dengan masalah riset. Apa perbedaan fundamental dalam cara mendefinisikan dan mendekati keduanya?

**Jawaban:**
> Masalah dalam coding seperti bug atau error biasanya bersifat teknis, spesifik, dan langsung terlihat melalui kegagalan fungsi program. Solusinya cenderung fokus pada identifikasi penyebab teknis lalu perbaikan kode secara langsung. Sebaliknya, masalah riset lebih kompleks karena berangkat dari fenomena nyata, memerlukan proses observasi, diagnosis akar masalah, validasi data, serta formulasi pertanyaan yang dapat diuji secara ilmiah. Dengan demikian, riset tidak hanya mencari “apa yang salah,” tetapi juga memahami “mengapa masalah terjadi” dan “bagaimana menghasilkan pengetahuan baru” yang relevan dan terukur.
