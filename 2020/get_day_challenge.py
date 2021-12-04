import datetime
import requests

today_int = str(datetime.datetime.now().day)
url = "https://adventofcode.com/2020/day/" + today_int  + "/input"
r = requests.get(url)
with open(today_int + "_input.txt", 'wb') as f:
    f.write(r.content)
open(today_int + "_day.py","w+")
