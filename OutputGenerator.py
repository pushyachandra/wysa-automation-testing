import csv

def generate_output_csv(data_dict, output_file_path):
    with open(output_file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for key, values in data_dict.items():
            writer.writerow([key] + values)
