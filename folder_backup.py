#! python3
"""
folder_backup.py - Copies an entire folder and its contents into a zip file whose filename increments
"""
import zipfile
import os


def backup_to_zip(folder):
    """
    Backup the entire contents of 'folder' into a zip file
    :param folder: 
    :return: 
    """
    folder = os.path.abspath(folder)  # make sure folder is absolute

    # figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zip_filename = "{}_{}{}".format(os.path.basename(folder), str(number), ".zip")
        if not os.path.exists(zip_filename):
            break
        number += 1

    # This should create the zip file in my documents folder
    os.chdir(r"C:\Users\michael.f.koegel\Documents")

    # create the zip file
    print("Creating {}...".format(zip_filename))
    backup_zip = zipfile.ZipFile(zip_filename, "w")

    for folder_name, sub_folders, file_names in os.walk(folder):
        print("Adding files in {}".format(folder_name))
        # add the current folder to the zip file
        backup_zip.write(folder_name)
        # add all files in this folder to the zip file
        for filename in file_names:
            new_base = os.path.basename(folder)
            if filename.startswith(new_base) and filename.endswith(".zip"):
                continue  # we don't want to backup the backup files
            backup_zip.write(os.path.join(folder_name, filename))
    backup_zip.close()
    print("Done")

backup_to_zip(r"C:\Users\michael.f.koegel\Documents\House")
