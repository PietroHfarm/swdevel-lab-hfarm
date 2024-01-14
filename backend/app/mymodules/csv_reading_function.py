import csv


def csv_reading(file_path):
    """
    Reads data from a CSV file and returns a list of dictionaries.

    Parameters:
        file_path (str): The path to the CSV file to be read.

    Returns:
        list of dict: A list of dictionaries,
        where each dictionary
        represents a row from the CSV.
    """
    dati = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            dati.append(row)
    return dati
