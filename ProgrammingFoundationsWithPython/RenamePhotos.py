# rename filenames


import os


def rename_files():
    # Get gilenames
    file_list=os.listdir(r"/Users/avengers/Desktop/Github_Ramsri/HTML_CSS_JavaScript/ProgrammingFoundationsWithPython/prank")
    #print file_list
    saved_path = os.getcwd()
    os.chdir(r"/Users/avengers/Desktop/Github_Ramsri/HTML_CSS_JavaScript/ProgrammingFoundationsWithPython/prank")
    # For each file rename filenames
    for file_name in file_list:
        print file_name
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)        

rename_files()      
