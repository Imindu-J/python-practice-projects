import requests
from datetime import datetime,timedelta
import webbrowser

USERNAME = 'imindu'
TOKEN = 'uhwq29vjowd80238fksc'

today =datetime.now()
date = today.strftime('%Y%m%d')

headers = {
    'X-USER-TOKEN': TOKEN,
}

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
## Created a user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_id = 'graph1'
graph_config = {
    'id': graph_id,
    'name': 'Coding graph',
    'unit': 'commit',
    'type': 'int',
    'color': 'shibafu',
}

def create_graph():
    response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
    print(response.text)

def create_pixel():
    pixel_create_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}'

    qty = input('Enter rate(0-9): ')
    pixel_data = {
        'date': date,
        'quantity': qty
    }

    response = requests.post(url=pixel_create_endpoint, headers=headers, json=pixel_data)
    print(response.text)
    # if response.text['message'] == 'Success':
    #     print('success')
    webbrowser.open(url=f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}.html')


def update_pixel():
    pixel_update_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{date}'

    qty = input('Enter rate(0-9): ')
    pixel_update_data = {
        'quantity': qty
    }

    response = requests.put(url= pixel_update_endpoint, headers=headers, json=pixel_update_data)
    print(response.text)

def delete_pixel():
    days = int(input('How many days ago was the pixel to be deleted added?'))
    del_date = today - timedelta(days=days)
    del_date = del_date.strftime('%Y%m%d')
    pixel_delete_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{del_date}'

    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    print(response)

create_pixel()