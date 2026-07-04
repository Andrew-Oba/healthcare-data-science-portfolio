"""
Download the heart disease dataset from Kaggle into data/raw/.

Dataset: Heart Disease Cleveland UCI
Source: https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci
"""

import shutil
from pathlib import Path

import kagglehub

# Kaggle dataset slug
DATASET_SLUG = "cherngs/heart-disease-cleveland-uci"

# Destination folder: 01-heart-disease-eda/data/raw/
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"


def download_dataset():
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset: {DATASET_SLUG}")
    download_path = Path(kagglehub.dataset_download(DATASET_SLUG))
    print(f"Downloaded to cache: {download_path}")

    # Copy all files from the kagglehub cache into our project's data/raw folder
    copied_files = []
    for file in download_path.glob("*"):
        if file.is_file():
            destination = RAW_DATA_DIR / file.name
            shutil.copy2(file, destination)
            copied_files.append(destination)

    print(f"\nCopied {len(copied_files)} file(s) to {RAW_DATA_DIR}:")
    for f in copied_files:
        print(f"  - {f.name}")


if __name__ == "__main__":
    download_dataset()