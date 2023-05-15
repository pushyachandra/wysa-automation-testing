import csv

def parse_csv(file_path):
    data_dict = {}

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            if len(row) == 3:
                key = row[1]
                values = row[2].split(',')
                data_dict[key] = values

    return data_dict
