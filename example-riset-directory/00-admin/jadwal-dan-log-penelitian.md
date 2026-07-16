# Jadwal & Log Pelaksanaan Penelitian

Catatan kronologis pelaksanaan tiap tahap (sumber: riwayat commit git & dokumen `09-docs/tahap-N-*.md`). Tanggal mengikuti `git log`.

## Log Pelaksanaan

| Tanggal | Tahap | Aktivitas | Referensi |
|---|---|---|---|
| 2026-07-07 s.d. 2026-07-09 | Tahap 1 | Identifikasi permasalahan, studi literatur, penyusunan proposal penelitian, perancangan arsitektur sistem Adaptive Energy Scheduler, serta penyusunan research gap dan research question. | [09-docs/tahap-1-perancangan-penelitian.md](../09-docs/tahap-1-perancangan-penelitian.md), [01-proposal/proposal-penelitian.md](../01-proposal/proposal-penelitian.md) |
| 2026-07-10 | Tahap 2 | Pengumpulan dataset NASA POWER tahun 2024, identifikasi variabel penelitian (Solar Radiation, Temperature, Humidity, Wind Speed), serta penyusunan desain eksperimen. | [09-docs/tahap-2-pengumpulan-dataset.md](../09-docs/tahap-2-pengumpulan-dataset.md), [02-literatur/tinjauan-pustaka.md](../02-literatur/tinjauan-pustaka.md) |
| 2026-07-11 s.d. 2026-07-12 | Tahap 3 | Implementasi preprocessing dataset, validasi data (8784 record, tanpa missing value dan duplicate), transformasi variabel, pembangunan PV Model, serta perhitungan energi panel surya. | [09-docs/tahap-3-preprocessing-dan-pv-model.md](../09-docs/tahap-3-preprocessing-dan-pv-model.md), `experiment_final_part1.py` |
| 2026-07-13 s.d. 2026-07-14 | Tahap 4 | Implementasi Energy Demand Model dan Battery Model, perhitungan Pump Load, Fan Load, LED Load, Charge, Discharge, dan State of Charge (SOC). | [09-docs/tahap-4-energy-demand-dan-battery-model.md](../09-docs/tahap-4-energy-demand-dan-battery-model.md), `experiment_final_part2.py` |
| 2026-07-15 | Tahap 5 | Implementasi Rule-Based Scheduler dan Adaptive Energy Scheduler, pengujian awal sistem, serta evaluasi efisiensi penggunaan energi. | [09-docs/tahap-5-adaptive-energy-scheduler.md](../09-docs/tahap-5-adaptive-energy-scheduler.md), `experiment_final_part3.py` |
| 2026-07-16 | Tahap 6 | Pelaksanaan eksperimen sebanyak lima kali (multiple run), analisis statistik (mean, standar deviasi, improvement), serta pembuatan grafik perbandingan Rule-Based dan Adaptive Scheduler. | [09-docs/tahap-6-eksperimen-dan-analisis.md](../09-docs/tahap-6-eksperimen-dan-analisis.md), `experiment_final_part4.py`, `summary_final.xlsx`, `comparison_efficiency.png` |
| 2026-07-16 s.d. 2026-07-17 | Tahap 7 | Penyusunan dokumentasi penelitian, pembaruan laporan WS-09 sampai WS-16, validasi hasil eksperimen, interpretasi hasil, serta penyusunan laporan akhir penelitian. | [09-docs/tahap-7-dokumentasi-dan-pelaporan.md](../09-docs/tahap-7-dokumentasi-dan-pelaporan.md), [08-laporan/laporan-penelitian.md](../08-laporan/laporan-penelitian.md) |

## Status Ringkas

- **Tahap 1**: Selesai. Identifikasi permasalahan, penyusunan proposal penelitian, studi literatur, serta perancangan arsitektur Adaptive Energy Scheduler telah diselesaikan.
- **Tahap 2**: Selesai. Dataset NASA POWER Hourly tahun 2024 berhasil diperoleh, divalidasi, dan digunakan sebagai sumber data penelitian dengan total **8784 record** tanpa missing value maupun duplicate.
- **Tahap 3**: Selesai. Proses preprocessing data dan implementasi **PV Model** berhasil dilakukan. Sistem mampu menghitung Solar Radiation, PV Power, dan PV Energy sebagai dasar simulasi produksi energi panel surya.
- **Tahap 4**: Selesai. Implementasi **Energy Demand Model** dan **Battery Model** berhasil dilakukan, meliputi perhitungan kebutuhan energi pompa, kipas, lampu, Charge, Discharge, dan State of Charge (SOC).
- - **Tahap 5**: Selesai. Implementasi Rule-Based Scheduler dan Adaptive Energy Scheduler berhasil dilakukan. Hasil eksperimen menunjukkan Rule Efficiency sebesar **40,40%** dan Adaptive Efficiency sebesar **42,19%**, sehingga diperoleh peningkatan efisiensi rata-rata sebesar **1,79%**. Hasil ini menjadi baseline untuk pengembangan algoritma adaptif pada penelitian selanjutnya..
- **Tahap 6**: Selesai. Eksperimen sebanyak **5 kali (multiple run)** telah dilaksanakan. Seluruh output berhasil dihasilkan dalam bentuk file CSV, XLSX, serta grafik perbandingan. Analisis statistik menunjukkan **Mean Rule = 40,40%**, **Mean Adaptive = 42,19%**, **Mean Improvement = 1,79%**, **Std Rule = 0,14**, dan **Std Adaptive = 0,07**.
- **Tahap 7**: Selesai. Dokumentasi penelitian telah diperbarui, termasuk penyusunan laporan **WS-09 sampai WS-16**, validasi hasil eksperimen, interpretasi hasil, serta penyusunan laporan penelitian.

### Status Implementasi

| Komponen | Status |
|----------|:------:|
| Proposal Penelitian | ✅ Selesai |
| Studi Literatur | ✅ Selesai |
| Dataset NASA POWER | ✅ Selesai |
| Preprocessing | ✅ Selesai |
| PV Model | ✅ Selesai |
| Energy Demand Model | ✅ Selesai |
| Battery Model | ✅ Selesai |
| Rule-Based Scheduler | ✅ Selesai |
| Adaptive Energy Scheduler | ✅ Selesai |
| Eksperimen (5 Run) | ✅ Selesai |
| Analisis Statistik | ✅ Selesai |
| Visualisasi Hasil | ✅ Selesai |
| Dokumentasi WS-09 s.d. WS-16 | ✅ Selesai |

### Catatan Penelitian

Seluruh tahapan penelitian telah diselesaikan sesuai dengan perencanaan yang dibuat pada proposal. Implementasi berhasil menghasilkan sistem Adaptive Energy Scheduler berbasis panel surya menggunakan dataset NASA POWER tahun 2024 sebanyak 8784 data. Eksperimen dilakukan sebanyak lima kali (multiple run) dan menunjukkan bahwa Adaptive Energy Scheduler memperoleh efisiensi rata-rata sebesar 42,19%, lebih tinggi dibandingkan Rule-Based Scheduler sebesar 40,40%, dengan peningkatan efisiensi rata-rata sebesar 1,79%.

Walaupun peningkatan efisiensi masih relatif kecil, hasil tersebut menunjukkan bahwa pendekatan adaptif memiliki potensi untuk meningkatkan pengelolaan energi pada sistem hidroponik cerdas. Pengembangan algoritma yang lebih kompleks, seperti Fuzzy Logic, Reinforcement Learning, atau Model Predictive Control, dapat menjadi arah penelitian selanjutnya.

## Item Tindak Lanjut (Checklist Sebelum Submission)

- [x] Menyusun proposal penelitian dan memperbarui rumusan masalah, research gap, serta research question sesuai topik Adaptive Energy Scheduler.
- [x] Melakukan studi literatur dan melengkapi referensi ilmiah yang relevan mengenai Smart Farming, IoT, Panel Surya, Battery Management System, dan Adaptive Energy Scheduler.
- [x] Mengunduh, memvalidasi, dan mendokumentasikan dataset NASA POWER Hourly tahun 2024 (8784 record, tanpa missing value dan duplicate).
- [x] Mengimplementasikan preprocessing data, PV Model, Energy Demand Model, Battery Model, Rule-Based Scheduler, dan Adaptive Energy Scheduler.
- [x] Melaksanakan eksperimen sebanyak **5 kali (multiple run)** serta menghasilkan output dalam format CSV, XLSX, dan grafik.
- [x] Melakukan analisis statistik deskriptif (Mean, Standard Deviasi, Improvement) dan mendokumentasikan hasil eksperimen.
- [x] Memperbarui seluruh dokumen **WS-09 sampai WS-16** berdasarkan hasil eksperimen yang telah diperoleh.

### Sebelum Submission

- [ ] Memastikan seluruh sitasi dan daftar pustaka telah sesuai dengan gaya penulisan yang ditentukan dosen (APA/IEEE atau format yang diwajibkan).
- [ ] Memeriksa kembali konsistensi angka pada seluruh dokumen (jumlah data 8784, Rule Efficiency 40,40%, Adaptive Efficiency 42,19%, Improvement 1,79%, Mean, dan Standard Deviasi).
- [ ] Memastikan seluruh gambar, tabel, dan grafik telah diberi nomor, judul, serta sumber yang sesuai.
- [ ] Melakukan pengecekan tata bahasa, ejaan, dan format penulisan pada seluruh dokumen penelitian.
- [ ] Memastikan seluruh file pendukung (dataset, source code, output eksperimen, grafik, dan laporan) tersimpan dengan baik dan dapat dibuka kembali.
- [ ] Melakukan review akhir bersama dosen pembimbing sebelum proses pengumpulan atau seminar hasil.

## Korespondensi

*(belum ada — tambahkan catatan korespondensi dengan pembimbing/editor jurnal di sini saat tersedia)*
