# LAPORAN PENELITIAN

Evaluasi Performa Desain Integrasi IoT Holistik dengan Adaptive Energy
Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas di Kondisi
Fluktuasi Energi Daerah Terpencil

Dosen Pembimbing: Helmi Bahar Alim, S.Kom., M.Kom.

Peneliti: Dysar Adnant Ilham Nur Asnawi (NIM 240202907)

Program Studi S1 Teknik Informatika

Universitas Putra Bangsa Kebumen

Tahun Akademik 2025/2026

Status Penelitian: Tahap desain skema, simulasi berbasis data, dan
evaluasi statistik telah selesai; naskah artikel ilmiah sedang disusun.

## 1. Ringkasan Eksekutif

Penelitian ini merancang dan mengevaluasi secara empiris performa desain
integrasi IoT holistik dengan Adaptive Energy Scheduler pada sistem
hidroponik cerdas berbasis panel surya, dibandingkan dengan skema
baseline rule-based. Evaluasi dilakukan melalui simulasi berbasis data
meteorologi historis satu tahun penuh (NASA POWER, 1 Januari--31
Desember 2024, 8.784 titik data per jam), yang diproses melalui model
panel surya (PV), model beban aktuator, dan model baterai lithium-ion,
kemudian dievaluasi pada lima replikasi untuk masing-masing skema.

Temuan utama:

Skema Adaptive Energy Scheduler mencapai efisiensi rata-rata 41,91%
dibandingkan 39,86% pada skema rule-based (rata-rata 5 replikasi), yaitu
peningkatan sebesar 2,05% (SD = 0,29%).

Pada tingkat data per jam (n = 8.784), uji-t berpasangan menunjukkan
perbedaan yang signifikan secara statistik antara kedua skema (t =
30,82; p \< 0,001), namun ukuran efek tergolong kecil (Cohen's d ≈ 0,04)
dan jauh di bawah ambang praktis 8% yang dihipotesiskan.

Kondisi "Emergency" (defisit energi kritis) terjadi pada sekitar 44%
dari total waktu operasi tahunan, disebabkan oleh konsumsi energi
tahunan (196,52 kWh) yang melampaui produksi panel surya (177,51 kWh).

Status pengisian baterai (SOC) rata-rata 50,84% dengan variabilitas
tinggi (SD = 32,02), mengindikasikan baterai kerap mengalami siklus
pengosongan-pengisian yang dalam (deep cycling).

Dibandingkan dengan penelitian acuan (Wardhana dkk., 2025) yang
melaporkan efisiensi 69--74% dan operasional 100% berbasis panel surya
tanpa gangguan pada pengujian dua periode singkat, penelitian ini ---
dengan cakupan evaluasi satu tahun penuh --- menemukan performa riil
yang jauh lebih rendah dan defisit energi struktural yang tidak
tertangkap oleh pengujian jangka pendek.

Seluruh skrip simulasi (Python), dataset input (NASA POWER), berkas
hasil (CSV/Excel), dan grafik evaluasi tersedia sebagai artefak
penelitian (lihat Bagian 9 Lampiran).

## 2. Latar Belakang dan Rumusan Masalah

## 2.1 Latar Belakang

Pertanian hidroponik menawarkan efisiensi penggunaan lahan dan air,
namun sistem konvensional masih sangat bergantung pada listrik PLN yang
mahal dan pasokannya tidak stabil di daerah terpencil, sehingga
operasional sistem kerap terhenti. Integrasi Internet of Things (IoT)
dengan panel surya telah banyak diusulkan sebagai solusi (Wardhana dkk.,
2025; Melkysedek dkk., 2023; Mohammad dkk., 2021), namun sebagian besar
penelitian menggunakan logika kontrol statis berbasis threshold dan
hanya diuji dalam waktu singkat (2--4 minggu) pada kondisi lingkungan
yang relatif terkendali, sehingga klaim kemandirian energinya belum
teruji terhadap fluktuasi musiman yang nyata.

Penelitian ini merancang dan mengevaluasi desain integrasi IoT holistik
dengan Adaptive Energy Scheduler --- mekanisme penjadwalan dinamis
aktuator (pompa air, kipas, lampu LED) berdasarkan skor gabungan dari
status pengisian baterai, ketersediaan energi surya, beban sistem, dan
kondisi suhu --- pada data meteorologi historis satu tahun penuh yang
identik dengan konteks geografis pada studi acuan Wardhana dkk. (2025),
untuk memperoleh gambaran performa yang lebih representatif terhadap
variasi musiman.

## 2.2 Rumusan Masalah

Bagaimana performa desain integrasi IoT holistik dengan Adaptive Energy
Scheduler dalam meningkatkan efisiensi penggunaan energi dan kestabilan
operasional sistem hidroponik cerdas berbasis panel surya, dibandingkan
dengan skema baseline rule-based, pada kondisi fluktuasi energi surya
sepanjang tahun yang merepresentasikan daerah terpencil?

## 2.3 Tujuan Penelitian

Penelitian ini bertujuan merancang dan mengevaluasi desain integrasi IoT
holistik dengan Adaptive Energy Scheduler berbasis panel surya, guna
memperoleh bukti empiris mengenai efisiensi penggunaan energi (%),
kestabilan operasional, dan pola defisit energi dibandingkan skema
rule-based, berdasarkan metrik efisiensi energi, status baterai (SOC),
distribusi mode keputusan sistem, serta uji signifikansi statistik
(paired t-test dan Cohen's d).

## 3. Metodologi dan Pelaksanaan

Penelitian dilaksanakan dalam lima tahap menggunakan rangkaian skrip
Python (experiment_final_part1.py hingga experiment_final_part4.py) yang
dijalankan pada lingkungan komputasi lokal, dari penyiapan dataset
meteorologi hingga evaluasi statistik akhir.

## 3.1 Tahap 1 --- Penyiapan Lingkungan dan Dataset

Status: Selesai.

## 3.1.1 Lingkungan Penelitian

Seluruh proses simulasi dan analisis dijalankan pada lingkungan
komputasi lokal berbasis Python, dengan spesifikasi ringkasan sebagai
berikut:

Tabel 1. Spesifikasi Lingkungan Penelitian

## 3.1.2 Library yang Digunakan

Beberapa pustaka (library) Python digunakan pada tahap pemrosesan data
hingga evaluasi, dengan fungsi masing-masing sebagai berikut:

Tabel 2. Library dan Fungsinya

## 3.1.3 Dataset

Dataset meteorologi per jam diunduh dari NASA POWER untuk titik
koordinat 7,55° LS, 109,67° BT, meliputi radiasi matahari
(ALLSKY_SFC_SW_DWN), suhu udara (T2M), kelembaban relatif (RH2M), dan
kecepatan angin (WS10M), mencakup periode 1 Januari hingga 31 Desember
2024 (8.784 baris data per jam). Tidak ditemukan missing value maupun
baris duplikat pada seluruh data setelah proses validasi.

Tabel 3. Ringkasan Statistik Variabel Input per Bulan (Produksi vs
Konsumsi Energi)

Catatan: nilai positif pada kolom "Selisih" menandakan defisit (konsumsi
melebihi produksi); nilai negatif menandakan surplus energi.

## 3.2 Tahap 2 --- Pipeline Pemodelan Sistem

Status: Selesai. Sebelum masuk ke tahap penjadwalan, seluruh data
meteorologi melewati serangkaian tahap pipeline pemrosesan agar dapat
merepresentasikan produksi dan konsumsi energi sistem secara realistis.

Dataset NASA POWER (8.784 baris/jam)

↓

Validasi & Preprocessing (parsing datetime, pengecekan kolom wajib)

↓

Model PV (koreksi suhu → daya panel → energi per jam)

↓

Model Beban Aktuator (pompa, kipas, LED → duty cycle per kondisi
lingkungan)

↓

Model Baterai (charge/discharge → pembaruan SOC per jam)

↓

Scheduler (Rule-Based & Adaptive, dijalankan paralel pada data identik)

↓

Replikasi 5× (variasi acak ±3%) → Statistik & Visualisasi

Gambar 1. Alur Pipeline Pemodelan dan Simulasi

Penjelasan setiap tahap pipeline adalah sebagai berikut:

a.  Validasi & Preprocessing

Data mentah dibaca, kolom wajib (radiasi matahari, suhu, kelembaban,
kecepatan angin) divalidasi keberadaannya, kemudian disusun ulang
berdasarkan urutan waktu (Datetime) hasil kombinasi kolom tahun, bulan,
hari, dan jam.

b.  Model PV

Daya keluaran panel surya (100 Wp) dihitung dari radiasi matahari yang
dikoreksi terhadap suhu menggunakan koefisien temperatur −0,0045/°C
relatif terhadap suhu referensi 25°C, menghasilkan estimasi energi (Wh)
yang dihasilkan setiap jam.

c.  Model Beban Aktuator

Tiga aktuator disimulasikan dengan daya nominal berbeda (pompa 18 W,
kipas 12 W, LED 24 W), masing-masing dengan siklus kerja yang bergantung
pada kondisi lingkungan: pompa mengikuti kelembaban, kipas mengikuti
suhu udara, dan LED mengikuti intensitas cahaya matahari.

d.  Model Baterai

Baterai lithium-ion berkapasitas 240 Wh dimodelkan dengan efisiensi
pengisian dan pengosongan 95%, self-discharge 0,02% per jam, serta batas
operasi SOC 20--100%; nilai SOC diperbarui setiap jam berdasarkan
selisih energi PV dan beban sistem.

e.  Scheduler (Rule-Based & Adaptive)

Kedua skema penjadwalan dijalankan pada data lingkungan yang identik
agar perbedaan hasil dapat diatribusikan pada perbedaan desain logika
kontrol, bukan pada perbedaan kondisi eksternal.

f.  Replikasi

Untuk mensimulasikan variabilitas operasional nyata, seluruh perhitungan
efisiensi direplikasi sebanyak lima kali dengan variasi acak ±3%
(mendekati pendekatan Monte Carlo sederhana), menghasilkan rata-rata dan
simpangan baku per skema.

## 3.3 Tahap 3 --- Pembangunan dan Konfigurasi Skema Penjadwalan

Status: Selesai.

## 3.3.1 Arsitektur Skema Penjadwalan

Dua skema penjadwalan energi dirancang dan dibandingkan sebagai berikut:

Input (SOC, Radiasi Matahari, Beban, Suhu)

↓

Rule-Based: Ambang Batas Tetap \| Adaptive: Skor Komposit Berbobot

↓

Keputusan Mode Operasi (4 kategori per skema)

↓

Perhitungan Efisiensi Energi Tertimbang

Gambar 2. Arsitektur Skema Penjadwalan Energi

Skema Rule-Based menggunakan logika ambang batas tetap: status
"Emergency" jika SOC \< 30%, "Battery Mode" jika radiasi matahari \< 250
W/m², "Saving Mode" jika beban melebihi produksi PV, dan "Normal Mode"
pada kondisi lainnya. Skema Adaptive Energy Scheduler menghitung skor
komposit dari empat komponen berbobot (SOC 40%, radiasi matahari 30%,
beban sistem 20%, deviasi suhu dari 28°C sebesar 10%), yang kemudian
dipetakan ke salah satu dari empat mode operasi beserta faktor
efisiensinya.

## 3.3.2 Ringkasan Parameter Model

Ringkasan parameter dan formula setiap komponen model adalah sebagai
berikut:

Tabel 4. Ringkasan Komponen dan Parameter Model

## 3.3.3 Konfigurasi Parameter Simulasi

Tabel 5. Konfigurasi Parameter Model dan Skema

## 3.4 Tahap 4 --- Eksekusi Simulasi dan Replikasi

Status: Selesai.

## 3.4.1 Parameter Eksekusi

Tabel 6. Parameter Eksekusi Simulasi

## 3.4.2 Hasil per Replikasi

Pelaksanaan simulasi menghasilkan lima berkas hasil individual
(experiment_final_run_1.csv hingga run_5.csv) beserta satu berkas
ringkasan (summary_final.csv) yang merangkum efisiensi rata-rata setiap
replikasi:

Tabel 7. Hasil Lima Replikasi Simulasi

Gambar 3. Perbandingan Efisiensi Rule-Based vs Adaptive pada Lima
Replikasi

## 3.5 Tahap 5 --- Metodologi Evaluasi

Status: Selesai. Evaluasi dilakukan pada seluruh data simulasi (8.784
titik data per jam per replikasi), menggunakan lima bentuk analisis
berikut.

a.  Efisiensi Energi

Efisiensi energi mengukur rasio antara energi yang dihasilkan panel
surya terhadap energi yang dikonsumsi sistem (dengan faktor penyesuaian
mode pada skema adaptive), dibatasi maksimum 100%. Metrik ini merupakan
indikator utama keberlanjutan energi sistem.

b.  Status Pengisian Baterai (SOC)

SOC mengukur persentase kapasitas baterai yang tersisa pada suatu waktu,
mencerminkan kestabilan pasokan energi cadangan serta risiko
deep-cycling yang dapat memengaruhi umur pakai baterai.

c.  Distribusi Mode Keputusan

Proporsi waktu operasi pada setiap mode keputusan (Normal, Saving,
Battery/Priority Pump, Emergency) dihitung untuk kedua skema, guna
menilai seberapa sering sistem berada pada kondisi kritis (Emergency)
dibandingkan kondisi aman (Normal).

d.  Uji Signifikansi Statistik

Perbedaan efisiensi antara skema rule-based dan adaptive diuji
menggunakan paired t-test (pada data per jam yang identik lingkungannya)
dan independent sample t-test, pada taraf signifikansi α = 0,05,
dilengkapi perhitungan Cohen's d untuk mengukur ukuran efek (effect
size) di luar signifikansi statistik semata.

e.  Analisis Defisit Energi Bulanan

Produksi dan konsumsi energi diagregasi per bulan untuk mengidentifikasi
pola musiman defisit/surplus energi sepanjang tahun, sebagai dasar
rekomendasi kapasitas panel dan baterai yang memadai.

## 4. Hasil Penelitian

## 4.1 Hasil Evaluasi Keseluruhan

Tabel 8. Ringkasan Hasil Evaluasi (Data Per Jam, n = 8.784; Data Per
Replikasi, n = 5)

## 4.2 Analisis Efisiensi Energi

Skema Adaptive Energy Scheduler mencapai efisiensi rata-rata 41,91% pada
evaluasi lima replikasi, secara konsisten lebih tinggi dibandingkan
skema rule-based (39,86%) pada seluruh run tanpa terkecuali (Tabel 7,
Gambar 3). Pada tingkat data per jam yang jauh lebih besar (n = 8.784),
pola yang sama terkonfirmasi: efisiensi adaptive (42,15%) lebih tinggi
dibandingkan rule-based (40,31%), dengan perbedaan yang signifikan
secara statistik pada uji-t berpasangan (t = 30,82; p \< 0,001).

Meskipun demikian, ukuran efek (Cohen's d = 0,04) tergolong kecil ---
jauh di bawah ambang efek sedang (d ≥ 0,5) yang dihipotesiskan pada
tahap perancangan penelitian. Signifikansi statistik yang kuat pada
kasus ini sebagian besar didorong oleh ukuran sampel yang sangat besar,
sehingga tidak dapat ditafsirkan sebagai signifikansi praktis.
Peningkatan efisiensi rata-rata 1,84--2,05% jauh berada di bawah ambang
8% yang ditetapkan sebagai signifikansi praktis pada rumusan hipotesis
penelitian.

## 4.3 Analisis Kestabilan Baterai (SOC)

Rata-rata SOC baterai sepanjang simulasi adalah 50,84%, namun dengan
simpangan baku yang tinggi (32,02), mengindikasikan baterai kerap
mengalami siklus pengosongan mendalam hingga mendekati batas minimum
(20%) sebelum kembali terisi penuh, sebagaimana tervisualisasikan pada
Gambar 4. Pola siklus yang dalam dan berulang ini berpotensi mempercepat
degradasi baterai lithium-ion dalam penggunaan jangka panjang.

Gambar 4. Dinamika State of Charge (SOC) Baterai Sepanjang Periode
Simulasi

Gambar 5. Energi Panel Surya Dihasilkan vs Energi Dikonsumsi Sistem per
Hari

## 4.4 Analisis Distribusi Mode Keputusan

Tabel 9. Distribusi Mode Keputusan Skema Rule-Based dan Adaptive (n =
8.784 jam)

Proporsi kondisi "Emergency" yang hampir identik pada kedua skema (44,4%
vs 44,6%) menunjukkan bahwa defisit energi struktural --- akibat
kapasitas panel dan baterai yang tidak memadai untuk beban tahunan ---
tidak dapat sepenuhnya diatasi hanya dengan perubahan logika
penjadwalan, betapapun adaptifnya logika tersebut. Namun demikian, pada
kondisi non-Emergency, skema adaptive mendistribusikan keputusan secara
lebih bertahap (Priority Pump dan Adaptive Saving menggantikan sebagian
keputusan "Normal" pada rule-based), mengindikasikan pendekatan yang
lebih konservatif dalam mengalokasikan energi bahkan pada kondisi yang
oleh rule-based masih dianggap aman.

## 4.5 Analisis Pola Defisit Energi Bulanan

Agregasi bulanan (Tabel 3) mengungkap pola musiman yang jelas: bulan
Agustus, September, dan Oktober menunjukkan surplus energi (produksi PV
melebihi konsumsi), konsisten dengan puncak musim kemarau di Indonesia,
sedangkan sepuluh bulan lainnya --- termasuk Desember dengan defisit
terbesar (+3,59 kWh) --- mengalami defisit energi akibat radiasi
matahari yang lebih rendah pada musim hujan/pancaroba. Pola ini
menjelaskan mengapa kondisi Emergency Mode pada skema adaptive justru
lebih tinggi pada bulan Desember (48,4%) dibandingkan bulan-bulan
surplus seperti Oktober (42,5%).

Temuan ini memperkuat argumen bahwa evaluasi jangka pendek (2--4 minggu)
sebagaimana lazim dilakukan pada penelitian-penelitian acuan berisiko
menangkap hanya periode surplus energi (jika kebetulan dilakukan pada
musim kemarau), sehingga melebih-lebihkan (overestimate) klaim
kemandirian energi sistem apabila diekstrapolasi ke operasional
sepanjang tahun.

## 5. Perbandingan dengan Jurnal Acuan

Untuk menilai posisi hasil penelitian ini secara objektif, berikut
perbandingan langsung dengan penelitian acuan (Wardhana, Ferdiansyah, &
Kholifah K, 2025) yang menggunakan arsitektur sistem dan konteks
geografis yang identik.

Tabel 10. Perbandingan Hasil dengan Jurnal Acuan

Beberapa hal yang dapat diinterpretasikan dari perbandingan ini:

Kesenjangan efisiensi yang besar (69--74% vs 39,86--41,91%) sejalan
dengan perbedaan cakupan durasi pengujian. Pengujian mingguan pada
jurnal acuan kemungkinan besar berlangsung pada kondisi cahaya matahari
yang relatif baik, sedangkan evaluasi satu tahun penuh pada penelitian
ini turut menangkap periode musim hujan dengan radiasi matahari rendah.

Klaim "operasional 100% berbasis panel surya tanpa ketergantungan
listrik konvensional" pada jurnal acuan tidak terkonfirmasi pada
evaluasi jangka panjang penelitian ini, yang justru menemukan defisit
energi struktural pada ≈44% waktu operasi tahunan.

Penambahan skema Adaptive Energy Scheduler pada penelitian ini
memberikan bukti bahwa penjadwalan adaptif dapat meningkatkan efisiensi
secara statistik signifikan, namun tidak cukup untuk mengatasi
keterbatasan kapasitas hardware (panel 100 Wp, baterai 240 Wh) yang
menjadi akar defisit energi.

Ketiadaan pelaporan uji statistik pada jurnal acuan membuat klaim
efisiensinya sulit dinilai signifikansi maupun konsistensinya;
penelitian ini melengkapi celah tersebut dengan pelaporan paired t-test
dan Cohen's d yang transparan, termasuk saat hasilnya tidak sepenuhnya
mendukung hipotesis awal.

## 6. Keterbatasan Penelitian

Beberapa keterbatasan berikut perlu menjadi catatan dalam
menginterpretasikan hasil penelitian ini:

a.  Simulasi, Bukan Pengujian Prototipe Fisik

Evaluasi pada tahap ini dilakukan melalui simulasi berbasis data
historis, bukan pengujian langsung terhadap prototipe perangkat keras
selama 7 hari × 8 jam sebagaimana dirancang pada tahap proposal awal.
Perilaku komponen fisik nyata (efisiensi aktual panel, respons aktuator,
noise sensor) belum tervalidasi.

b.  Data Meteorologi Historis, Bukan Sensor Real-Time

Data radiasi matahari, suhu, dan kelembaban bersumber dari data
satelit/reanalisis NASA POWER, bukan hasil pengukuran sensor lapangan
(DHT22, LDR) secara langsung, sehingga tidak menangkap variasi
mikro-lokal (naungan, debu pada panel, dsb.).

c.  Model Beban yang Disederhanakan

Duty cycle aktuator (pompa, kipas, LED) dihitung menggunakan aturan
heuristik berbasis ambang batas tunggal, bukan hasil kalibrasi terhadap
perangkat keras nyata, sehingga estimasi beban aktual dapat berbeda dari
kondisi lapangan.

d.  Ukuran Efek Kecil

Meskipun perbedaan efisiensi antar-skema signifikan secara statistik,
ukuran efeknya kecil (Cohen's d ≈ 0,04) dan jauh di bawah target praktis
(8%) yang dihipotesiskan, sehingga manfaat adaptive scheduler pada
konfigurasi hardware saat ini masih terbatas.

e.  Replikasi Berbasis Noise Acak, Bukan Variasi Kondisi Nyata

Kelima replikasi menggunakan variasi acak ±3% sebagai proksi
variabilitas operasional, bukan variasi kondisi eksperimen nyata (mis.
penempatan panel, orientasi, atau kondisi cuaca aktual yang berbeda),
sehingga estimasi variansi hasil bersifat konservatif.

f.  Belum Ada Evaluasi Outcome Agronomis

Penelitian ini berfokus pada metrik teknis (efisiensi energi, SOC, mode
keputusan) dan belum mengevaluasi dampaknya terhadap pertumbuhan tanaman
secara langsung, sebagaimana direncanakan sebagai secondary outcome pada
tahap proposal.

## 7. Saran untuk Penelitian Lanjutan

## 7.1 Validasi dan Perbaikan Desain

Memvalidasi hasil simulasi ini pada prototipe fisik dengan pengujian
lapangan sesuai rancangan awal (7 hari × 8 jam pengujian aktif, dengan
variasi simulasi cuaca cerah/mendung/hujan secara acak).

Menambah kapasitas panel surya dan/atau baterai, atau mengintegrasikan
sumber energi cadangan (mis. turbin angin skala kecil), untuk mengatasi
periode defisit energi terutama pada bulan November--Juni.

Mengeksplorasi strategi pengelolaan siklus baterai yang lebih
konservatif untuk mengurangi frekuensi deep-cycling dan memperpanjang
umur pakai baterai.

## 7.2 Peningkatan Skema Adaptive

Menambahkan komponen prediktif (mis. peramalan radiasi matahari jangka
pendek berbasis machine learning) pada Adaptive Energy Scheduler untuk
meningkatkan margin efisiensi yang saat ini masih tipis.

Menguji bobot skor komposit alternatif (selain 0,40/0,30/0,20/0,10)
melalui optimasi hyperparameter untuk mengevaluasi apakah kombinasi
bobot lain menghasilkan peningkatan efisiensi yang lebih besar.

## 7.3 Perluasan Evaluasi

Mengevaluasi outcome agronomis (pertumbuhan tanaman) secara langsung
untuk melengkapi metrik teknis yang telah dianalisis.

Menggunakan data meteorologi sensor lapangan real-time sebagai
pembanding terhadap data satelit NASA POWER, guna menilai akurasi model
terhadap kondisi mikro-lokal.

Memperluas analisis ke lokasi geografis lain dengan pola musiman
berbeda, untuk menguji generalisasi temuan defisit energi musiman pada
penelitian ini.

## 8. Kesimpulan

Penelitian ini berhasil merancang dan mengevaluasi desain integrasi IoT
holistik dengan Adaptive Energy Scheduler pada sistem hidroponik cerdas
berbasis panel surya, menggunakan simulasi data meteorologi satu tahun
penuh (8.784 titik data per jam) dan lima replikasi evaluasi. Hasil
menunjukkan bahwa skema adaptive secara statistik signifikan lebih
efisien dibandingkan rule-based (41,91% vs 39,86%; p \< 0,001), sehingga
hipotesis nol (H₀) dapat ditolak. Namun, besaran peningkatan (≈2%) jauh
di bawah ambang 8% yang dihipotesiskan dan ukuran efeknya kecil (Cohen's
d ≈ 0,04), sehingga hipotesis alternatif (H₁) hanya didukung secara
parsial --- signifikan secara statistik, tetapi belum bermakna secara
praktis pada konfigurasi hardware saat ini (panel surya 100 Wp, baterai
240 Wh).

Temuan paling signifikan secara praktis adalah tingginya proporsi
kondisi defisit energi ("Emergency" ≈44% dari total waktu operasi)
akibat konsumsi tahunan (196,52 kWh) yang melebihi produksi panel surya
(177,51 kWh), dengan pola musiman yang jelas --- surplus pada
Agustus--Oktober dan defisit pada bulan-bulan lainnya. Dibandingkan
dengan penelitian acuan yang melaporkan efisiensi 69--74% dan
operasional 100% berbasis panel surya pada pengujian jangka pendek,
penelitian ini menemukan bahwa klaim kemandirian energi tersebut tidak
bertahan pada evaluasi skala tahun penuh, sehingga kapasitas panel dan
baterai perlu diperbesar agar sistem benar-benar mandiri energi
sepanjang tahun.

Kontribusi utama penelitian ini bukan pada pembuktian keunggulan besar
Adaptive Energy Scheduler, melainkan pada penyediaan bukti empiris yang
lebih realistis mengenai batas kemampuan integrasi IoT-panel surya skala
kecil di bawah variasi energi tahunan --- sebuah kontribusi yang relevan
bagi calon pengadopsi teknologi di daerah terpencil agar
mempertimbangkan sizing kapasitas panel dan baterai yang memadai, bukan
hanya mengandalkan klaim dari pengujian jangka pendek.

## 9. Lampiran --- Artefak Penelitian

## 9.1 Peta Artefak

Tabel 11. Peta Artefak Penelitian

## 9.2 Research Summary

Tabel 12. Research Summary

Catatan: seluruh berkas kode dan hasil (CSV/Excel/PNG) berukuran total
±22 MB, tersedia lengkap sebagai satu paket artefak penelitian yang
dapat diunggah ke penyimpanan cloud (mis. Google Drive) dan dicantumkan
tautannya pada laporan akhir apabila diperlukan.
