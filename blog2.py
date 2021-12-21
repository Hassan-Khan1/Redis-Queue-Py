from redis import Redis
from rq import Connection, Queue, Worker
import blog1  
import sys
from datetime import datetime, timedelta
# similar to rq worker
with Connection():
    qs = sys.argv[1:] or ['default']

    w = Worker(qs)
    w.work()

# edis_connection = Redis(host='localhost', port=6379, db=0)
    q = Queue(connection=Redis())


    # job = q.enqueue(blog1.sum_numbers_from_string, 'adje-fje5-sjfdu1s-gdj9-asd1fg')
# job = queue.enqueue(task1.print_numbers, 'https://picsum.photos/v2/list')

    job = q.enqueue_in(timedelta(seconds=10), blog1.sum_numbers_from_string, 'adje-fje5-sjfdu1s-gdj9-asd1fg')


print("Result : ",job.result)   # => None
job.get_id()
# result.get_id()
# result.get_status()def main():
list_jobs = q.get_jobs
list_jobs()
