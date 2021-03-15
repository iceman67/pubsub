import redis
import time
import uuid 
import json

queue = redis.StrictRedis(host='localhost', port=6379, db=0)
channel = queue.pubsub()

for i in range(5): 
    queue.publish("test", i)
    time.sleep(0.5)
id = uuid.uuid1()

mydata = { 'ID': str(id)}
msg = json.dumps(mydata)
queue.publish('register', msg)
queue.publish('__admin__', "shutdown")
