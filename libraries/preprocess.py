import json
import os

from math import isnan
from typing import List
from datetime import datetime

from libraries.etl.etl import get_IUCR_codes_mapping
from libraries.common.utils import get_cache_file

DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'
IUCR_MAPPING = get_IUCR_codes_mapping()


def get_preprocessed_data(original_recs: List[dict]) -> List[dict]:
    print('Started Preprocessing Data')
    file_name = 'preprocessed_data.json'
    cached_file_location = get_cache_file(file_name)

    start = datetime.now().timestamp()
    if os.path.exists(cached_file_location):
        preprocessed_records = json.load(open(cached_file_location, 'r'))
        print("Using Cache'd PreProccess File")
    else:
        preprocessed_records = preprocess_data(original_recs)
        json.dump(preprocessed_records, open(cached_file_location, 'w'))
    end = datetime.now().timestamp()
    print(f'Preprocess took {end-start} seconds.')

    return preprocessed_records


def preprocess_data(original_recs):
    pre_processed_recs = []
    for og_rec in original_recs:
        preprocess_rec = preprocess_data_record(og_rec) 
        if preprocess_rec:
            pre_processed_recs.append(preprocess_rec)
    return pre_processed_recs

def preprocess_data_record(rec: dict):
    if not IUCR_MAPPING.get(rec['IUCR']):
        primary_charge = rec['Primary Type']
        secondary_charge = rec['Description']
    else:
        primary_charge = IUCR_MAPPING[rec['IUCR']]['primary']
        secondary_charge = IUCR_MAPPING[rec['IUCR']]['secondary']

    if isnan(rec['District']) or isnan(rec['Beat']):
        return {}

    return {
        'id': f"{rec['ID']}_{rec['Case Number']}",
        'date': datetime.strptime(rec['Date'], DATE_FORMAT).strftime('%Y-%m-%d'),
        'address': rec['Block'],
        'location_type': rec['Location Description'],
        'general_charge': primary_charge,
        'detailed_charge': secondary_charge,
        'arrest_made': rec['Arrest'],
        'domestic_related': rec['Domestic'],
        'district': int(float(rec['District'])),
        'beat': int(float(rec['Beat']))
    }
