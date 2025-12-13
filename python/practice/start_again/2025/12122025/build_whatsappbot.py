#   https://www.geeksforgeeks.org/python/building-whatsapp-bot-on-python/

from flask import Flask
from googlesearch import search
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
@app.route("/", methods=["POST"])
def bot():
    user_msg = requests.values.get('Body', '').lower()
    response = MessagingResponse()
    q = user_msg + "hello"
    result = []
    for i in search(q, num_results=3):
        result.append(i)
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for result in search_results:
        msg = response.message(result)
    return str(response)
if __name__ == "__main__":
    app.run()