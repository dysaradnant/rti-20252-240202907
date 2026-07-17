# 05 - Kode

Folder ini berisi seluruh source code yang digunakan untuk mengimplementasikan simulasi **Adaptive Energy Scheduler** berbasis panel surya pada sistem hidroponik cerdas.

Implementasi dikembangkan menggunakan bahasa pemrograman **Python** dan dibagi menjadi beberapa tahapan eksperimen, mulai dari preprocessing data hingga evaluasi performa sistem.

---

# Struktur Folder

```text
05-kode/
│
├── experiment/
│   ├── experiment_final_part1.py
│   ├── experiment_final_part2.py
│   ├── experiment_final_part3.py
│   └── experiment_final_part4.py
│
├── model/
│   └── metadata.py
│
├── config/
│
└── requirements.txt
```

---

# Deskripsi Folder

## experiment/

Berisi seluruh tahapan eksperimen penelitian.

| File | Deskripsi |
|------|-----------|
| experiment_final_part1.py | Melakukan preprocessing dataset dan perhitungan produksi energi panel surya (PV Model). |
| experiment_final_part2.py | Mengimplementasikan Battery Model dan Energy Demand Model. |
| experiment_final_part3.py | Mengimplementasikan Adaptive Energy Scheduler dan membandingkannya dengan Rule-Based Scheduler. |
| experiment_final_part4.py | Melakukan multiple run, analisis statistik, visualisasi hasil, dan menghasilkan metadata eksperimen. |

---

## model/

Berisi modul pendukung yang digunakan oleh eksperimen.

| File | Deskripsi |
|------|-----------|
| metadata.py | Membuat file `simulation_metadata.csv` secara otomatis setelah eksperimen selesai dijalankan. |

---

## config/

Berisi file konfigurasi yang digunakan selama proses simulasi (jika ada).

---

# Dependensi

Library yang digunakan pada penelitian ini tercantum pada file:

```text
requirements.txt
```

Instal seluruh dependensi menggunakan perintah berikut:

```bash
pip install -r requirements.txt
```

---

# Urutan Menjalankan Program

Jalankan setiap tahapan eksperimen secara berurutan:

```bash
python experiment_final_part1.py
```

```bash
python experiment_final_part2.py
```

```bash
python experiment_final_part3.py
```

```bash
python experiment_final_part4.py
```

---

# Output

Hasil eksekusi akan menghasilkan:

- Data hasil preprocessing
- Data simulasi Battery Model
- Data Adaptive Energy Scheduler
- Ringkasan hasil eksperimen
- Grafik evaluasi
- Metadata eksperimen

Output tersebut akan disimpan pada folder:

- `../04-data/`
- `../06-output/`

---

# Acuan

- `../03-teori/` — Landasan teori penelitian.
- `../04-data/` — Dataset dan data hasil preprocessing.
- `../06-output/` — Hasil simulasi dan grafik evaluasi.
- `../09-docs/` — Dokumentasi teknis penelitian.
