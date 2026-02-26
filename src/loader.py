import pandas as pd
from pathlib import Path


def load_all_csv(data_path: str):
    """
    data/raw 폴더 안의 모든 CSV를 읽어서 하나의 DataFrame으로 병합
    """
    data_dir = Path(data_path)
    csv_files = list(data_dir.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError("No CSV files found in data directory.")

    df_list = []

    for file in csv_files:
        df = pd.read_csv(file)
        df["source_file"] = file.name
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    return combined_df
