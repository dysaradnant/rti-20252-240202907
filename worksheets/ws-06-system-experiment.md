# WS-06: System-Experiment Mapping

> **Bab 6 — System Design sebagai Experimental Artifact**

---

## Ringkasan Materi

### Sistem = Instrumen Pengujian, Bukan Produk

Seorang engineer bertanya "apakah sistem bekerja?" — seorang peneliti bertanya "apa yang bisa dibuktikan sistem ini?" Sistem dalam riset adalah **artifact** — objek yang sengaja dibuat untuk menguji klaim spesifik.

### System as Experiment Model

```
RQ → Variable → System Component → Experimental Setup → Output
```

Setiap komponen sistem harus bisa ditelusuri ke variabel riset (top-down), dan setiap pengukuran harus menjawab RQ (bottom-up).

### Mapping Variabel ke Komponen

| Tipe Variabel | Peran di Sistem | Contoh |
|---------------|----------------|--------|
| **IV** (Independent) | Modul yang bisa di-toggle/swap | Algoritma A vs B |
| **DV** (Dependent) | Modul pengukuran | Logger, metrics collector |
| **CV** (Control) | Config yang dikunci | Dataset, parameter tetap |

Jika variabel tidak bisa di-map ke komponen apapun → arsitektur perlu didesain ulang.

### 4 Prinsip Desain Eksperimental

| Prinsip | Pertanyaan Kunci |
|---------|-----------------|
| **Traceability** | Komponen ini melayani variabel yang mana? |
| **Modularity** | Bisakah IV diubah tanpa memengaruhi yang lain? |
| **Controllability** | Apakah CV dieksternalisasi ke config file? |
| **Measurability** | Apakah sistem otomatis menghasilkan data yang dibutuhkan? |

### Variable Isolation melalui Arsitektur

- **Modular architecture** — Pisahkan berdasarkan variabel
- **Configuration-driven** — Ubah config (YAML/JSON), bukan code
- **Feature toggles** — On/off flag untuk ablation study

  Contoh config YAML dengan feature toggles:
  ```yaml
  model:
    type: cnn          # IV: ganti "rf" untuk kondisi baseline
  features:
    use_temporal: true  # toggle komponen temporal
    use_normalization: true  # toggle preprocessing
  experiment:
    seed: 42
    runs: 5
  ```
  Dengan pendekatan ini, berbeda kondisi eksperimen = berbeda satu baris config, **tanpa mengubah kode**.

### Research vs Engineering

| Aspek | Engineering | Research |
|-------|------------|----------|
| Tujuan sistem | Memenuhi kebutuhan user | Menguji hipotesis, menghasilkan bukti |
| Arsitektur | Optimasi performa & skalabilitas | Optimasi isolasi variabel & reprodusibilitas |
| Konfigurasi | Sering hardcoded | Dieksternalisasi ke config file |
| Fitur tambahan | Menambah nilai user | Menambah noise jika tidak terkait RQ |

### Istilah Penting

- **Artifact** — Objek yang sengaja dibuat untuk memecahkan masalah atau menguji proposisi
- **Traceability** — Kemampuan menelusuri hubungan RQ → variabel → komponen → output
- **Variable Isolation** — Mengubah hanya satu variabel sambil menahan yang lain konstan
- **Ablation Study** — Menguji kontribusi tiap komponen dengan melepasnya satu per satu
- **Configuration-driven Execution** — Semua parameter di config file, bukan hardcoded

---

## Template A.6 — Mapping RQ ke Arsitektur Sistem

```
SYSTEM-EXPERIMENT MAPPING

Research Question: Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem (waktu operasi 24 jam tanpa gangguan) dibandingkan dengan baseline sistem IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil dengan variasi intensitas cahaya matahari?

Variable → Component Mapping:
| Variabel | Tipe | Komponen Sistem | Cara Manipulasi/Pengukuran |
|----------|------|-----------------|---------------------------|
| Desain Sistem | IV | Arsitektur keseluruhan (Holistic Controller + Energy Management Module) | Ganti config mode: holistic_mode: true/false atau swap modul Energy Scheduler |
| Efisiensi Penggunaan Energi | DV | Energy Monitoring & Logging Module + Power Meter Interface | Data logger real-time (setiap 5 menit) + perhitungan otomatis |
| Kestabilan Operasional      | DV   | System Health Monitor + Uptime Tracker | Timestamp logging + deteksi downtime otomatis |
| Kontrol Lingkungan (Suhu & Kelembaban) | DV Pendukung | Sensor Fusion Layer + Actuator Controller | Sensor DHT22 + log deviasi terhadap setpoint |
| Kondisi Lingkungan (Intensitas Cahaya) | CV | Environmental Simulator / Sensor Input | Dikontrol melalui variasi lampu simulasi atau pengujian outdoor |

4 Prinsip Desain:
  [v] Traceability — Setiap komponen bisa ditelusuri ke variabel
  [v] Variable Isolation — IV bisa diubah tanpa mengubah CV
  [v] Measurement Integration — Pengukuran DV built-in
  [v] Reproducibility — Setup bisa direkonstruksi

Experimental Setup:
  Input data     : Data sensor real-time (DHT22, solar irradiance sensor, current/voltage sensor)
  Parameter      : Setpoint suhu & kelembaban, jadwal aktuator, threshold baterai, durasi pengujian (minimal 8 minggu)
  Output format  : CSV/JSON log harian (energi, uptime, deviasi sensor), grafik visualisasi, dan laporan summary per kondisi eksperimen
```

---

## Latihan 1 — Variable-to-Component Mapping

Gunakan RQ dan variabel dari WS-05. Petakan ke komponen sistem.

**RQ:** Apakah desain integrasi IoT holistik berbasis panel surya yang diusulkan mampu meningkatkan efisiensi penggunaan energi minimal sebesar 8% dan kestabilan operasional sistem (waktu operasi 24 jam tanpa gangguan) dibandingkan dengan baseline sistem IoT solar sederhana pada kondisi lingkungan simulasi daerah terpencil dengan variasi intensitas cahaya matahari?

| Variabel | Tipe | Komponen Sistem | Cara Manipulasi / Pengukuran |
|----------|------|-----------------|---------------------------|
| Desain Sistem | IV | Holistic Energy Management Module + Adaptive Scheduler | Toggle melalui configuration file |
| Efisiensi Penggunaan Energi | DV | Power Monitoring Subsystem | Real-time calculation + data logger |
| Kestabilan Operasional | DV | System Reliability Monitor | Continuous uptime logging |
| Akurasi Kontrol Lingkungan | DV | Actuator & Sensor Control Layer | Deviation logging dari setpoint |

**Apakah semua variabel bisa di-map?** [v] Ya / [ ] Tidak
> Jika tidak, komponen apa yang perlu ditambahkan? _________

---

## Latihan 2 — 4 Prinsip Desain

Evaluasi desain sistem terhadap 4 prinsip.

| Prinsip | Status | Bukti / Penjelasan |
|---------|--------|-------------------|
| Traceability | ✅ | Setiap modul utama diberi label sesuai variabel riset (misalnya folder energy_management/ untuk IV) |
| Modularity | ✅ | Modul Energy Scheduler, Sensor Fusion, dan Actuator Controller dapat diubah secara independen |
| Controllability | ✅ | Semua parameter penting (setpoint, scheduling logic, threshold) disimpan di file config YAML/JSON |
| Measurability | ✅ | Logging otomatis untuk semua metrik DV sudah terintegrasi sejak awal desain |

**Prinsip mana yang paling sulit dipenuhi?** Modularity & Variable Isolation
**Strategi untuk mengatasinya:**
> Saya akan menerapkan pendekatan configuration-driven design yang ketat dan membuat feature toggles untuk setiap komponen penting. Selain itu, saya akan mendokumentasikan setiap perubahan konfigurasi agar eksperimen dapat direplikasi dengan mudah oleh orang lain. Ini memang memerlukan disiplin ekstra di awal, tetapi sangat berharga untuk kredibilitas hasil riset.

---

## Latihan 3 — Ablation Study Planning

Jika sistem memiliki 3 komponen utama, rencanakan ablation study.

> **Panduan jumlah kondisi:** Untuk 3 komponen (A, B, C), kondisi minimal yang direkomendasikan:
> Full + (-A) + (-B) + (-C) = **4 kondisi dasar**. Jika waktu memungkinkan, tambahkan kombinasi ganda: (-A,-B), (-A,-C), (-B,-C) = **7 kondisi**. Sesuaikan dengan *computational cost* dan tenggat waktu penelitian.

| Kondisi | Holistic Scheduler | Adaptive Battery Management | Full Sensor Fusion | Hasil yang Diharapkan |
|---------|-----------|-----------|-----------|----------------------|
| Full | ✅ | ✅ | ✅ | Performa terbaik |
| – Scheduler | ❌ | ✅ | ✅ | Penurunan efisiensi energi |
| – Battery | ✅ | ❌ | ✅ | Penurunan kestabilan operasional |
| – Fusion | ✅ | ✅ | ❌ | Deviasi kontrol lingkungan meningkat |

**Komponen mana yang diprediksi paling berkontribusi?** Holistic Scheduler (pengaturan waktu aktuator berdasarkan prediksi ketersediaan energi surya)
**Mengapa?**
> Karena fluktuasi intensitas matahari adalah tantangan utama di daerah terpencil. Scheduler yang adaptif kemungkinan besar memberikan kontribusi paling besar terhadap efisiensi energi dan kestabilan sistem dibandingkan komponen lain.

---

## Refleksi

> Apa risiko jika sistem dibangun seperti produk (monolitik, fitur lengkap) lalu baru dilakukan eksperimen? Mengapa arsitektur modular penting untuk riset?

**Jawaban:**
> Risiko utama jika sistem dibangun seperti produk (monolitik dan fitur lengkap) lalu baru dilakukan eksperimen adalah kehilangan kontrol variabel. Sulit mengetahui komponen mana yang sebenarnya menyebabkan perbaikan (atau penurunan) performa. Selain itu, sulit mereplikasi eksperimen dan rawan confounding variable.
> Arsitektur modular sangat penting dalam riset karena memungkinkan variable isolation — kita bisa mengubah satu faktor saja sambil menjaga faktor lain konstan. Ini membuat klaim ilmiah kita lebih kuat, hasil lebih dapat dipercaya, dan memudahkan ablation study untuk memahami kontribusi masing-masing komponen. Pada akhirnya, sistem bukan lagi sekadar “produk yang keren”, melainkan instrumen ilmiah yang membantu kita menjawab pertanyaan riset dengan jujur dan rigorus.
