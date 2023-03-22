import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "froglufka@gmail.com"
MY_PASSWORD = "learningonestep509"
MY_LAT = 51.519351
MY_LONG = -0.129758 


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]

    iss_latitude = float(data["latitude"])
    iss_longitude = float(data["longitude"])

    #position of the iss  within +5 or -5 degrees of my position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    