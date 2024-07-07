import requests

def generate_token():
    url = 'https://www.arcgis.com/sharing/rest/generateToken'
    params = {
        'f': 'json',
        'username': 'j.pagan_MrMap',
        'password': 'Chu20jesu_',
        'referer': 'https://www.arcgis.com',
        'expiration': 60  # Token expiration in minutes
    }
    response = requests.post(url, data=params)
    response_json = response.json()
    print("Response JSON:", response_json)
    token = response_json.get('token')
    return token

def update_index_html(token):
    with open('index.html', 'r') as file:
        file_data = file.read()

    # Replace the old token with the new one
    new_data = file_data.replace('var token = "mzFcMRqhxzPAoRJavp2MJngNzOXMGXKTE25GDqcLccy1J9Tug2tlhMAuP5DjVA6SxMtaua7pdPlDWlTVrJBj7CgwsZ56wrxdT4IhVjHPfIkGBn6uF40bpvMYLRiFtcZmBEuCEt-3DpvveQZAk_OkfaQQkUGeMr-GwveJo4HsLIaJ3Ros2rzIEf_LWHsV9HZn";', f'var token = "{token}";')

    with open('index.html', 'w') as file:
        file.write(new_data)

if __name__ == "__main__":
    new_token = generate_token()
    print("New token:", new_token)
    if new_token:
        update_index_html(new_token)
    else:
        print("Failed to generate a new token.")
