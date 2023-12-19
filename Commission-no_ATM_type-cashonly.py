import urllib.request
import json

api_url = "https://data.gov.il/api/3/action/datastore_search?resource_id=b9d690de-0a9c-45ef-9ced-3e5957776b26&limit=5"

# Make the request and read the response
with urllib.request.urlopen(api_url) as response:
    data = json.loads(response.read().decode('utf-8'))

# Check the structure of the response
if 'result' in data and 'records' in data['result']:
    # Access the nested 'records' field
    records = data['result']['records']

    # Print the records to understand the structure
    print("All records:")
    print(records)

    # Filter the data based on both 'Commission' and 'ATM_Type'
    filtered_data = [record for record in records if record.get('Commission') == 'לא' and record.get('ATM_Type') == 'משיכת מזומן']

    # Print the filtered data
    print("\nFiltered data:")
    print(filtered_data)

    # Export filtered data to a JSON file
    with open('filtered_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(filtered_data, json_file, ensure_ascii=False, indent=2)
        print("Filtered data exported to 'filtered_data.json'")
else:
    print("Invalid response structure. Check the API documentation.")
