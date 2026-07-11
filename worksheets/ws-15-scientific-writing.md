# WS-15: Scientific Writing

> **Bab 15 — Penulisan Ilmiah**

---

## Ringkasan Materi

### Scientific Argument Flow

```
Problem → Gap → RQ → Method → Result → Analysis → Conclusion → Contribution
```

Paper ilmiah adalah **satu argumen utuh** dari masalah ke kontribusi. Setiap node harus terhubung logis ke node sebelum dan sesudahnya.

### Struktur IMRAD

| Section | Peran | Pertanyaan Kunci |
|---------|-------|-----------------|
| **Introduction** | Motivasi + frame | Why is this needed? |
| **Method** | Deskripsi (reproducible) | How was it done? |
| **Results** | Laporan objektif | What was found? |
| **Discussion** | Interpretasi + refleksi | What does it mean? |
| **Conclusion** | Ringkasan + kontribusi | So what? |

### Logical Flow — "Red Thread"

Setiap paragraf menjawab satu pertanyaan dan memicu pertanyaan berikutnya. Alur logis ini harus terasa di tiga level:
1. **Antar-kalimat** dalam paragraf
2. **Antar-paragraf** dalam section
3. **Antar-section** dalam paper

### Internal Consistency

Setiap elemen yang dijanjikan di Introduction harus hadir di Discussion/Conclusion.

**Consistency Matrix:**
```
           Intro  Method  Result  Discuss  Conclude
RQ1          ✓      ✓       ✓       ✓        ✓
RQ2          ✓      ✓       ✓       ✗ ←      ✓
Metrik-X     ✗      ✗       ✓ ←     ✗        ✗
```
**Masalah:** RQ2 dibahas di semua bagian kecuali Discussion. Metrik-X muncul di Result tapi tidak diperkenalkan di Method.

### Writing Quality Triad

| Kualitas | Deskripsi | Contoh Buruk → Baik |
|----------|----------|---------------------|
| **Clarity** | Dipahami sekali baca | "Performa meningkat" → "Accuracy meningkat dari 85.3% ke 89.7%" |
| **Precision** | Istilah eksak, tanpa ambiguitas | "signifikan" → "signifikan secara statistik (p=0.003, d=1.2)" |
| **Conciseness** | Setiap kata menambah informasi | Hapus kalimat redundan, filler words |

### Urutan Penulisan yang Disarankan

1. **Method & Results** — paling stabil, tulis pertama
2. **Discussion** — interpretasi berdasarkan hasil
3. **Introduction** — frame sesuai temuan aktual
4. **Abstract & Conclusion** — terakhir

### Target Jumlah Kata

| Section | Target |
|---------|--------|
| Introduction | 500–700 |
| Related Work | 700–1000 |
| Method | 800–1200 |
| Results | 500–800 |
| Discussion | 600–900 |
| Conclusion | 200–400 |

### Jebakan Kognitif

1. "Lebih panjang = lebih lengkap" → conciseness lebih berharga
2. "Introduction harus ditulis pertama" → justru ditulis terakhir
3. "Jargon teknis = lebih ilmiah" → clarity lebih penting
4. "Discussion = ringkasan Results" → Discussion = interpretasi + konteks

---

## Template A.15 — Paper Structure Checklist

```
PAPER STRUCTURE CHECKLIST

Title   : Evaluasi Performa Desain Integrasi IoT Holistik dengan Adaptive Energy Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas di Kondisi Fluktuasi Energi Daerah Terpencil
Target  : [✓] Jurnal  [ ] Konferensi  [ ] Laporan

Section Check:
  [✓] Abstract — masalah, metode, hasil utama, kontribusi (max 250 kata)
  [✓] Introduction — konteks → gap → RQ → kontribusi → struktur paper
  [✓] Related Work — concept-centric, gap positioning
  [✓] Method — reproducible: desain, variabel, metrik, setup, prosedur
  [✓] Results — tabel + grafik + observasi (tanpa interpretasi)
  [✓] Discussion — interpretasi, perbandingan, implikasi, limitation
  [✓] Conclusion — jawaban RQ, kontribusi, future work

Consistency Matrix:
  [✓] RQ di Introduction = RQ di Method = RQ di Conclusion
  [✓] Variabel di Method = variabel di Results
  [✓] Klaim di Discussion didukung data di Results
  [✓] Limitasi di Discussion di-address di Conclusion/Future Work

Writing Quality:
  [✓] Clarity — mudah dipahami tanpa re-read
  [✓] Precision — tidak ada istilah ambigu
  [✓] Conciseness — tidak ada kalimat redundan
```

---

## Latihan 1 — Paper Outline

Buat outline paper untuk riset Anda menggunakan struktur IMRAD.

| Section | Konten Utama (2-3 kalimat) | Target Kata |
|---------|---------------------------|------------|
| Abstract | Menjelaskan masalah ketergantungan energi pada sistem hidroponik IoT, metode Adaptive Energy Scheduler berbasis panel surya menggunakan dataset NASA POWER, hasil eksperimen menunjukkan Adaptive Scheduler memperoleh efisiensi rata-rata 42.19% dibanding Rule-Based 40.40%, serta kontribusi penelitian terhadap pengelolaan energi hidroponik. | 200–250 |
| Introduction | Menjelaskan pentingnya hidroponik cerdas, tantangan fluktuasi energi di daerah terpencil, research gap pada sistem rule-based, research question, hipotesis, serta kontribusi Adaptive Energy Scheduler. | 500-700 |
| Related Work | Mengulas penelitian mengenai smart farming, IoT, hidroponik, panel surya, battery management, dan adaptive energy management serta mengidentifikasi research gap yang belum terjawab. | 700-1000 |
| Method | Menjelaskan Design Science Research, dataset NASA POWER, preprocessing, PV Model, Energy Demand Model, Battery Model, Rule-Based Scheduler, Adaptive Scheduler, setup eksperimen, metrik evaluasi, serta teknik analisis data.| 800-1200 |
| Results | Menyajikan hasil eksperimen berupa tabel efisiensi, statistik deskriptif, grafik perbandingan Rule-Based dan Adaptive Scheduler, serta hasil lima kali eksperimen. | 500-800 |
| Discussion | Menginterpretasikan peningkatan efisiensi Adaptive Scheduler, membahas hubungan dengan penelitian terdahulu, menjelaskan keterbatasan penelitian, serta implikasi praktis terhadap sistem hidroponik cerdas. | 600-900 |
| Conclusion | Menyimpulkan bahwa Adaptive Scheduler memberikan peningkatan efisiensi dibanding Rule-Based Scheduler pada konfigurasi yang digunakan serta memberikan rekomendasi penelitian lanjutan. | 200-400 |

---

## Latihan 2 — Consistency Matrix

Buat consistency matrix untuk memverifikasi internal consistency paper Anda.

|  | Intro | Method | Result | Discussion | Conclusion |
|--|-------|--------|--------|-----------|-----------|
| RQ1 | ✓ | ✓ | ✓ | ✓ | ✓ |
| Hipotesis | ✓ | ✓ | ✓ | ✓ | ✓ |
| Metrik Efisiensi Energi | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel IV (Adaptive vs Rule-Based) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Variabel DV (Efisiensi, SOC) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Dataset NASA POWER | ✓ | ✓ | ✓ | ✓ | ✓ |
| PV Model| ✗ | ✓ | ✓ | ✓ | ✓ |
| Battery Model | ✗ | ✓ | ✓ | ✓ | ✓ |
| Adaptive Scheduler | ✓ | ✓ | ✓ | ✓ | ✓ |
| Kontribusi Penelitian | ✓ | ✓ | ✓ | ✓ | ✓ |

**Isi setiap sel:** ✓ (ada & konsisten), ✗ (missing), ~ (ada tapi inkonsisten)

**Inkonsistensi yang ditemukan:**
> Tidak ditemukan inkonsistensi utama. Seluruh komponen penelitian telah muncul secara konsisten mulai dari Introduction hingga Conclusion. Beberapa komponen teknis seperti PV Model dan Battery Model tidak dijelaskan secara rinci pada Introduction karena memang merupakan bagian metodologi penelitian.

**Tindakan perbaikan:**
> Memastikan semua metrik evaluasi yang digunakan pada Results telah dijelaskan pada bagian Method.
> Menambahkan pembahasan mengenai keterbatasan Adaptive Scheduler pada bagian Discussion.
> Menyelaraskan kembali nilai hasil eksperimen yang ditampilkan pada Abstract, Results, Discussion, dan Conclusion agar menggunakan angka yang sama.

---

## Latihan 3 — Writing Quality Check

Ambil satu paragraf dari tulisan Anda (atau tulis paragraf baru) dan evaluasi kualitasnya.

**Paragraf asli:**
> Penelitian ini mengembangkan sistem Adaptive Energy Scheduler berbasis panel surya untuk meningkatkan efisiensi penggunaan energi pada sistem hidroponik cerdas. Sistem menggunakan dataset NASA POWER sebagai sumber data intensitas radiasi matahari dan kondisi lingkungan untuk melakukan simulasi pengelolaan energi.

| Kriteria | Evaluasi | Perbaikan |
|----------|---------|-----------|
| Clarity | Sudah jelas tetapi belum menyebutkan hasil penelitian. | Tambahkan hasil eksperimen secara eksplisit. |
| Precision | Belum menyebutkan nilai peningkatan efisiensi secara spesifik. | Tambahkan nilai efisiensi Rule-Based dan Adaptive Scheduler. |
| Conciseness | Sudah cukup ringkas. | Tidak diperlukan pengurangan kalimat. |

**Paragraf setelah perbaikan:**
> Penelitian ini mengembangkan Adaptive Energy Scheduler berbasis panel surya untuk meningkatkan efisiensi penggunaan energi pada sistem hidroponik cerdas. Simulasi menggunakan dataset NASA POWER tahun 2024 yang berisi 8784 data radiasi matahari dan kondisi lingkungan. Hasil eksperimen menunjukkan bahwa Adaptive Energy Scheduler memperoleh rata-rata efisiensi sebesar 42.19%, lebih tinggi dibandingkan Rule-Based Scheduler sebesar 40.40%, sehingga menghasilkan peningkatan efisiensi rata-rata sebesar 1.79% pada konfigurasi simulasi yang digunakan.

---

## Refleksi

> Apa perbedaan antara menulis "tentang" riset dan menulis sebagai "argumen" riset? Bagaimana urutan penulisan (Method → Discussion → Introduction) mengubah kualitas tulisan?

> Menulis tentang penelitian berarti hanya menjelaskan apa yang dilakukan selama proses penelitian, sedangkan menulis sebagai argumen ilmiah berarti menyusun rangkaian penjelasan yang logis untuk meyakinkan pembaca bahwa penelitian tersebut memang diperlukan, dilakukan dengan metode yang tepat, menghasilkan temuan yang dapat dipercaya, dan memberikan kontribusi ilmiah. Dalam penulisan ilmiah, setiap bagian harus saling terhubung mulai dari masalah penelitian, research gap, pertanyaan penelitian, metode, hasil, pembahasan, hingga kesimpulan.
> Saya juga memahami bahwa urutan penulisan Method → Results → Discussion → Introduction → Abstract → Conclusion lebih efektif dibandingkan menulis secara berurutan dari pendahuluan. Dengan menyelesaikan bagian metode dan hasil terlebih dahulu, seluruh data eksperimen telah tersedia sehingga pembahasan dapat dibuat berdasarkan bukti yang nyata. Pendahuluan kemudian dapat disesuaikan dengan hasil penelitian yang diperoleh, sedangkan abstrak dan kesimpulan menjadi ringkasan akhir yang konsisten dengan keseluruhan isi artikel. Pendekatan ini membantu menghasilkan tulisan yang lebih sistematis, konsisten, dan mudah dipahami oleh pembaca maupun reviewer.
