from urllib.request import urlopen
import re
from datetime import datetime
import pytz

def display_time_with_timezone(timezone):
    """Display the current time in the specified timezone."""
    try:
        tz = pytz.timezone(timezone)
        now = datetime.now(tz)
        print(f"The current time in {timezone} is: {now.strftime('%H:%M:%S')}")
    except Exception as e:
        print(f"Invalid timezone: {timezone}. Error: {e}")

print('Hello, world!')

url="https://www.timeanddate.de/"
page=urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

pattern='<span id="clk_hm">.*?</span>'
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title)

pattern_2='<span id="ij0">.*?</span>'
match_results_2 = re.search(pattern_2, html, re.IGNORECASE)
title_2 = match_results_2.group()
title_2 = re.sub("<.*?>", "", title_2)
print("The current time is: " + title + ":" + title_2 )

# Ask the user for a timezone
timezone = input("Enter a timezone (e.g., 'Europe/Berlin', 'America/New_York'): ")
display_time_with_timezone(timezone)