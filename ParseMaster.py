import csv

def parse_csv(file_path):
    data_dict = {}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if len(row) == 2:
                key = row[0]
                values = row[1].split(',')
                data_dict[key] = values

    return data_dict
