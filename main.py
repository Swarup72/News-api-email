import requests

from sendemail import send_email

api_key = "7acc5d0af08b40578fc38de9940d621d"
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=7acc5d0af08b40578fc38de9940d621d"

#make request
request = requests.get(url)

#get a dictionary with a data
content = request.json()
body = ""
#access the title and description of the article
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2 * "\n"

# body = body.encode("UTF-8")
send_email(message=body)