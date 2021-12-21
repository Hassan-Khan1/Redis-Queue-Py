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
from time import sleep


def initialize__queue(queue_name):



  queue = Queue(queue_name, connection=Redis())
  # scheduler = Scheduler(queue=queue)
  print(queue.started_job_registry)  # Returns StartedJobRegistry
  queue.deferred_job_registry   # Returns DeferredJobRegistry
  queue.finished_job_registry  # Returns FinishedJobRegistry
  queue.failed_job_registry  # Returns FailedJobRegistry
  print(queue.scheduled_job_registry)  # Returns ScheduledJobRegistry

  job = queue.enqueue(Redis1.print_numbers, 'https://picsum.photos/v2/list')

  # job = queue.enqueue_in(timedelta(seconds=10),Redis1.print_numbers, 'https://picsum.photos/v2/list')

  # job1 = queue.enqueue_at(datetime(2021, 12, 21, 11, 48), Redis1.print_numbers, 'https://picsum.photos/v2/list')

  print(job in queue) 
  print('Job enqueued_at: ' , job.enqueued_at)
  registry = ScheduledJobRegistry(queue=queue)
  print(job in registry)  
# job = queue.enqueue_at(datetime(2021, 12, 21, 9, 15),Redis1.print_numbers, 'https://picsum.photos/v2/list')
  # job = queue.enqueue_in(timedelta(seconds=10),Redis1.print_numbers, 'https://picsum.photos/v2/list')
  # print("Job Is Queue : ",job in queue)  # Outputs False as job is not enqueued
  # registry = ScheduledJobRegistry(queue=queue)
  # print(job in registry)

  # job = scheduler.enqueue_in(timedelta(seconds=10),Redis1.print_numbers, 'https://picsum.photos/v2/list')
  
  # scheduler.enqueue_in(timedelta(seconds=10),Redis1.print_numbers, 'https://picsum.photos/v2/list')



  worker = Worker(queue)
  worker.work(burst=True)
  # registry = ScheduledJobRegistry(queue=queue)

  # worker = Worker(queue)
  # worker.work(burst=True,with_scheduler=True)

with Connection():
  initialize__queue('1')

  # initialize__queue('2')
  # initialize__queue('3')
  # initialize__queue('4')
  # initialize__queue('5')
  # initialize__queue('6')
  # initialize__queue('7')
