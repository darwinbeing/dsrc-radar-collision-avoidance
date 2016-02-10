from threading import Thread
import time
import logging

class DsrcDataParser(Thread):
    def __init__(self, callback=None, log=True):
        Thread.__init__(self)
        self.callback = callback
        self.log = log

    def run(self):
        import random
        time.sleep(random.random()*2)
        while True:
            data = [random.randint(0,100)]
            if self.log:
                logging.debug(data)

            self.callback(self, data)
            time.sleep(random.random()*2)
