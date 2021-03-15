import redis
import time
import threading

class Listener(threading.Thread):
    def __init__(self, r, p):
        threading.Thread.__init__(self)
        self.redis = r
        self.pubsub = self.redis.pubsub()
        self.pubsub.psubscribe(p)

    def run(self):
        for m in self.pubsub.listen():
            if 'pmessage' != m['type']:
                continue
            if '__admin__' == m['channel'].decode("utf-8")  and 'shutdown' == m['data'].decode("utf-8"):
                print ('Listener shutting down, bye bye.')
                break
            print ('[{}]: {}'.format(m['channel'].decode("utf-8") , m['data'].decode("utf-8") ))

            # channel + data
            if 'register' == m['channel'].decode("utf-8"):
                print ('Register :', m['data'].decode("utf-8")) 
              

if __name__ == "__main__":
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    #r = redis.StrictRedis()
    client = Listener(r, '*')
    client.start() 


