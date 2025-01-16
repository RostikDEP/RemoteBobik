import time
import requests
import schedule

import utils.config as config
from client.linux.utils import RemoteServer
import preferences

print("""                                                     
 ____  _____ __  __  ___ _____ _____   ____   ___  ____ ___ _  __
|  _ \| ____|  \/  |/ _ |_   _| ____| | __ ) / _ \| __ |_ _| |/ /
| |_) |  _| | |\/| | | | || | |  _|   |  _ \| | | |  _ \| || ' / 
|  _ <| |___| |  | | |_| || | | |___  | |_) | |_| | |_) | || . \ 
|_| \_|_____|_|  |_|\___/ |_| |_____| |____/ \___/|____|___|_|\_\ \n""")

class ServerListener:
    def __init__(self):
        self.run = True
        self.RemoteServer = RemoteServer(config.SERVER)


    def RunLoop(self, timeout):
        try:
            schedule.every(timeout).seconds.do(self.CheckUncompletedTasks)
            while self.run:
                schedule.run_pending()
                time.sleep(1)
        except:
            pass


    def CheckUncompletedTasks(self):
        result = self.RemoteServer.RequestUncompleted(preferences.MY_ID)
        if len(result) != 0:
            print("I have uncompleted tasks")
            print(result)
        else:
            print("Tasks not exist")


    def SendRequest(self):
        print("Hello")



if __name__ == "__main__":
    serverListener = ServerListener()
    serverListener.RunLoop(config.REQUESTS_TIMEOUT)