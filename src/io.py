from paths import RAW_DATA_DIR, IMPORTED_DATA_DIR
import pandas as pd

workbook = pd.ExcelFile(RAW_DATA_DIR / "online_retail_II.xlsx")

sheets = [
    workbook.parse(sheet_name=sheet) for sheet in workbook.sheet_names
]

dataset = pd.concat(sheets, ignore_index=True)

dataset["Invoice"] = dataset["Invoice"].astype("string")
dataset["StockCode"] = dataset["StockCode"].astype("string")
dataset["Description"] = dataset["Description"].astype("string")

dataset.to_parquet(IMPORTED_DATA_DIR / "online_retail_II.parquet")