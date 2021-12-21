from datetime import datetime, timedelta
import time
import random
import time
import requests
import json

import urllib.request
def print_task(seconds):
    print("Starting task")
    random_num = random.randrange(1, 3, 1)
    # optional print statement to see the numbers 
    # print("the randomly generated number = ", random_num) 
    if random_num == 2:
        raise RuntimeError('Sorry, I failed! Let me try again.')
    else:
        for num in range(seconds):
            print(num, ". Hello World!")
            time.sleep(1)
    print("Task completed")
# def print_task(seconds):
#     print("Starting task")
#     for num in range(seconds):
#         print(num, ". Hello World!")
#         time.sleep(1)
#     print("Task completed")

def print_numbers(url):
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
    # print("Starting num task")
    # for num in range(seconds):
    #     print(num)
    #     time.sleep(1)
    # print("Task to print_numbers completed")