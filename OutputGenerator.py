import csv

def generate_output_csv(filename, test_results):
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Test Result'])
        writer.writerows(test_results)
    