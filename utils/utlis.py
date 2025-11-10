import configparser
import pandas as pd
import os

def get_cols_name(col_name: str):
    config = configparser.ConfigParser(interpolation=None)
    config.read("utils/cols.conf")  # fixed path

    cols = [c.strip() for c in config.get(col_name, "columns").split(",")]
    return cols


def change_dtype(df, dtype):
    df['Umsatz IST'] = (
        df['Umsatz IST']
        .str.replace('.', '', regex=False)
        .replace('', '0')
        .astype(dtype)
    )
    return df


print(get_cols_name("Bestellte_Langsamdreher_Vortag"))
