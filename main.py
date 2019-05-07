import os
from zipfile import ZipFile

import re


def get_series_files(directory, serie):
    # initializing empty file paths list 
    file_paths = [] 
  
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(directory): 
        for filename in files: 
            # join the two strings in order to form the full filepath.

            if re.match('{}_'.format(serie), filename):
                filepath = os.path.join(root, filename) 
                file_paths.append((filepath, filename)) 

    # returning all file paths 
    return file_paths 



def write_com_zip_file(serie_files_paths, zip_path):
    file_paths = []

    for root, directories, files in os.walk(os.getcwd()): 
        for filename in files: 
            # join the two strings in order to form the full filepath.

            if filename.lower().find('commercial') != -1:
                filepath = os.path.join(root, filename)
                file_paths.append((filepath, filename))

    com_file_paths = serie_files_paths + file_paths
    print(com_file_paths)

    with ZipFile(zip_path,'w') as zip:
        for (file_path, file_name) in com_file_paths:
            zip.write(file_path, file_name)


def write_per_zip_file(serie_files_paths, zip_path):
    file_paths = []

    for root, directories, files in os.walk(os.getcwd()): 
        for filename in files: 
            # join the two strings in order to form the full filepath.

            if filename.lower().find('personal') != -1:
                filepath = os.path.join(root, filename)
                file_paths.append((filepath, filename))

    per_file_paths = serie_files_paths + file_paths

    with ZipFile(zip_path,'w') as zip:
        for (file_path, file_name) in per_file_paths:
            zip.write(file_path, file_name)



def start_processing():
    # current_path = os.getcwd()
    current_path = 'C:\\'
    zip_base_path = os.path.join(current_path, 'Folder_Zip')

    if not os.path.exists(zip_base_path):
        os.mkdir(zip_base_path)

    for serie in range(1, 10000):
        # Get image file paths of the serie
        serie_files_paths = get_series_files(
            os.path.join(current_path, 'Folder_Out'),
            str(serie),
        )

        if len(serie_files_paths) != 0:
            write_com_zip_file(serie_files_paths, os.path.join(zip_base_path, '{}_COM.zip'.format(str(serie))))
            write_per_zip_file(serie_files_paths, os.path.join(zip_base_path, '{}_PER.zip'.format(str(serie))))



if __name__ == '__main__':
    start_processing()