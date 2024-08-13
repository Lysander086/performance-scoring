from app.config.configuration import Config
import requests
import icalendar
from datetime import datetime, timedelta, date
import pytz
import re
import os
from dotenv import load_dotenv

load_dotenv()  
timezone = pytz.timezone('Asia/Tokyo')

# Function to fetch and parse ICS data
def fetch_ics_data(url):
    cookies = {
        '_ga': 'GA1.1.778671165.1686390277',
        'tt_distid': 'help-65e46f92077e6668a2ba6dc6',
        't': '0CAB80045A64122B313ECEE5862340033197D2CA6AC16E0831A0F124101B2E3D6B3EFE28415E16C0D2DCA309DC3EEDC68254893B95D1AABD200A1E3E7B2F46FDB78295B53C5E7E37A428BDC9831AECBCE6E2C8BF3E6AE70775BB88994DE2493CBF120022F28D256661E173102E93A7DE711F9CAEDB907858339C16F5498F0C3FBF120022F28D2566053F6BD7465799CC4566F2D1A0700160F7D92574D052E33EE4801B98560056DB01D4F1AC4449A92A441259BAE0414AF2',
        '_csrf_token': 'YhA3kUP3r4wQm6b74LwaC5aaLmOyJCobXuu3nZsiwo4-1722514031',
        '_bl_uid': 'Xslq6zjFbm6d1kt167p5nz20zOy0',
        'oai': '908D8E614F34B641B1FF648CF152FF162A2074F669FB219B1257AB544D46A0CBC05C3BDD19FB9626CDDA1BFFB2E5182819AEBC0F685DDD099CDED2469CA67B69A92E854D9199D14FFEDB15A4614EC5BE803545D6772E8691C1F431F82FC474A01922938FB6DD215C3EB2BE8B6A515594CF6BFE7F5316FBEF5D6CDCE8A86ABB0DB128B20B4C79C7F9F622D81559166E973AEEBBC9216487712F82A833E0E4D071',
        '_ga_TM2QKQ5S5Q': 'GS1.1.1722834749.208.0.1722834759.50.0.0',
        'AWSALB': 'yETgIGoLJ2Gw5/Bcer9ak3wRKS9MilKU6/BhPCUTJWfkj8Cg+fox44u3k0MXpfXd/JwcUOjuMpco0cx6+gnCmgOjP81IBonl6CajLPUbKlUEkYv0zVV3EelNtTYKKznlZdHEyf8XdGLheHJRl1OqVHeCtKrghXkGJlshpPT+KtxKidhWzk3J9p7agjGH4Q==',
        'AWSALBCORS': 'yETgIGoLJ2Gw5/Bcer9ak3wRKS9MilKU6/BhPCUTJWfkj8Cg+fox44u3k0MXpfXd/JwcUOjuMpco0cx6+gnCmgOjP81IBonl6CajLPUbKlUEkYv0zVV3EelNtTYKKznlZdHEyf8XdGLheHJRl1OqVHeCtKrghXkGJlshpPT+KtxKidhWzk3J9p7agjGH4Q==',
    }
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en,en-US;q=0.9,ja;q=0.8,zh-CN;q=0.7,zh;q=0.6',
        'dnt': '1',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'service-worker-navigation-preload': 'true',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
    }
    response = requests.get(url, cookies=cookies, headers=headers)
    return response.text


class Event:
    def __init__(self, start, end, title, description):
        self.start: float = start
        self.end: float = end
        self.title: str = title
        self.description: str = description

    def toText(self):
        # Convert timestamps back to datetime with timezone for display
        start_dt = datetime.fromtimestamp(self.start, timezone)
        end_dt = datetime.fromtimestamp(self.end, timezone)

        start_time = start_dt.strftime('%H:%M')
        end_time = end_dt.strftime('%H:%M')
        return f"{start_dt.strftime('%Y/%m/%d')}\n{start_time}-{end_time}\n任務名: {self.title}\n"


def extract_events(ics_data: str, sdt: date = date.today() + timedelta(days=1)) -> list:
    calendar = icalendar.Calendar.from_ical(ics_data)
    events: list = []

    sdt_timestamp = datetime.combine(sdt, datetime.min.time()).timestamp() + 86399  # 23:59:59

    for component in calendar.walk():
        if component.name == "VEVENT":
            start = component.get('DTSTART').dt

            # Convert start to timestamp
            if isinstance(start, datetime):
                start_timestamp = start.timestamp()
            elif isinstance(start, date):
                start_timestamp = datetime.combine(start, datetime.min.time()).timestamp()
            else:
                raise ValueError("Invalid DTSTART value")

            end = component.get('DTEND').dt if component.get('DTEND') else start + timedelta(hours=1) 
            if  isinstance(end, datetime) == False:
                end_timestamp = datetime.combine(end, datetime.max.time()).timestamp()
            else:
                end_timestamp = end.timestamp() 

            title: str = component.get('SUMMARY')
            description: str = component.get('DESCRIPTION', '')

            if start_timestamp <= sdt_timestamp:
                event = Event(start_timestamp, end_timestamp, title, re.sub('http(s)*://(.)+', '', description))
                events.append(event)

    # Sort events by start timestamp
    events.sort(key=lambda event: event.start)

    return events


# URL of the ICS file
url = os.getenv('TICKTICK_SUBSCRIPTION_URL')

# Fetch and process ICS data
ics_data = fetch_ics_data(url)
dt = datetime.now() + timedelta(days=0)
events = extract_events(ics_data, dt)
config = Config()

with open(os.path.join(config.resource_dir, 'output', f'{dt.strftime("%m-%d")}.md'), 'w', encoding='utf-8') as f:
    f.write("Zede's One day\n")
    # Output events
    for event in events:
        f.write(event.toText() )
        f.write("-"*50 + "\n")
