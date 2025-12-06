import requests
import json
import os
import sys
import urllib3
from elasticsearch import Elasticsearch

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

print("Select SIEM platform:")
print("1. Elasticsearch")
print("2. Splunk")
siem_choice = input("Enter your choice (1 or 2): ").strip()

if siem_choice not in ['1', '2']:
    print("Error: Invalid choice. Please enter 1 or 2.")
    exit(1)

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = input("Enter the path to a JSON file or directory containing JSON files: ").strip()

path = path.strip('"').strip("'")

if not os.path.exists(path):
    print(f"Error: Path does not exist: {path}")
    exit(1)

files_to_process = []

if os.path.isfile(path):
    if path.endswith(".json"):
        files_to_process.append(path)
    else:
        print(f"Error: File is not a JSON file: {path}")
        exit(1)
elif os.path.isdir(path):
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            files_to_process.append(os.path.join(path, filename))
else:
    print(f"Error: Invalid path: {path}")
    exit(1)

if not files_to_process:
    print("No JSON files found to process.")
    exit(1)

if siem_choice == '1':
    es_host = input("Enter Elasticsearch host (default: localhost): ").strip() or 'localhost'
    es_port = input("Enter Elasticsearch port (default: 9200): ").strip() or '9200'
    es_user = input("Enter Elasticsearch username (default: elastic): ").strip() or 'elastic'
    es_pass = input("Enter Elasticsearch password: ").strip()
    es_index = input("Enter Elasticsearch index name: ").strip()
    
    if not es_index:
        print("Error: Index name cannot be empty.")
        exit(1)
    
    es = Elasticsearch(
        [{'host': es_host, 'port': int(es_port), 'scheme': 'https'}],
        http_auth=(es_user, es_pass),
        verify_certs=False
    )
    print(f"\nConnected to Elasticsearch at {es_host}:{es_port}")
    
elif siem_choice == '2':
    splunk_host = input("Enter Splunk host (default: localhost): ").strip() or 'localhost'
    splunk_port = input("Enter Splunk HEC port (default: 8088): ").strip() or '8088'
    use_https = input("Use HTTPS? (y/n, default: y): ").strip().lower() or 'y'
    splunk_token = input("Enter Splunk HEC token: ").strip()
    splunk_index = input("Enter Splunk index name (default: apt29): ").strip() or 'apt29'
    
    protocol = 'https' if use_https == 'y' else 'http'
    splunk_url = f"{protocol}://{splunk_host}:{splunk_port}/services/collector/event"
    splunk_headers = {
        'Authorization': f'Splunk {splunk_token}',
        'Content-Type': 'application/json'
    }
    print(f"\nConnected to Splunk at {protocol}://{splunk_host}:{splunk_port}")

i = 1
for file_path in files_to_process:
    filename = os.path.basename(file_path)
    print(f"Processing {filename}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    json_element = json.loads(line)
                    
                    if siem_choice == '1':
                        es.index(index=es_index, id=i, document=json_element)
                    
                    elif siem_choice == '2':
                        splunk_event = {
                            'index': splunk_index,
                            'event': json_element
                        }
                        response = requests.post(
                            splunk_url,
                            headers=splunk_headers,
                            json=splunk_event,
                            verify=False
                        )
                        if response.status_code != 200:
                            print(f"Error sending to Splunk: {response.text}")
                    
                    i += 1
                    
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in {filename}: {e}")
                    
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

print(f"\nSuccessfully imported {i-1} documents to {'Elasticsearch' if siem_choice == '1' else 'Splunk'}.")