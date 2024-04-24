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
            'client_id': 'your-client-id',
        }
        encodedFormData = '&'.join([f"{key}={value}" for key, value in formData.items()])

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Make the POST request to obtain access token
        response = requests.post('your-url-for-token', data=encodedFormData, headers=headers)
        response.raise_for_status()
        return response.json()['access_token']
    except requests.exceptions.RequestException as e:
        print('Error getting access token:', e)

# Function to fetch users from Keycloak
def fetch_users(access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get('realm-url', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Error fetching users:', e)

# Function to fetch groups from Keycloak
def fetch_groups(access_token):
    try:
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        response = requests.get('realm-url', headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print('Error fetching groups:', e)

# Main function to export users and groups
def export_data():
    try:
        # Fetch access token
        access_token = get_access_token()
        
        # Fetch users and groups
        users = fetch_users(access_token)
        groups = fetch_groups(access_token)

        # Combine users and groups into a single dictionary
        user_data = {
            'users': users,
            'groups': groups
        }

        # Write the data to a JSON file
        with open('keycloak_data.json', 'w') as file:
            json.dump(user_data, file, indent=2)
        
        print('Data exported successfully to keycloak_data.json')
    except Exception as e:
        print('Error exporting data:', e)

# Call the main function to start the export process
export_data()
