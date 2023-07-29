from pandas import DataFrame
import json

def load(df: DataFrame, file_location: str):
    """
        Return as a list of dictionary datatype.
    """
    data_to_load = df.to_dict('records')
    json.dump(data_to_load, open(file_location, 'w'))
    return data_to_load