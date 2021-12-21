from rq import Connection, Queue
from redis import Redis
# from count_words import count_words_at_url # added import!
import requests
import requests
import json
import urllib.request
from threading import Thread,currentThread
import time
import random
def count_words_at_url(url):
    r = requests.get(url)

    pak_json = r.json()
    list = [] 
    random_num  = random.randint(0,25)
    pakg_str = json.dumps(pak_json[random_num]['download_url'])
    ss = pakg_str.replace('"','')
    list.insert(0,ss)
    ss = [random.choice('0123456789') for _ in range(1,5)]
    ss2 = "".join(ss)  
    # print(ss2 , time.thread_time())
    Image1  = urllib.request.urlretrieve(list[0],f'Imagee{ss2}.jpg')
    print(ss2, ' : ',list[0])
    return Image1




redis_conn = Redis()
# q = Queue(connection=redis_conn)
q = Queue('low', connection=redis_conn)

job = q.enqueue('count_words_at_url', 'https://picsum.photos/v2/list')
print (" Result : :",job)
