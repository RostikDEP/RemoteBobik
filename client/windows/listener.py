from utils import config
from utils import RemoteServer
from utils import Types
import time

#Клас Listener
class Listener:
    def __init__(self, server_=config.SERVER):
        self.server = server_       #Присвоїти полю server значення із конфіга
        self.RemoteServer = RemoteServer(server_)   #створити поле із екземпляром класа RemoteServer для
                                                    #для роботи із віддаленим сервером
    #Цикл обробки
    def RunLoop(self):
        while True:
            results = self.RemoteServer.RequestUncompleted(config.MY_ID)
            for result in results:
                if result[3] in Types.Methods.available and result[4] in Types.Status.available:
                    print(f"{result}+++++")
                else:
                    print(f"{result}----")

            time.sleep(config.REQUESTS_TIMEOUT)


#DEBUG------------
if __name__ == "__main__":
    listener = Listener()
    listener.RunLoop()



