from datetime import datetime, timedelta
import time
from redis import Redis
from rq import Queue
# import tasks
import Redis1 
from rq import Connection, Queue, Worker
import sys
from rq.registry import ScheduledJobRegistry
from rq_scheduler import Scheduler
from rq.job import Job

def initialize__queue(queue_name):
  queue = Queue(queue_name, connection=Redis())
  # scheduler = Scheduler(queue=queue)
  print('Job id: %s')

  job = queue.enqueue(Redis1.print_numbers, 'https://picsum.photos/v2/list',job_id='my_job_id')
  print('Job id: ' , job.id)


  # Can also give predetermined job id 
  # job = queue.enqueue(Redis1.print_numbers, 'https://picsum.photos/v2/list',job_id='my_job_id') 

  redis = Redis()
  job = Job.fetch('my_job_id', connection=redis)
  print('Job get_status: ' , job.get_status())
  print('Job origin: ' , job.origin)
  print('Job func_name: ' , job.func_name)
  print('Job args: ' , job.args)
  print('Job result: ' , job.result)
  print('Job enqueued_at: ' , job.enqueued_at)
  print('Job started_at: ' , job.started_at)
  print('Job ended_at: ' , job.ended_at)
  print('Job worker_name: ' , job.worker_name)


  # registry = ScheduledJobRegistry(queue=queue)
  # print(job in registry) 

  worker = Worker(queue)
  worker.work()

with Connection():
  initialize__queue('1')
  # initialize__queue('2')
  # initialize__queue('3')
  # initialize__queue('4')
  # initialize__queue('5')
  # initialize__queue('6')
  # initialize__queue('7')
