import sys
from rq import Connection, Worker
from redis import Redis
from rq import Queue
# Preload libraries
# import library_that_you_want_preloaded

redis = Redis()

# Count the number of workers in this Redis connection
workers = Worker.count(connection=redis)

# Count the number of workers for a specific queue
queue = Queue('queue_name', connection=redis)
workers = Worker.all(queue=queue)
