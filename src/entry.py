from dotenv import load_dotenv
load_dotenv() 

import time
from config import EVENT_CONFIG
from vcf import handler


def timed_handler(event, context):
    start = time.time()
    result = handler(event, context)
    end = time.time()
    print(end - start)
    return result

def entry():
    result = timed_handler(EVENT_CONFIG, None)
    print(result)

if __name__ == "__main__":
    entry()
