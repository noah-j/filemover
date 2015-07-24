__author__ = 'Noah'

from shutil import move
from os import listdir,mkdir
from datetime import datetime

"""File_Mover is a collection of functions to move files based on extensions.
Tired of cutting and pasting? Do you like taking risks?
The functions contained herein move large batches of files in a dangerous and
relatively error prone manor using only command line prompts!

directory_query(): Use to initialize File_Mover functionality

file_mover(criteria, src, dest): moves files based on directory_query() inputs

stamped_folder_maker(dest_dir): creates a folder based on current timestamp

char_replace(date_stamp, chars): converts all non-numeric figures to '_'
"""

def directory_query():
    #I would like to add additional file selection criteria at some point
    print 'Please enter the file type you wish to move including the \'.\''
    file_type = raw_input('> ')

    print 'Please enter the full path to your files'
    source_path = raw_input('> ')

    print 'Please enter the full destination path'
    dest_path = raw_input('> ')

    print 'Would you like to create a new subfolder for your files? Y/N'
    new_folder_query = raw_input('> ')

    nfq_answer = new_folder_query

    if nfq_answer == 'Y' or nfq_answer == 'y' :
        print 'Would you like to use a timestamp as the folder name? Y/N'
        timestamp_query = raw_input('> ')
        if timestamp_query == 'Y' or timestamp_query == 'y' :
            file_mover(file_type,source_path,stamped_folder_maker(dest_path))
        else:
            print 'Please enter desired folder name'
            specific_name = raw_input('> ')
            named_folder = '{0}\{1}'.format(dest_path,specific_name)
            mkdir(named_folder)
            file_mover(file_type,source_path,named_folder)
    else:
        file_mover(file_type,source_path,dest_path)

def file_mover(criteria,src,dest):

    moved_items = []

    dir_contents = listdir(src)
    for item in dir_contents:
        item_name = item
        item = '{0}\{1}'.format(src,item)
        if item.lower().endswith(criteria):
            move(item,dest)
            moved_items.append('{0}'.format(item_name))
    print moved_items
    print 'Have been moved to folder: {0}'.format(dest)



def stamped_folder_maker(dest_dir):
    time_stamp = datetime.now()
    replace_these = ['-', ' ', '.', ':','/']
    str_time_stamp = time_stamp.strftime('%c')

    folder_name = char_replace(str_time_stamp,replace_these)
    stamped_folder_path = '{0}\{1}'.format(dest_dir,folder_name)
    mkdir(stamped_folder_path)
    return stamped_folder_path

def char_replace(date_stamp,chars):
    name = date_stamp
    for spot in date_stamp:
        if spot in chars:
            name = name.replace(spot,'_')
    return name