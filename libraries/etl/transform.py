from pandas import read_csv, DataFrame

def transform(file_data: str) -> DataFrame:
    """
        Transform to DataFrame
    """
    df = read_csv(file_data)
    return df