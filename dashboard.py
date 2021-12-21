from flask import Flask
import rq_dashboard
import time
import requests
import json
import random
import urllib.request
from rq import Queue
from redis import Redis

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


# def image_download(url):
#     # resp = requests.get(url)
#     # return len(resp.text.split())


#     r = requests.get(url)
#     pak_json = r.json()

        



# redis_conn = Redis()
# q = Queue(connection=redis_conn)  # no args implies the default queue



# job = q.enqueue(image_download, 'https://picsum.photos/v2/list')
# print("REsult : ",job.result)