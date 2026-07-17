
"""
experiment_final.py - Bagian 1
Tahap:
1. Konfigurasi
2. Logging
3. Membaca Dataset NASA POWER
4. Validasi Dataset
5. Preprocessing
6. PV Model

Bagian berikutnya akan menambahkan:
- Energy Demand Model
- Battery Model
- Scheduler
"""

import logging
import os
from pathlib import Path
import pandas as pd

# ==========================
# KONFIGURASI
# ==========================
DATASET = "dataset/POWER_Point_Hourly_20240101_20241231_007d55S_109d67E_LST.csv"

PANEL_RATED_POWER = 100.0      # Wp
TEMP_REFERENCE = 25.0          # °C
TEMP_COEFFICIENT = 0.0045      # /°C

OUTPUT_DIR = Path("output")
LOG_DIR = Path("logs")

OUTPUT_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "experiment_final.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# ==========================
# LOAD DATASET
# ==========================
def load_dataset(path: str) -> pd.DataFrame:
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()

    header = None
    for i, line in enumerate(lines):
        if line.startswith("YEAR"):
            header = i
            break

    if header is None:
        raise RuntimeError("Header YEAR tidak ditemukan.")

    df = pd.read_csv(path, skiprows=header)
    logging.info("Dataset berhasil dibaca.")
    return df

# ==========================
# VALIDASI
# ==========================
def validate(df: pd.DataFrame):
    required = [
        "YEAR","MO","DY","HR",
        "ALLSKY_SFC_SW_DWN",
        "T2M","RH2M","WS10M"
    ]

    missing = [c for c in required if c not in df.columns]
    if missing:
        raise RuntimeError(f"Kolom tidak ditemukan: {missing}")

    print("=== VALIDASI DATASET ===")
    print("Jumlah baris :", len(df))
    print("Missing value :", int(df[required].isna().sum().sum()))
    print("Duplicate :", int(df.duplicated().sum()))
    print("========================")

# ==========================
# PREPROCESSING
# ==========================
def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = df[[
        "YEAR","MO","DY","HR",
        "ALLSKY_SFC_SW_DWN",
        "T2M","RH2M","WS10M"
    ]]

    df.rename(columns={
        "ALLSKY_SFC_SW_DWN":"Solar",
        "T2M":"Temperature",
        "RH2M":"Humidity",
        "WS10M":"Wind"
    }, inplace=True)

    df["Datetime"] = pd.to_datetime(dict(
        year=df["YEAR"],
        month=df["MO"],
        day=df["DY"],
        hour=df["HR"]
    ))

    df = df.sort_values("Datetime").reset_index(drop=True)

    return df

# ==========================
# PV MODEL
# ==========================
def pv_model(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Koreksi temperatur
    df["TempCorrection"] = (
        1 - TEMP_COEFFICIENT * (df["Temperature"] - TEMP_REFERENCE)
    ).clip(lower=0)

    # Daya panel
    df["PV_Power_W"] = (
        PANEL_RATED_POWER *
        (df["Solar"] / 1000.0) *
        df["TempCorrection"]
    )

    # Energi per jam
    df["PV_Energy_Wh"] = df["PV_Power_W"]

    return df

# ==========================
# SIMPAN
# ==========================
def save(df: pd.DataFrame):
    csv_path = OUTPUT_DIR / "experiment_part1.csv"
    xlsx_path = OUTPUT_DIR / "experiment_part1.xlsx"

    df.to_csv(csv_path, index=False)
    df.to_excel(xlsx_path, index=False)

    print(f"Hasil CSV  : {csv_path}")
    print(f"Hasil XLSX : {xlsx_path}")

# ==========================
# SUMMARY
# ==========================
def summary(df: pd.DataFrame):
    print("\n===== RINGKASAN =====")
    print("Periode :", df["Datetime"].min(), "s/d", df["Datetime"].max())
    print("Solar rata-rata :", round(df["Solar"].mean(),2))
    print("PV Power rata-rata :", round(df["PV_Power_W"].mean(),2),"W")
    print("PV Energy total :", round(df["PV_Energy_Wh"].sum(),2),"Wh")
    print("=====================")

# ==========================
# MAIN
# ==========================
def main():
    print("Membaca dataset NASA POWER...")
    df = load_dataset(DATASET)

    validate(df)

    print("Preprocessing...")
    df = preprocess(df)

    print("Menjalankan PV Model...")
    df = pv_model(df)

    save(df)

    summary(df)

    print("\nBagian 1 selesai.")
    print("Lanjutkan ke Bagian 2: Energy Demand Model & Battery Model.")

if __name__ == "__main__":
    main()
