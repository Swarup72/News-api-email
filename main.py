import requests
api_key = "26a7996118684f208701efe32e5ea1f3"
url ="https://newsapi.org/v2/everything?q=tesla&from=2025-07-04&sortBy=publishedAt&apiKey=26a7996118684f208701efe32e5ea1f3"

#make request
request = requests.get(url)

#get a dictionary with a data
content = request.json()

#access the title and description of the article
for article in content['articles']:
    print(article['title'])