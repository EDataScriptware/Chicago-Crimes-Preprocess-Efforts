from __init__ import PROJECT_DIRECTORY, CACHE_DIRECTORY, EXTERNAL_DIRECTORY
import pandas 

def get_external_file(file_name: str):
    dir = f'{PROJECT_DIRECTORY}{EXTERNAL_DIRECTORY}{file_name}'
    dir.replace('//', '/')
    return dir

def get_cache_file(file_name: str):
    dir = f'{PROJECT_DIRECTORY}{CACHE_DIRECTORY}{file_name}'
    dir.replace('//', '/')
    return dir


def dict_to_csv(data: dict, file_location: str):
    df = pandas.DataFrame.from_dict(data)
    df.to_csv(file_location)