from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
# import tasks
from apps1 import print_numbers,print_task

queue = Queue(connection=Redis())

def queue_tasks():
    job = queue.enqueue('print_numbers', 'https://picsum.photos/v2/list')
    # job = q.enqueue('count_words_at_url', 'https://picsum.photos/v2/list')

    # queue.enqueue_in(timedelta(seconds=10), task1.print_numbers, 5)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()