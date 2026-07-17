# 06 - Output

Folder ini berisi seluruh hasil simulasi, analisis, dan visualisasi yang dihasilkan dari implementasi **Adaptive Energy Scheduler** berbasis panel surya pada sistem hidroponik cerdas.

Seluruh file pada folder ini dihasilkan secara otomatis setelah menjalankan tahapan eksperimen yang terdapat pada folder `05-kode`.

---

# Struktur Folder

```text
06-output/
│
├── csv/
├── excel/
├── graph/
└── README.md
```

---

# csv/

Berisi hasil simulasi dalam format **CSV**.

| File | Deskripsi |
|------|-----------|
| experiment_part1.csv | Hasil preprocessing dataset dan perhitungan PV Model. |
| experiment_part2.csv | Hasil simulasi Battery Model dan Energy Demand Model. |
| experiment_part3.csv | Hasil simulasi Adaptive Energy Scheduler. |
| experiment_final_run_1.csv | Hasil simulasi run ke-1. |
| experiment_final_run_2.csv | Hasil simulasi run ke-2. |
| experiment_final_run_3.csv | Hasil simulasi run ke-3. |
| experiment_final_run_4.csv | Hasil simulasi run ke-4. |
| experiment_final_run_5.csv | Hasil simulasi run ke-5. |
| summary_final.csv | Ringkasan hasil seluruh eksperimen. |

---

# excel/

Berisi hasil simulasi dalam format Microsoft Excel.

| File | Deskripsi |
|------|-----------|
| experiment_part1.xlsx | Hasil preprocessing dan PV Model. |
| experiment_part2.xlsx | Hasil Battery Model dan Energy Demand Model. |
| experiment_part3.xlsx | Hasil Adaptive Energy Scheduler. |
| summary_final.xlsx | Ringkasan hasil eksperimen dalam format Excel. |

---

# graph/

Berisi visualisasi hasil penelitian.

| File | Deskripsi |
|------|-----------|
| comparison_efficiency.png | Perbandingan efisiensi Rule-Based Scheduler dan Adaptive Energy Scheduler pada setiap simulasi. |

---

# Ringkasan Hasil

Berdasarkan lima kali simulasi, diperoleh hasil sebagai berikut.

| Parameter | Nilai |
|-----------|-------:|
| Mean Rule Efficiency | 39.86 % |
| Mean Adaptive Efficiency | 41.91 % |
| Mean Improvement | 2.05 % |
| Average SOC | 50.78 % |

Hasil tersebut menunjukkan bahwa **Adaptive Energy Scheduler** memberikan peningkatan efisiensi dibandingkan metode Rule-Based Scheduler pada skenario simulasi yang digunakan.

---

# Cara Menghasilkan Output

Seluruh file pada folder ini dihasilkan secara otomatis dengan menjalankan tahapan eksperimen berikut.

```bash
python experiment_final_part1.py
python experiment_final_part2.py
python experiment_final_part3.py
python experiment_final_part4.py
```

---

# Acuan

- `../04-data/` — Dataset dan data hasil preprocessing.
- `../05-kode/` — Source code implementasi penelitian.
- `../09-docs/` — Dokumentasi metodologi dan analisis penelitian.
