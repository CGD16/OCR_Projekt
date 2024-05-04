from pdfminer.high_level import extract_text
import pandas as pd


path_list = []
data_list = []
def extract_text_from_pdf(pdf_file_path):
    extracted_text = extract_text(pdf_file_path)
    # data.append({'path': pdf_file_path, 'Text': extracted_text})
    path_list.append(pdf_file_path)
    data_list.append(extracted_text)
    print(extracted_text)
    print(f"Done with extracting text from PDF for {pdf_file_path}")





'''
alt

def extract_text_from_pdf():

    data = []
    for line in open(r'./Dateien/file_names.txt'):
        line = line.strip()
        extracted_text = extract_text(line)
        data.append({'path': line, 'Text': extracted_text})
        print(extract_text(line))

    df = pd.DataFrame(data)
    df.to_json(r'./Dateien/allFiles.json', orient='records', lines=True)

'''
