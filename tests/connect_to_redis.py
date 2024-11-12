from db.redis_client import get_redis_connection
import time

r = get_redis_connection()

r.set("temp", "Value", 2)
res = r.get("temp")
print(res) # should print "Value"

time.sleep(2)

res = r.get("temp")
print(res) # should print "None"