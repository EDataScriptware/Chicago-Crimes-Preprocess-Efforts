import os 
import json

from datetime import datetime
from typing import List
from libraries.common.utils import get_cache_file

def get_all_arrest_types():
    return [
            'THEFT', 'DECEPTIVE PRACTICE', 'SEX OFFENSE', 'BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'OTHER OFFENSE', 'PUBLIC PEACE VIOLATION', 
            'CRIMINAL SEXUAL ASSAULT', 'BURGLARY', 'LIQUOR LAW VIOLATION', 'OFFENSE INVOLVING CHILDREN', 'CRIMINAL TRESPASS', 'WEAPONS VIOLATION', 
            'ROBBERY', 'MOTOR VEHICLE THEFT', 'ASSAULT', 'OBSCENITY', 'INTERFERENCE WITH PUBLIC OFFICER', 'HUMAN TRAFFICKING', 'ARSON', 'GAMBLING', 
            'PROSTITUTION', 'NON-CRIMINAL', 'INTIMIDATION', 'STALKING', 'KIDNAPPING', 'CONCEALED CARRY LICENSE VIOLATION', 'HOMICIDE', 'OTHER NARCOTIC VIOLATION', 
            'RITUALISM', 'PUBLIC INDECENCY', 'NON - CRIMINAL', 'NON-CRIMINAL (SUBJECT SPECIFIED)', 'DOMESTIC VIOLENCE'
        ]

def get_group_by_beat_recs(records: List[dict]):
    print('Started Grouping!')
    cached_file_location = get_cache_file('grouped_data.json')
    start = datetime.now().timestamp()

    if os.path.exists(cached_file_location):
        grouped_data = json.load(open(cached_file_location, 'r'))
        print("Using Cache'd Grouped File")
    else:
        grouped_data = group_by_beat(records)
        json.dump(grouped_data, open(cached_file_location, 'w'))
    end = datetime.now().timestamp()
    print(f'Grouping Data took {end-start} seconds.')


def group_by_beat(records: List[dict]):
    beat_dict = {}
    for rec in records:
        if rec['beat'] not in beat_dict:
            beat_dict[rec['beat']] = {
            'district': rec['district'],
             'data':
                {
                'total_arrest_made': 0,
                'total_domestic_related': 0,
                'arrest_type': {arrest_type: 0 for arrest_type in get_all_arrest_types()}
                }
            }
        subdict = beat_dict[rec['beat']]['data']
        if rec.get('arrest_made'):
            subdict['total_arrest_made'] += 1
        
        if rec.get('domestic_related'):
            subdict['total_domestic_related'] += 1
        
        subdict['arrest_type'][rec['general_charge']] += 1
    return beat_dict

