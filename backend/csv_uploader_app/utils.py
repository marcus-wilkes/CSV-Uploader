import io
import csv
from .models import CsvData


def validate_file(uploaded_file):
    if not uploaded_file:
        return 'No file inputted', 400
    if uploaded_file.content_type != 'text/csv':
        return 'Only CSV files are allowed', 400
    if uploaded_file.size == 0:
        return 'Uploaded file is empty', 400

    return None, None


def map_location_to_state(city):
    state_map = {
        'Boston': 'MA',
        'Palo Alto': 'CA',
        'New York': 'NY',
    }
    return state_map.get(city, 'Unknown')


def process_csv_data(uploaded_file):
    decoded_file = io.StringIO(uploaded_file.read().decode('utf-8'))
    reader = csv.DictReader(decoded_file)
    mapping = {'First Name': 'first_name', 'Last Name': 'last_name',
               'Class 1': 'class_name', 'Class 2': 'class_name',
               'School': 'school', 'Location': 'state'}
    objects_to_create = []
    for row in reader:
        name = f"{row.get('First Name', '').strip()} {row.get('Last Name', '').strip()}"
        mapped_data = {'name': name, 'class_name': row.get('Class 1', ''),
                       'school': row.get('School', ''), 'state': row.get('Location', '')}
        objects_to_create.append(CsvData(**mapped_data))
    return objects_to_create
