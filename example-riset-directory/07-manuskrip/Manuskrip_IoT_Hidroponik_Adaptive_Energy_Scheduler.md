Evaluasi Performa Desain Integrasi IoT Holistik dengan Adaptive Energy
Scheduler Berbasis Panel Surya pada Sistem Hidroponik Cerdas di Kondisi
Fluktuasi Energi Daerah Terpencil

Dysar Adnant Ilham Nur Asnawi1, Helmi Bahar Alim, S.Kom., M.Kom2,

¹Program Studi Ilmu Komputer, Fakultas Sains dan Teknologi, Universitas
Putra Bangsa, Kebumen, Indonesia

email: dysaradnant3@gmail.com1

1.  Abstrak

Pertanian hidroponik di daerah terpencil menghadapi ketergantungan
tinggi pada listrik konvensional, sementara penelitian terdahulu umumnya
menguji integrasi IoT dan panel surya hanya dalam durasi singkat pada
kondisi cahaya yang relatif stabil, sehingga klaim kemandirian energinya
belum teruji terhadap fluktuasi musiman yang nyata. Penelitian ini
mengevaluasi performa desain integrasi IoT holistik dengan Adaptive
Energy Scheduler dan membandingkannya dengan skema baseline rule-based,
menggunakan pendekatan Design Science Research. Simulasi dibangun dari
data meteorologi per jam NASA POWER selama satu tahun penuh (1
Januari--31 Desember 2024, 8.784 titik data) yang diproses melalui model
PV, model beban aktuator (pompa, kipas, lampu LED), dan model baterai
lithium-ion, kemudian dievaluasi melalui lima replikasi untuk setiap
skema penjadwalan. Hasil menunjukkan efisiensi rata-rata skema
rule-based sebesar 39,86% dan skema adaptive sebesar 41,91%, dengan
peningkatan efisiensi rata-rata 2,05% (SD = 0,29%). Uji-t berpasangan
pada seluruh data per-jam menunjukkan perbedaan yang signifikan secara
statistik (t = 30,82; p \< 0,001), tetapi ukuran efek tergolong kecil
(Cohen's d ≈ 0,04) dan magnitudenya berada jauh di bawah ambang
peningkatan 8% yang dihipotesiskan. Analisis lebih lanjut mengungkap
bahwa kondisi "Emergency" muncul pada sekitar 44% dari total waktu
operasi akibat defisit energi tahunan (konsumsi 196,52 kWh berbanding
produksi 177,51 kWh), dengan status pengisian baterai (SOC) rata-rata
50,84% namun berfluktuasi tajam (SD = 32,02). Temuan ini menegaskan
bahwa Adaptive Energy Scheduler secara statistik unggul, namun manfaat
praktisnya terbatas apabila kapasitas panel surya dan baterai tidak
turut disesuaikan dengan kondisi energi yang berfluktuasi sepanjang
tahun --- sebuah nuansa penting yang tidak tertangkap oleh pengujian
jangka pendek pada penelitian-penelitian sebelumnya.

Kata Kunci: IoT; Hidroponik Cerdas; Energi Terbarukan; Adaptive Energy
Scheduler; Efisiensi Energi.

Abstract

Hydroponic farming in remote areas remains heavily dependent on
conventional electricity, while prior studies have generally tested
IoT-solar integration only over short periods under relatively stable
irradiance, leaving claims of energy self-sufficiency largely unverified
against real seasonal fluctuation. This study evaluates the performance
of a holistic IoT design equipped with an Adaptive Energy Scheduler
against a rule-based baseline scheme, following a Design Science
Research approach. The simulation was built from a full year of hourly
NASA POWER meteorological data (1 January--31 December 2024, 8,784 data
points), processed through a PV model, an actuator load model (pump,
fan, LED), and a lithium-ion battery model, and evaluated across five
replicated runs per scheduling scheme. Results show an average
efficiency of 39.86% for the rule-based scheme and 41.91% for the
adaptive scheme, an average improvement of 2.05% (SD = 0.29%). A paired
t-test on the full hourly dataset indicated a statistically significant
difference (t = 30.82; p \< 0.001), yet the effect size was small
(Cohen's d ≈ 0.04) and well below the hypothesized 8% improvement
threshold. Further analysis revealed that an "Emergency" state occurred
in roughly 44% of total operating time due to an annual energy deficit
(196.52 kWh consumed versus 177.51 kWh produced), with an average
battery state of charge (SOC) of 50.84% but high variability (SD =
32.02). These findings indicate that the Adaptive Energy Scheduler is
statistically superior, but its practical benefit is limited unless
solar panel and battery capacity are also resized to match year-round
energy fluctuation --- a nuance that short-duration testing in prior
work fails to capture.

Keywords: Internet of Things; Smart Hydroponics; Renewable Energy;
Adaptive Energy Scheduler; Energy Efficiency.

2.  Pendahuluan

2.1 Latar Belakang

Pertanian merupakan sektor vital dalam pemenuhan kebutuhan pangan yang
terus meningkat seiring pertumbuhan populasi \[1\]. Pertanian hidroponik
menawarkan solusi efisiensi penggunaan lahan dan air, namun sistem
hidroponik cerdas di daerah terpencil masih sangat bergantung pada
listrik PLN yang mahal dan pasokannya tidak stabil, sehingga operasional
sistem kerap terhenti. Integrasi Internet of Things (IoT) dengan panel
surya telah banyak diusulkan sebagai solusi \[2\]--\[4\], namun sebagian
besar penelitian menggunakan logika kontrol statis berbasis threshold
dan hanya diuji dalam waktu singkat pada kondisi lingkungan yang relatif
terkendali, sehingga klaim kemandirian energinya belum teruji terhadap
fluktuasi musiman yang nyata (pemetaan literatur lebih rinci disajikan
pada Bagian 3).

2.2 Rumusan Masalah

Bagaimana performa desain integrasi IoT holistik dengan Adaptive Energy
Scheduler dalam meningkatkan efisiensi penggunaan energi dan kestabilan
operasional sistem hidroponik cerdas berbasis panel surya, dibandingkan
dengan skema baseline rule-based, pada kondisi fluktuasi energi surya
yang merepresentasikan daerah terpencil, dievaluasi melalui simulasi
data meteorologi satu tahun penuh?

Hipotesis nol (H₀) menyatakan tidak terdapat perbedaan signifikan pada
efisiensi penggunaan energi dan kestabilan operasional antara skema
holistik Adaptive Energy Scheduler dan baseline rule-based; hipotesis
alternatif (H₁) menyatakan skema holistik menghasilkan efisiensi energi
minimal 8% lebih tinggi dengan kestabilan operasional yang lebih baik,
pada taraf signifikansi α = 0,05 dan effect size minimal sedang (Cohen's
d ≥ 0,5).

2.3 Tujuan Penelitian

Penelitian ini bertujuan mengembangkan dan mengevaluasi desain integrasi
IoT holistik dengan Adaptive Energy Scheduler berbasis panel surya guna
meningkatkan efisiensi penggunaan energi dan kestabilan operasional
sistem hidroponik cerdas pada kondisi fluktuasi energi di daerah
terpencil, serta menguji secara statistik apakah peningkatan performa
yang dihasilkan bermakna baik secara statistik maupun praktis
dibandingkan baseline rule-based.

2.4 Kontribusi Penelitian

Kontribusi penelitian ini terletak pada tiga hal:

Evaluasi performa Adaptive Energy Scheduler pada cakupan data
meteorologi satu tahun penuh (8.784 titik data per jam), berbeda dari
mayoritas penelitian acuan yang hanya menguji dalam skala mingguan pada
kondisi cuaca yang relatif ideal.

Pelaporan uji signifikansi statistik (paired t-test dan Cohen's d)
secara transparan, termasuk ketika hasil tidak sepenuhnya mendukung
hipotesis penelitian --- sebuah praktik pelaporan yang jarang ditemukan
pada literatur sistem hidroponik-IoT berbasis panel surya.

Identifikasi dan kuantifikasi pola defisit energi musiman (bulanan) pada
sistem berskala kecil (panel 100 Wp, baterai 240 Wh), yang memberikan
dasar empiris bagi rekomendasi sizing kapasitas hardware bagi calon
pengadopsi di daerah terpencil.

3.  Tinjauan Pustaka

3.1 IoT dan Otomasi pada Sistem Hidroponik

Penerapan IoT pada sistem hidroponik telah banyak dieksplorasi untuk
meningkatkan efisiensi pengelolaan lingkungan tanaman. Alam dan Nasuha
\[5\] mengembangkan sistem pengendali pH air dan pemantauan lingkungan
hidroponik berbasis fuzzy logic dan IoT untuk pengendalian kualitas air
secara real-time. Austria dkk. \[6\] merancang sistem rumah kaca pintar
berbasis IoT untuk kebun hidroponik dengan pemantauan multi-parameter
lingkungan tumbuh. Rahutomo dkk. \[7\] mengimplementasikan dan
mensosialisasikan smart farming hidroponik berbasis IoT pada skala
komunitas, melaporkan peningkatan produktivitas dibandingkan metode
konvensional. Ridwan dan Sari \[8\] menerapkan IoT untuk otomatisasi
kontrol suhu, kelembaban, dan tingkat keasaman hidroponik secara
real-time. Pada domain terkait, Adhy dkk. \[10\] mengembangkan sistem
monitoring keamanan berbasis IoT pada green house, menunjukkan perluasan
aplikasi IoT di luar sekadar pemantauan parameter tumbuh tanaman.

Pola umum dari studi-studi ini adalah dominannya penggunaan
mikrokontroler low-cost (Arduino Uno, ESP32/ESP8266) dan platform IoT
sederhana (Blynk), dengan pengujian yang umumnya berlangsung 2--4 minggu
pada skala prototipe kecil dan berfokus pada satu atau dua aspek otomasi
(monitoring atau kontrol tunggal), bukan integrasi holistik seluruh
komponen lingkungan tumbuh.

3.2 Integrasi Energi Terbarukan pada Sistem IoT Pertanian

Untuk mengatasi ketergantungan pada listrik konvensional, sejumlah
penelitian mengintegrasikan panel surya ke dalam sistem IoT pertanian.
Mohammad dkk. \[4\] mengembangkan sistem hidroponik otomatis-modern
berbasis panel surya dan baterai, melaporkan operasional yang stabil
pada skala prototipe laboratorium. Melkysedek dkk. \[3\] merancang
instalasi hidroponik berbasis IoT multisensor dengan sumber energi panel
surya, memungkinkan pemantauan lengkap terhadap kondisi lingkungan
tanaman tanpa ketergantungan listrik PLN. Almalki \[9\] mengusulkan
platform pemantauan pertanian cerdas berbiaya rendah berbasis IoT dan
UAV yang turut mempertimbangkan efisiensi energi pada skala lapangan
yang lebih luas.

Studi paling relevan dengan penelitian ini adalah Wardhana dkk. \[2\],
yang merancang dan menguji prototipe integrasi IoT dalam pertanian
hidroponik cerdas berbasis energi terbarukan --- menggunakan
mikrokontroler Arduino Uno/ESP8266, sensor DHT22, serta panel surya 100
Wp dengan baterai lithium-ion --- dan melaporkan efisiensi penggunaan
energi 69--74% serta operasional 100% berbasis panel surya tanpa
ketergantungan listrik konvensional, dievaluasi pada dua periode
pengujian mingguan (Minggu 1--2 dan Minggu 3--4).

3.3 Sintesis Gap Penelitian

Pemetaan tujuh penelitian relevan (2020--2025) di atas \[2\]--\[8\],
\[10\] menunjukkan dua kesenjangan (gap) utama. Pertama, context gap:
seluruh pengujian pada studi acuan berlangsung pada durasi singkat (2--4
minggu) tanpa mempertimbangkan variasi musiman sepanjang tahun, sehingga
klaim kemandirian energi yang dilaporkan --- termasuk efisiensi 69--74%
pada \[2\] --- belum teruji terhadap kondisi cuaca ekstrem (musim hujan
berkepanjangan, hari mendung berturut-turut) yang relevan bagi konteks
iklim tropis Indonesia. Kedua, method gap: mayoritas studi \[3\]--\[8\],
\[10\] menerapkan integrasi parsial (hanya monitoring atau kontrol
reaktif berbasis ambang batas tetap), dan belum ada yang mengevaluasi
skema penjadwalan energi adaptif-prediktif secara statistik terhadap
baseline rule-based pada cakupan data jangka panjang.

Penelitian ini mengisi kedua celah tersebut dengan mengevaluasi Adaptive
Energy Scheduler pada data meteorologi historis satu tahun penuh,
menggunakan konteks geografis dan spesifikasi hardware yang identik
dengan studi acuan \[2\], sehingga hasilnya dapat dibandingkan secara
langsung (lihat Bagian 5.4).

4.  Metodologi Penelitian

Penelitian ini mengadopsi pendekatan Design Science Research (DSR)
dengan desain eksperimen perbandingan (comparison study) antara dua
skema penjadwalan energi pada model prototipe sistem hidroponik cerdas
berbasis IoT dan panel surya. Evaluasi dilakukan melalui simulasi
berbasis data (data-driven simulation) menggunakan data meteorologi per
jam dari NASA POWER \[11\] untuk titik koordinat 7,55°LS, 109,67°BT ---
identik dengan konteks geografis studi acuan \[2\] --- meliputi radiasi
matahari, suhu udara, kelembaban relatif, dan kecepatan angin, sepanjang
1 Januari hingga 31 Desember 2024 (8.784 baris data per jam).

4.1 Model Sistem

Model Panel Surya (PV): daya keluaran panel dihitung dari radiasi
matahari (dikonversi terhadap kapasitas panel 100 Wp) dan dikoreksi
terhadap suhu menggunakan koefisien temperatur −0,0045/°C relatif
terhadap suhu referensi 25°C.

Model Beban Aktuator: tiga aktuator disimulasikan --- pompa air (18 W),
kipas (12 W), dan lampu LED (24 W) --- masing-masing dengan siklus kerja
(duty cycle) yang ditentukan oleh kondisi lingkungan: pompa mengikuti
tingkat kelembaban, kipas mengikuti suhu udara, dan lampu LED mengikuti
intensitas cahaya matahari.

Model Baterai: kapasitas baterai lithium-ion 240 Wh dengan SOC awal
100%, batas operasi 20--100%, efisiensi pengisian dan pengosongan
masing-masing 95%, serta self-discharge 0,02% per jam. SOC diperbarui
setiap jam berdasarkan selisih antara energi panel surya dan beban
sistem.

4.2 Skema Penjadwalan (Independent Variable)

Kondisi A (Baseline / Rule-Based): menggunakan logika ambang batas tetap
--- status "Emergency" jika SOC \< 30%, "Battery Mode" jika radiasi
matahari \< 250 W/m², "Saving Mode" jika beban melebihi produksi panel
surya, dan "Normal Mode" pada kondisi lainnya, merepresentasikan
pendekatan umum pada \[3\]--\[8\]. Efisiensi dihitung sebagai rasio
energi panel surya terhadap beban (maksimum 100%).

Kondisi B (Treatment / Adaptive Energy Scheduler): menghitung skor
komposit dari empat komponen berbobot --- SOC baterai (bobot 0,40),
ketersediaan radiasi matahari (0,30), tingkat beban sistem (0,20), dan
deviasi suhu dari titik optimal 28°C (0,10). Skor tersebut menentukan
salah satu dari empat mode operasi (Normal Operation, Adaptive Saving,
Priority Pump, Emergency Mode) beserta faktor efisiensi operasionalnya
(0,95 hingga 0,60).

4.3 Prosedur Eksperimen dan Analisis Data

Data diproses berurutan melalui tahap: (1) pembacaan dan validasi
dataset NASA POWER, (2) pembentukan model PV, (3) perhitungan model
beban dan baterai, (4) penerapan skema rule-based dan adaptive secara
paralel pada data identik, dan (5) replikasi sebanyak lima kali dengan
variasi acak ±3% untuk mensimulasikan variabilitas operasional
(pendekatan Monte Carlo sederhana). Kedua skema dievaluasi pada dataset
lingkungan yang identik agar perbedaan hasil dapat diatribusikan pada
perbedaan desain penjadwalan. Analisis data menggunakan statistik
deskriptif, uji-t (paired dan independent sample t-test) pada α = 0,05,
serta Cohen's d untuk mengukur ukuran efek. Seluruh pemrosesan
menggunakan Python (Pandas, SciPy, Matplotlib).

Sebagai catatan metodologis: evaluasi pada tahap ini dilakukan melalui
simulasi berbasis data historis satu tahun penuh, bukan pengujian fisik
langsung terhadap prototipe perangkat keras selama 7 hari × 8 jam
sebagaimana dirancang pada tahap proposal awal. Validasi pada prototipe
fisik direkomendasikan sebagai tahap lanjutan (lihat Bagian 7).

5.  Hasil dan Analisis

5.1 Hasil Evaluasi Keseluruhan

Simulasi dijalankan pada 8.784 titik data per jam sepanjang tahun 2024.
Total energi yang dihasilkan panel surya sepanjang tahun adalah 177,51
kWh, sedangkan total konsumsi energi sistem mencapai 196,52 kWh,
sehingga terjadi defisit energi tahunan sebesar ≈19 kWh (≈10,7% dari
total konsumsi). Kondisi ini secara langsung memengaruhi status baterai,
dengan rata-rata SOC 50,84% namun simpangan baku tinggi (32,02),
menandakan baterai kerap mengalami siklus pengosongan-pengisian yang
dalam (deep cycling).

Tabel 1. Hasil Lima Replikasi Perbandingan Efisiensi Rule-Based vs
Adaptive

Pada tingkat data per-jam (n = 8.784), efisiensi rata-rata skema
rule-based adalah 40,31% (SD = 46,38) dan skema adaptive 42,15% (SD =
47,03). Uji-t berpasangan pada seluruh data menunjukkan perbedaan yang
signifikan secara statistik antara kedua skema (t = 30,82; p \< 0,001),
namun ukuran efek (Cohen's d) hanya sebesar 0,04, tergolong sangat kecil
dan jauh di bawah target sedang (d ≥ 0,5) yang dihipotesiskan.

Tabel 2. Distribusi Mode Keputusan Skema Rule-Based dan Adaptive (n =
8.784 jam)

Gambar 1. Perbandingan Efisiensi Rule-Based vs Adaptive pada Lima
Replikasi

Gambar 2. Energi Panel Surya Dihasilkan vs Energi Dikonsumsi Sistem per
Hari

Gambar 3. Dinamika State of Charge (SOC) Baterai Sepanjang Periode
Simulasi

5.2 Analisis Signifikansi Statistik dan Ukuran Efek

Hasil pengujian menunjukkan bahwa H₀ dapat ditolak secara statistik ---
Adaptive Energy Scheduler menghasilkan efisiensi yang lebih tinggi
secara konsisten dibandingkan rule-based pada seluruh replikasi
(Tabel 1) maupun pada uji per-jam berpasangan. Namun demikian, H₁ hanya
didukung sebagian: peningkatan efisiensi rata-rata (1,84--2,05%) jauh
berada di bawah ambang 8% yang ditetapkan sebagai signifikansi praktis,
dan ukuran efek (Cohen's d ≈ 0,04) tergolong kecil, bukan sedang seperti
yang dihipotesiskan. Signifikansi statistik yang kuat (p \< 0,001) pada
kasus ini sebagian besar didorong oleh ukuran sampel yang sangat besar
(n = 8.784), sehingga signifikansi statistik tidak dapat ditafsirkan
sebagai signifikansi praktis --- sebuah nuansa metodologis penting yang
perlu ditekankan pada evaluasi sistem serupa di masa depan.

5.3 Analisis Defisit Energi dan Distribusi Mode Keputusan

Temuan yang lebih substansial terletak pada tingginya proporsi kondisi
"Emergency" (≈44% dari total waktu operasi) pada kedua skema. Hal ini
mengindikasikan bahwa kapasitas panel surya 100 Wp dan baterai 240 Wh
pada desain saat ini tidak memadai untuk menutupi kebutuhan beban sistem
secara konsisten sepanjang tahun, terutama pada periode dengan radiasi
matahari rendah (musim hujan/berawan).

Perbedaan pola distribusi mode keputusan (Tabel 2) mengindikasikan bahwa
Adaptive Energy Scheduler mengelola sumber daya secara lebih proaktif
dan bertahap: mode "Normal Operation" pada skema adaptive (13,6%) jauh
lebih jarang dibanding "Normal Mode" pada rule-based (29,3%), sementara
mode antara seperti "Priority Pump" dan "Adaptive Saving" menggantikan
sebagian kondisi yang pada rule-based langsung dikategorikan "Normal"
atau "Battery Mode". Fluktuasi SOC yang tinggi (SD = 32,02 dari
rata-rata 50,84%) sebagaimana tervisualisasi pada Gambar 3 juga memiliki
implikasi praktis: siklus pengosongan-pengisian yang dalam dan berulang
berpotensi mempercepat degradasi baterai lithium-ion dalam penggunaan
jangka panjang.

5.4 Perbandingan dengan Jurnal Acuan

Untuk menilai posisi hasil penelitian ini secara objektif, berikut
perbandingan langsung dengan penelitian acuan \[2\] yang menggunakan
arsitektur sistem dan konteks geografis identik.

Tabel 3. Perbandingan Hasil dengan Jurnal Acuan \[2\]

Kesenjangan efisiensi yang besar (69--74% vs 39,86--41,91%) sejalan
dengan perbedaan cakupan durasi pengujian: pengujian mingguan pada \[2\]
kemungkinan besar berlangsung pada kondisi cahaya matahari relatif baik,
sedangkan evaluasi satu tahun penuh pada penelitian ini turut menangkap
periode musim hujan dengan radiasi matahari rendah.

Klaim "operasional 100% berbasis panel surya tanpa ketergantungan
listrik konvensional" pada \[2\] tidak terkonfirmasi pada evaluasi
jangka panjang penelitian ini, yang menemukan defisit energi struktural
pada ≈44% waktu operasi tahunan.

Ketiadaan pelaporan uji statistik pada \[2\] membuat klaim efisiensinya
sulit dinilai signifikansi maupun konsistensinya; penelitian ini
melengkapi celah tersebut dengan pelaporan paired t-test dan Cohen's d
yang transparan, termasuk saat hasilnya tidak sepenuhnya mendukung
hipotesis awal.

6.  Kesimpulan

Penelitian ini berhasil mengevaluasi desain integrasi IoT holistik
dengan Adaptive Energy Scheduler pada sistem hidroponik cerdas berbasis
panel surya, dibandingkan dengan baseline rule-based, menggunakan
simulasi data meteorologi satu tahun penuh. Hasil menunjukkan bahwa
skema adaptive secara statistik signifikan lebih efisien dibandingkan
rule-based (efisiensi rata-rata 41,91% vs 39,86%; p \< 0,001), sehingga
H₀ ditolak. Namun, besaran peningkatan (≈2%) jauh di bawah ambang 8%
yang dihipotesiskan dan ukuran efeknya kecil (Cohen's d ≈ 0,04),
sehingga H₁ hanya didukung secara parsial --- signifikan secara
statistik, tetapi belum bermakna secara praktis pada konfigurasi
hardware saat ini (panel surya 100 Wp, baterai 240 Wh).

Temuan paling signifikan secara praktis adalah tingginya proporsi
kondisi defisit energi ("Emergency" ≈44% dari total waktu operasi)
akibat konsumsi tahunan (196,52 kWh) yang melebihi produksi panel surya
(177,51 kWh), yang mengindikasikan bahwa kapasitas panel dan baterai
perlu diperbesar agar sistem benar-benar mandiri energi sepanjang tahun,
bukan hanya pada periode pengujian singkat dengan cuaca ideal
sebagaimana dilaporkan pada \[2\]. Dengan demikian, penelitian ini
memenuhi tujuannya untuk menghasilkan bukti empiris yang lebih realistis
mengenai performa integrasi IoT holistik dengan energi terbarukan pada
skala tahun penuh, sekaligus mengisi context gap dan method gap yang
diidentifikasi pada Bagian 3.

7.  Saran Penelitian Lanjutan

7.1 Validasi dan Perbaikan Desain

Memvalidasi hasil simulasi ini pada prototipe fisik dengan pengujian
lapangan sesuai rancangan awal (7 hari × 8 jam pengujian aktif, dengan
variasi simulasi cuaca cerah/mendung/hujan secara acak).

Menambah kapasitas panel surya dan/atau baterai, atau mengintegrasikan
sumber energi cadangan (mis. turbin angin skala kecil), untuk mengatasi
periode defisit energi terutama pada bulan-bulan dengan radiasi matahari
rendah.

Mengeksplorasi strategi pengelolaan siklus baterai yang lebih
konservatif untuk mengurangi frekuensi deep-cycling dan memperpanjang
umur pakai baterai.

7.2 Peningkatan Skema Adaptive

Menambahkan komponen prediktif (mis. peramalan radiasi matahari jangka
pendek berbasis machine learning) pada Adaptive Energy Scheduler untuk
meningkatkan margin efisiensi yang saat ini masih tipis.

Menguji bobot skor komposit alternatif melalui optimasi hyperparameter
untuk mengevaluasi apakah kombinasi bobot lain menghasilkan peningkatan
efisiensi yang lebih besar dan mendekati ambang 8% yang dihipotesiskan.

7.3 Perluasan Evaluasi

Mengevaluasi outcome agronomis (pertumbuhan tanaman) secara langsung
untuk melengkapi metrik teknis yang telah dianalisis pada penelitian
ini.

Menggunakan data meteorologi sensor lapangan real-time sebagai
pembanding terhadap data satelit NASA POWER \[11\], guna menilai akurasi
model terhadap kondisi mikro-lokal.

Memperluas analisis ke lokasi geografis lain dengan pola musiman
berbeda, untuk menguji generalisasi temuan defisit energi musiman pada
penelitian ini.

8.  Daftar Pustaka

\[1\] T. Bantacut, Y. R. Firdaus, and M. T. Akbar, "Pengembangan Jagung
untuk Ketahanan Pangan, Industri dan Ekonomi," Jurnal Pangan, vol. 24,
no. 2, pp. 135--148, 2015, doi: 10.33964/jp.v24i2.29.

\[2\] A. S. Wardhana, M. Ferdiansyah, and S. Kholifah K, "Desain dan
Prototipe Integrasi IoT dalam Pertanian Hidroponik Cerdas Berbasis
Energi Terbarukan," Jurnal Indonesia: Manajemen Informatika dan
Komunikasi, vol. 6, no. 1, pp. 105--114, 2025, doi:
10.35870/jimik.v6i1.1134.

\[3\] T. Melkysedek, E. Hesti, and I. Salamah, "Design and Build
Hydroponic Installations and Applications Using IoT-Based Multisensors
with Solar Panel Electrical Energy," Indonesian Journal of Electronics
and Instrumentation Systems, vol. 13, no. 2, p. 123, 2023, doi:
10.22146/ijeis.87906.

\[4\] L. Mohammad, M. K. A. Suyanto, A. Husna, and S. Pakpahan,
"Pengembangan Sistem Hidroponik Otomatis-Modern Berbasis Panel Surya dan
Baterai," Jurnal Nasional Teknologi Elektro dan Teknologi Informasi,
vol. 10, no. 1, pp. 77--84, 2021, doi: 10.22146/jnteti.v10i1.727.

\[5\] R. L. Alam and A. Nasuha, "Sistem Pengendali pH Air dan Pemantauan
Lingkungan Tanaman Hidroponik Menggunakan Fuzzy Logic Berbasis IoT,"
Elinvo (Electronics, Informatics, Vocational Education), vol. 5, no. 1,
pp. 11--20, 2020, doi: 10.21831/elinvo.v5i1.34587.

\[6\] A. C. Austria, J. S. Fabros, K. R. Sumilang, J. Bernardino, and A.
Doctor, "Development of IoT Smart Greenhouse System for Hydroponic
Gardens," International Journal of Computer Science Research, vol. 7,
pp. 2111--2136, 2023, doi: 10.25147/ijcsr.2017.001.1.149.

\[7\] F. Rahutomo, S. Sutrisno, S. Pramono, M. E. Sulistyo, M. H.
Ibrahim, and J. Haryono, "Implementasi dan Sosialisasi Smart Farming
Hidroponik Berbasis Internet of Things di Dusun Ngentak, Bulakrejo,
Sukoharjo," Jurnal Abdi Masyarakat Indonesia, vol. 2, no. 6,
pp. 1961--1970, 2022, doi: 10.54082/jamsi.567.

\[8\] M. Ridwan and K. M. Sari, "Penerapan IoT dalam Sistem Otomatisasi
Kontrol Suhu, Kelembaban, dan Tingkat Keasaman Hidroponik," Jurnal
Teknik Pertanian Lampung, vol. 10, no. 4, p. 481, 2021, doi:
10.23960/jtep-l.v10i4.481-487.

\[9\] F. A. Almalki, "A Low-Cost Platform for Environmental Smart
Farming Monitoring System Based on IoT and UAVs," Sustainability,
vol. 13, no. 11, p. 5908, 2021, doi: 10.3390/su13115908.

\[10\] D. R. Adhy et al., "Sistem Monitoring Keamanan Pada Green House,"
Power Elektronik: Jurnal Orang Elektro, vol. 13, no. 3, pp. 351--357,
2024, doi: 10.30591/polektro.v13i3.7721.

\[11\] NASA Langley Research Center (POWER Project), "NASA POWER Hourly
Data (Solar Irradiance, Temperature, Humidity, Wind Speed), Point 7.55°S
109.67°E," 2024. \[Online\]. Available: https://power.larc.nasa.gov/
