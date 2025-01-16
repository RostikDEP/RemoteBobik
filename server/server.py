from fastapi import FastAPI, HTTPException
from typing import Optional
from utils import DB_Processor


db = DB_Processor('database.db')
app = FastAPI()


@app.get("/")
def home():
    return "Rostik do something strange again !"


@app.get("/instructions/send")
async def send_instruction(from_ : Optional[int] = None, to : Optional[int] = None, instruction: Optional[str] = None, request: Optional[str] = ""):
    if from_ and to and instruction:
        db.AddInstruction(from_, to, instruction, request)
        return HTTPException(status_code=200, detail={"From": from_, "To": to, "Instruction": instruction, "Request": request})
    else:
        return HTTPException(status_code=400, detail="Incorrect request")


@app.get("/instructions/request_all")
async def instructions_request_all():
    records = db.GetAllInstructions()
    return records


@app.get("/instructions/request_uncompleted")
async def instructions_request_uncompleted(id_):
    records = db.GetInstructionByUncompleted(id_)
    return records