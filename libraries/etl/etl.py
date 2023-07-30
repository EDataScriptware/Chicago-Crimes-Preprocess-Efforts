from libraries.etl.extract import extract_file
from libraries.etl.transform import transform
from libraries.etl.load import load
from libraries.common.utils import get_cache_file, get_external_file

import os
import json

from datetime import datetime
from pandas import read_csv

def extract_transform_load(input_file_name: str, export_file_name: str):
    opened_file = extract_file(input_file_name)
    print('Extracted')
    df = transform(opened_file)
    print('Transformed')
    data = load(df, export_file_name)
    print('Loaded')
    return data


def get_data():
    # .CSV file was obtained from https://catalog.data.gov/dataset/crimes-2001-to-present
    # Crimes 2001 - to Present for Chicago, IL.
    file_name = 'Crimes_-_2001_to_Present'
    cached_file_location = get_cache_file(f'{file_name}.json') 

    start = datetime.now().timestamp()
    if os.path.exists(cached_file_location):
        print("Using Cache'd Extract File")
        data = json.load(open(cached_file_location, 'r'))
    else:
        data = extract_transform_load(get_external_file(f'{file_name}.csv'), cached_file_location)
    
    end = datetime.now().timestamp()
    print(f'ETL took {end-start} seconds.')
    return data

def get_IUCR_codes_mapping():
    file_name = 'Chicago_Police_Department_-_Illinois_Uniform_Crime_Reporting__IUCR__Codes.csv'
    cached_file_location = get_cache_file('IUCR_mapping.json')

    if not os.path.exists(cached_file_location):
        data = read_csv(open(get_external_file({file_name}), 'r')).to_dict('records')
        json.dump(data, open(cached_file_location, 'w'))
    else:
        print("Using Cache'd IUCR File")
        data = json.load(open(cached_file_location, 'r'))
    
    preprocessed_IUCR_mapping = {
            d['IUCR'].zfill(4): {
            'primary': d['PRIMARY DESCRIPTION'], 
            'secondary': d['SECONDARY DESCRIPTION']
            } for d in data
        }

    json.dump(preprocessed_IUCR_mapping, open(get_cache_file('preprocessed_IUCR_mapping.json'), 'w'))
    return preprocessed_IUCR_mapping