import json

import pandas as pd


def write_json(data: list[dict], filename: str):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def write_parquet(data: list[dict], filename: str):
    df = pd.DataFrame(data)
    df.to_parquet(filename, index=False)

def gather_data_by_date(data: list[dict], date_key: str):
    grouped_data = {}
    print(f'Gathering data by {date_key}')
    for item in data:
        if date_key in item:
            # Convert date to a consistent format
            date_str = pd.to_datetime(item[date_key]).strftime('%Y-%m-%d')
            grouped_data.setdefault(date_str, []).append(item)
    return grouped_data

def write_json_by_date(data: list[dict], date_key: str, filename_prefix: str):
    grouped_data = gather_data_by_date(data, date_key)

    for date, records in grouped_data.items():
        filename = f"{filename_prefix}_{date}.json"
        print(f'Saving {filename}')
        write_json(records, filename)

def write_parquet_by_date(data: list[dict], date_key: str, filename_prefix: str):
    grouped_data = gather_data_by_date(data, date_key)

    for date, records in grouped_data.items():
        filename = f"{filename_prefix}_{date}.parquet"
        print(f'Saving {filename}')
        write_parquet(records, filename)
