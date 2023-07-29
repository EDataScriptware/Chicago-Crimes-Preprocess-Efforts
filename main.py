## Authored by Edward Riley
## 

import os 

from libraries.common.utils import get_cache_file

from libraries.etl.etl import get_data
from libraries.preprocess import get_preprocessed_data



# We want to retrieve the data in a dictionary format 
# so it is easier to perform data preprocess


if not os.path.exists(get_cache_file('preprocessed_data.json')):
    records = get_data()
else:
    records = []
    print('Extract is skipped due to preprocess_data.json already exists.')

preprocessed_records = get_preprocessed_data(records)
