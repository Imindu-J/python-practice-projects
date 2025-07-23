import requests
from datetime import datetime
import smtplib

MY_LAT = 7.2941568 # Your latitude
MY_LONG = 80.6354944 # Your longitude
my_email = 'uijalt02@gmail.com'
password = 'yhuu jjjy ztjk wavs'

#Your position is within +5 or -5 degrees of the ISS position.
def is_overhead(my_lat, my_long):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if my_lat-5 < iss_latitude < my_lat+5 and my_long-5 < iss_longitude < my_long+5:
        return True
    else:
        return False

def is_dark():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LONG,
        'time_format': '24',
    }

    response = requests.get(url='https://api.sunrisesunset.io/json', params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise_hr = int(data["results"]["sunrise"].split(":")[0])
    sunset_hr = int(data["results"]["sunset"].split(":")[0])

    now_hr = datetime.now().hour
    print(now_hr, sunset_hr)
    if sunset_hr < now_hr or now_hr < sunrise_hr:
        return True
    else:
        return False

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_overhead(MY_LAT, MY_LONG) and is_dark():
    print(True)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject:ISS Tracker\n\nThe international Space Station is overhead.'
        )
else:
    print(False)
