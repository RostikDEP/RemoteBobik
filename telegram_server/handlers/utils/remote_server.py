import requests

class RemoteServer:
    def __init__(self, server):
        self.server = server


    def send_instruction(self, from_id, to_id, instruction):
        try:
            response = requests.get(f"{self.server}/instructions/send", params={
                "from_":from_id,
                "to":to_id,
                "instruction":instruction,
                "request":"None"},
            )
        except Exception as e:
            return False
        else:
            return True
