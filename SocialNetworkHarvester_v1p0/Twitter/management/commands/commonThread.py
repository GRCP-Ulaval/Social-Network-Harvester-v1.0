from .client import *
from SocialNetworkHarvester_v1p0.settings import LOG_DIRECTORY, DEBUG
import os

class CommonThread(threading.Thread):

    #@twitterLogger.debug()
    def __init__(self, threadName):
        super().__init__()
        self.name = threadName

    @twitterLogger.debug()
    def run(self):
        try:
            self.execute()
            log('%s has finished successfully'%threading.current_thread().name)
        except Exception as e:
            exceptionQueueLock.acquire()
            exceptionQueue.put((e, self.name))
            exceptionQueueLock.release()