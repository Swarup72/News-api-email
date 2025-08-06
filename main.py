import requests

from sendemail import send_email
topic = "tesla"
api_key = "7acc5d0af08b40578fc38de9940d621d"
url = "https://newsapi.org/v2/everything?"\
f"q={topic}"\
"&from=2025-07-06&sortBy=publishedAt" \
"&apiKey=7acc5d0af08b40578fc38de9940d621d"\
"&language=en"

#make request
request = requests.get(url)

#get a dictionary with a data
content = request.json()
body = ""
#access the title and description of the article
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + str(article["description"]) +"\n" \
               +article["url"] + 2 * "\n"

# body = body.encode("UTF-8")
send_email(message=body)