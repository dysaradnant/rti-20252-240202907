import os
import platform
import pandas as pd
from datetime import datetime

def save_metadata(
    dataset_name,
    rows,
    period,
    scheduler,
    output_file
):
    metadata = {
        "Parameter": [
            "Experiment Name",
            "Dataset",
            "Rows",
            "Period",
            "Python Version",
            "Operating System",
            "Execution Time",
            "PV Model",
            "Battery Model",
            "Energy Demand Model",
            "Scheduler",
            "Output File"
        ],
        "Value": [
            "Adaptive Energy Scheduler",
            dataset_name,
            rows,
            period,
            platform.python_version(),
            platform.system(),
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Enabled",
            "Enabled",
            "Enabled",
            scheduler,
            output_file
        ]
    }

    os.makedirs("metadata", exist_ok=True)

    df = pd.DataFrame(metadata)

    df.to_csv(
        "metadata/simulation_metadata.csv",
        index=False
    )

    print("Metadata berhasil disimpan.")