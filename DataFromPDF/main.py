import pdfminer
from pdfminer.high_level import extract_text
import pandas as pd
import os
from get_filepath import *
from OCR_recognition import *




if __name__ == '__main__':
    # hier werden die Pfade eingelesen und in einer Json - Datei gespeichert
    root = 'C:/Users/ChangGeng/Desktop/Projekte/NLP/03 - TextSummary/PDF_Lea' # 'D:\Computer\Benutzer'
    filename_list = get_names(root)
    with open(r'./Dateien/file_names_Lea.txt', 'w') as fp: # Dateien/file_names.txt
        for item in filename_list:
            fp.write("%s\n" % item)
        print('Done with collecting Filepath')

    print("Filename_list completed")


    for item in filename_list:
        try:
            if os.path.isfile(r'./Dateien/file_names_Lea.txt'):
                extract_text_from_pdf(item)
                print("Done with extracting text from PDF")
            else:
                print("Filepath does not exist")
        except (pdfminer.pdfdocument.PDFEncryptionError, pdfminer.pdfdocument.PDFPasswordIncorrect):
            print("Unsupported revision")
            continue
    print("Finish with OCR")


    df = pd.DataFrame({'Path': path_list, 'Text': data_list})
    df.to_json('./Dateien/allFiles_20240122.json', orient='records', lines=True)