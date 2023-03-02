
#This small project was made to change the name of a file to include its contents in the name

#How to operate:
#               Step 1.) In gFile copy and paste in the filepath of the text file DateSaved.txt.
#               Step 2.) In DateSaved.txt you will see a date already inside feel free to change this, its in the format year-month-date.
#               Step 3.) Make sure to save any changes to the .txt file.  
#               Step 4.) Run this code.
#               Step 5.) You will be prompted to type in the loctaion for the text file, paste in the filepath.
#               Step 6.) A  sucess message should pop up and you will be able to see the updated file name in File Explorer (It should now look like DateSaved-'date you entered inot the file').
#               Step 7.) If you get an error check your filepath and try again. 
#               Step 8.) If you want to change the name from the already changed name, make sure you change the gFile and the file name in the prompt to the name you previously chose.                


import pathlib
import os
from datetime import datetime

###Replace the underline with the file path of where you put the two files 
gFile=r'_______________________________________'
gFileHandle = ''

def get_correct_filename(pFile):
    # Use the pathlib.Path.stem method to get the filename without the extension
    return pathlib.Path(pFile).stem

def get_correct_fileext(pFile):
    # Use the pathlib.Path.suffix method to get the file extension
    return pathlib.Path(pFile).suffix

def get_correct_filepath(pFile):
    # Use the pathlib.Path.parent method to get the filepath without the filename
    return str(pathlib.Path(pFile).parent) + '\\'

def does_file_exist(pFileAndPath):
    return pathlib.Path(pFileAndPath).is_file

def locate_file(): 
    gFile = input('Please enter the file and path: ')
    return does_file_exist(gFile)

def check_is_a_date(pDate):
    try:
        date = datetime.strptime(pDate, '%Y%m%d')
        return True
    except ValueError:
        return False

def file_open_and_read():
    gFileHandle = open(gFile, 'r')
    vDate = gFileHandle.readline()
    gFileHandle.close()
    if check_is_a_date(vDate):
        return vDate, True
    else:
        return vDate, False

def rename_file(pFileRenameFrom, pFileRenameTo): 
    try: 
        os.rename(pFileRenameFrom, pFileRenameTo)
        return True
    except:
        return False

def main():
    if not locate_file():
        print('Error - File does not exist')
        exit()    
    vDate, vValid = file_open_and_read()
    if not vValid:
        print('Error - Date in file is not a date: ' + vDate)
        exit()
    vNewFilename = get_correct_filepath(gFile) + get_correct_filename(gFile) + '-' + vDate + get_correct_fileext(gFile)
    if rename_file(gFile, vNewFilename):
        print('')
        print(f'Success: File [{gFile}] renamed to be [{vNewFilename}]')
        print('')
    else:
        print('')
        print(f'Error: File [{gFile}] cannot be renamed to be [{vNewFilename}]')
        print('')
if __name__ == "__main__":
    main()

