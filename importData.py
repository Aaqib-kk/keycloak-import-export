import requests
import json

# Function to fetch access token
def get_access_token():
    try:
        # Data to be sent in the request
        formData = {
            'grant_type': 'password',
            'username': 'your-username',
            'password': 'your-password',
            'client_id': 'your-client-id'
        }
        encodedFormData = '&'.join([f"{key}={value}" for key, value in formData.items()])

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Make the POST request to obtain access token
        response = requests.post('url-token', data=encodedFormData, headers=headers)
        response.raise_for_status()
        return response.json()['access_token']
    except requests.exceptions.RequestException as e:
        print('Error getting access token:', e)

# Function to read JSON data from file
def read_json_file(filePath):
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print('Error reading JSON file:', e)

# Function to import users into Keycloak
def import_users(access_token, users):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        for user in users:
            # Make POST request to create user
            response = requests.post('realm-url', json=user, headers=headers)
            response.raise_for_status()
        print('Users imported successfully')
    except requests.exceptions.RequestException as e:
        print('Error importing users:', e)

# Function to import groups into Keycloak
def import_groups(access_token, groups):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        for group in groups:
            # Make POST request to create group
            response = requests.post('realm-url', json=group, headers=headers)
            response.raise_for_status()
        print('Groups imported successfully')
    except requests.exceptions.RequestException as e:
        print('Error importing groups:', e)

# Main function to import data
def import_data():
    try:
        # Fetch access token
        access_token = get_access_token()
        
        # Read exported data from file
        exported_data = read_json_file('keycloak_data.json')
        
        # Import users and groups
        import_users(access_token, exported_data['users'])
        import_groups(access_token, exported_data['groups'])

        print('Data imported successfully into Keycloak')
    except Exception as e:
        print('Error importing data:', e)

# Call the main function to start the import process
import_data()
