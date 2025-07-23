import requests
from datetime import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
# print(data['iss_position'])

parameters = {
    'lat' : 7.2941568,
    'lng' : 80.6354944,
    'time_format' : '24',
}
response = requests.get(url='https://api.sunrisesunset.io/json', params=parameters)
response.raise_for_status()
data = response.json()
sunrise_hr = data['results']['sunrise'].split(':')[0]
sunset_hr = data['results']['sunset'].split(':')[0]
print(data)
print(sunset_hr)

time_now_hr = str(datetime.now().time()).split(':')[0]
print(time_now_hr)