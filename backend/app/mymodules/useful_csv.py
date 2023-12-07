import csv

def leggi_dati_da_csv(file_path):
    dati = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            dati.append(row)
    return dati

