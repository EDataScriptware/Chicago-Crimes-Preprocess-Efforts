from __init__ import PROJECT_DIRECTORY, CACHE_DIRECTORY, EXTERNAL_DIRECTORY

def get_external_file(file_name: str):
    dir = f'{PROJECT_DIRECTORY}{EXTERNAL_DIRECTORY}{file_name}'
    dir.replace('//', '/')
    return dir

def get_cache_file(file_name: str):
    dir = f'{PROJECT_DIRECTORY}{CACHE_DIRECTORY}{file_name}'
    dir.replace('//', '/')
    return dir
