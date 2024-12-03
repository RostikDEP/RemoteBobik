from fastapi import FastAPI
from typing import Optional
app = FastAPI()


@app.get("/")
def home():
    return "Hello world"


@app.get("/send_instruction")
def send_instruction(from_ : Optional[int], to : Optional[int], instruction: Optional[str]):
    if from_ and to and instruction:
        return {"from_" : from_, "to" : to, "instruction" : instruction}
    return "Error"