import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    json_data = []

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            json_data.append(row)

    with open(json_file_path, mode='w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

# Example usage
csv_file_path = './assets/SURP_projects.csv'
json_file_path = 'SURP_projects.json'
csv_to_json(csv_file_path, json_file_path)
