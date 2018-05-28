import sys
from dict_client import get_ams_dict_client_class
from time import sleep

import redis

DC = get_ams_dict_client_class(redis)
d = DC()
d.set_args_of_ConnectionPool(host="127.0.0.1")
d.set_args_of_StrictRedis()

d.connect()

while True:
    sleep(2)
    print(d.keys(sys.argv[1]))