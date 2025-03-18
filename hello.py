from urllib.request import urlopen
import re

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