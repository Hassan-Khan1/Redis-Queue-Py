from rq import Queue
from redis import Redis
# from somewhere import count_words_at_url
import time
import requests
import json
import random
import urllib.request




def image_download(url):
    # resp = requests.get(url)
    # return len(resp.text.split())
    r = requests.get(url)
    pak_json = r.json()

    



redis_conn = Redis()
q = Queue(connection=redis_conn)  # no args implies the default queue



job = q.enqueue(image_download, 'https://picsum.photos/v2/list')
print("REsult : ",job.result)
# Delay execution of count_words_at_url('http://nvie.com')

# job = q.enqueue('An intro to decoders', 'http://nvie.com')
# print(job)   # => None


# q = Queue('low', connection=redis_conn)
# q.enqueue('An intro to decoders', 'http://nvie.com')
# # Now, wait a while, until the worker is finished
time.sleep(2)
print(q) 


