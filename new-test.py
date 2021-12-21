import sys
import time
from rq import Connection, Worker
from redis import Redis
import Redis1 


# job1 = qs.enqueue( Redis1.print_numbers, 'https://picsum.photos/v2/list')


redis = Redis(host='localhost')


def main(qs):
  with Connection(connection=redis):
        # if need_burst_workers():
            [Worker(qs).work(Redis1.print_numbers, 'https://picsum.photos/v2/list') for i in range(10)]
        # else:
        #     time.sleep(2) #in seconds
        #     print("Sorry")
if __name__ == '__main__':
    qs = sys.argv[1:] or ['default']
    main(qs)