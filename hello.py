from urllib.request import urlopen
import re

def AskBreakfast():
    breakfast = input("Hello there! What did you have for breakfast today? ")
    if breakfast == "" or breakfast == "Nothing":
        print("Nothing really? How are going to survive this day?")
    else:
        print("You had " + breakfast + " for breakfast? That sounds really awful! You disgust me!")

def AskDinner():
    dinner = input("What did you have for dinner? ")
    if dinner == "" or dinner == "Nothing" and AskBreakfast == "" or AskBreakfast == "Nothing":
        print("Nothing for breakfast and dinner? Are you trying to starve yourself?")
    elif dinner == "" or dinner == "Nothing":
        print("Nothing really? Are you on a diet?")
    else:
        print("You had " + dinner + " for dinner? That sounds terrible. Your food choices are really questionable! You need help!")


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

AskBreakfast()
AskDinner()