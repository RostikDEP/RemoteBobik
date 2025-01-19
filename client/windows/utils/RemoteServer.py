import requests

class RemoteServer:
    def __init__(self, server):
        self.server = server


    def RequestUncompleted(self, from_id, server_method="instructions/", action="request_uncompleted/"):
        try:
            result = requests.get(f"{self.server}{server_method}{action}", params={"id_": from_id})
            return list(result.json())
        except Exception as e:
            print(e)