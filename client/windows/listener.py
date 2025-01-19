from utils import config
from utils import RemoteServer
import time

class Listener:
    def __init__(self, server_=config.SERVER):
        self.server = server_
        self.RemoteServer = RemoteServer(server_)


    def RunLoop(self):
        while True:
            result = self.RemoteServer.RequestUncompleted(11)
            print( result)
            time.sleep(config.REQUESTS_TIMEOUT)





