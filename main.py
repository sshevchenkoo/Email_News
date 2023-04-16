import requests
from send_email import send_email

topic = "tesla"
api_key = "59ea32cddd1d4d58bfb452d008323d5a"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "from=2023-03-16&sortBy=publishedAt&" \
      "apiKey=59ea32cddd1d4d58bfb452d008323d5a&language=en"
request = requests.get(url)
content = request.json()


body = ""
for article in content["articles"]:
    if article["description"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)