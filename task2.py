from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
# import tasks
import task1 
from rq import Connection, Queue, Worker
import sys
import rq
with Connection():
#     qs = Queue('default',connection=Redis())

#     w = Worker(qs)
#     w.work()
    redis = Redis()
    queue = Queue('queue_name')
    # queue1 = Queue('queue_name1')
    # queue2 = Queue('queue_name2')
    # queue3= Queue('queue_name3')
    # queue = Queue('queue_name')
    with Connection():

        worker = Worker([queue], connection=redis, name='foo')

    # [Worker(qs).work(Redis1.print_numbers, 'https://picsum.photos/v2/list') for i in range(10)]

    # w = Worker(queue)
    # w = Worker(queue1)
    # w = Worker(queue2)
    # w = Worker(queue3)

    # w.work()

    # GG = queue.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')
  

        job = queue.enqueue(task1.print_numbers, 'https://picsum.photos/v2/list')

        job1 = queue.enqueue(task1.print_numbers, 'https://picsum.photos/v2/list')
    
    # rq.worker.RoundRobinWorker(job,job1)
    
    # job1 = qs.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')
    # job1 = qs.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')
    # job1 = qs.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')
    # job1 = qs.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')
    # job1 = qs.enqueue( task1.print_numbers, 'https://picsum.photos/v2/list')

    # job2 = queue.enqueue(timedelta(seconds=10), task1.print_numbers, 'https://picsum.photos/v2/list')

    # job3 = queue.enqueue(timedelta(seconds=10), task1.print_numbers, 'https://picsum.photos/v2/list')

    # job4 = queue.enqueue(timedelta(seconds=10), task1.print_numbers, 'https://picsum.photos/v2/list')

    # job5 = queue.enqueue(timedelta(seconds=10), task1.print_numbers, 'https://picsum.photos/v2/list')




# redis = Redis()
# queue = Queue('queue_name')

# Start a worker with a custom name
# print(len(queue))

# # Retrieving jobs
# queued_job_ids = queue.job_ids # Gets a list of job IDs from the queue
# queued_jobs = queue.jobs # Gets a list of enqueued job instances
# job = queue.fetch_job('my_id') # Returns job having ID "my_id"

# # Emptying a queue, this will delete all jobs in this queue
# queue.empty()

# # Deleting a queue
# queue.delete(delete_jobs=True) # Passing in `True` will remove all jobs in the queue
# queue is now unusable. It can be recreated by enqueueing jobs to it.
    # def queue_tasks():
        # queue.enqueue(task1.print_task, 5)
    

        # print(job.result)   # => None

# def main():
#     queue_tasks()
# if __name__ == "__main__":
#     main()

