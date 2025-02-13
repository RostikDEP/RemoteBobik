import requests

print("""                                                     
 ____  _____ __  __  ___ _____ _____   ____   ___  ____ ___ _  __
|  _ \| ____|  \/  |/ _ |_   _| ____| | __ ) / _ \| __ |_ _| |/ /
| |_) |  _| | |\/| | | | || | |  _|   |  _ \| | | |  _ \| || ' / 
|  _ <| |___| |  | | |_| || | | |___  | |_) | |_| | |_) | || . \ 
|_| \_|_____|_|  |_|\___/ |_| |_____| |____/ \___/|____|___|_|\_\ \n""")


def SendInstruction():
    server = input("Central server IP: ") or "http://127.0.0.1:8000/instructions/send"
    from_id = int(input("From id (default:11): ").strip() or "11")
    to_id = int(input("To id (default:22): ").strip() or "22")
    instruction = input("Instruction (default:TestInstruction): ") or "TestInstruction"
    request= input("Request (default:None): ") or "None"

    try:
        requests.get(server, params={
            "from_" : from_id,
            "to" : to_id,
            "instruction"  : instruction,
            "status" : "New",
            "request" : request
        })
    except Exception as e:
        print(e)


def CheckUncompleted():
    server = input("Central server IP: ") or "http://127.0.0.1:8000/instructions/request_uncompleted"
    from_id = int(input("From id (default:1): ").strip() or "1")

    try:
        result = requests.get(server, params={"id_" : from_id})
        return result.content.decode()
    except Exception as e:
        print(e)


def MakeUncompleted():
    result = CheckUncompleted()
    if len(result) != 0:
        print("I have uncompleted tasks")
    else:
        print("Tasks not exist")



if __name__ == "__main__":
    run = True
    while run:
        cmd = input("Enter command: ")
        if cmd == "send":
            SendInstruction()
        if cmd == "check_uncompleted":
            CheckUncompleted()
        if cmd == "make":
            MakeUncompleted()


        if cmd == "q":
            exit()