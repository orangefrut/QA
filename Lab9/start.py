import os
import time

COMMAND = 'Python -m unittest'
AUTH_COMMAND = COMMAND + ' tests.test_auth'
FIND_COMMAND = COMMAND + ' tests.test_search'
CART_COMMAND = COMMAND + ' tests.test_cart'
ORDER_COMMAND = COMMAND + ' tests.test_order'

start_time = time.time()
os.system(AUTH_COMMAND)
os.system(FIND_COMMAND)
os.system(CART_COMMAND)
os.system(ORDER_COMMAND)
print(time.time() - start_time)