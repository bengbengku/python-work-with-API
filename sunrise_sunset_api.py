import  requests
from datetime import datetime
from dateutil import tz

MY_LAT = 3.595196
MY_LNG = 98.672226

from_zone = tz.tzutc()
to_zone = tz.tzlocal()

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


res = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
res.raise_for_status()
data = res.json()

sunrise = data["results"]["sunrise"].split("T")
sunset = data["results"]["sunset"].split("T")

pilih = input("Ingin tau jadwal SUNSET ATAU SUNRISE. Ketik 'SET' ATAU 'RISE': ").lower()
if pilih == "set":
    sunset_convert = f"{sunset[0]} {sunset[1].split('+')[0]}"
    utc = datetime.strptime(sunset_convert, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    lokal = utc.astimezone(to_zone)
    lokal_separated = f"Sunset Pukul {lokal.hour}:{lokal.minute}:{lokal.second}"
elif pilih == "rise":
    sunrise_convert = f"{sunrise[0]} {sunrise[1].split('+')[0]}"
    utc = datetime.strptime(sunrise_convert, '%Y-%m-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    lokal = utc.astimezone(to_zone)
    lokal_separated = f"Sunrise Pukul {lokal.hour}:{lokal.minute}:{lokal.second}"
else:
    print("Keyword yang anda masukan salah!")

print(lokal_separated)





