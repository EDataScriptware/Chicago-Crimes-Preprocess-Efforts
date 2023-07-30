## Authored by Edward Riley
## 

import os 
import json

from libraries.common.utils import get_cache_file, dict_to_csv

from libraries.etl.etl import get_data
from libraries.preprocess import get_preprocessed_data
from libraries.group import get_group_by_beat_recs


# We want to retrieve the data in a dictionary format 
# so it is easier to perform data preprocess


if not os.path.exists(get_cache_file('preprocessed_data.json')):
    records = get_data()
else:
    records = []
    print('Extract is skipped due to preprocess_data.json already exists.')

# Let's clean up the works and take only what we need.
if not os.path.exists(get_cache_file('grouped_data.json')):
    preprocessed_records = get_preprocessed_data(records)
    # Generate Human Readable File to view easily
    # dict_to_csv(preprocessed_records, get_cache_file('preprocessed.csv'))

    grouped_data = get_group_by_beat_recs(preprocessed_records)
else:
    grouped_data = json.load(open(get_cache_file('grouped_data.json')))



# Because there is no numerical value that we can perform the 
# batch normalization or dropout normalization techniques. 
# We must group them by __beat__ and collect numerical datatypes.

