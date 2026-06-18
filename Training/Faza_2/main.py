from fastapi import FastAPI
from pydantic import BaseModel
import json


app = FastAPI()

with open("../Faza_1/workout_plan.json", "r", encoding="utf-8") as f:
        dane = json.load(f)

@app.get("/workout/push")
def get_push():
    return dane["push"]

@app.get("/workout/pull")
def get_pull():
    return dane["pull"]

@app.get("/workout/legs")
def get_legs():
    return dane["legs"]


class Series(BaseModel):
     exercise: str
     series: int
     weight: float
     reps: int
     rir: int
     rep_range_max: int

class Sesion(BaseModel):
     workout_date: str
     workout_type: str
     series: list[Series]

def add_weight(reps, rir, rep_range_max):
    if rir == 0 and reps > rep_range_max:
        return True
    else:
        return False
    
@app.post("/session")
def post_session(sesja: Sesion):
    wyniki = []
    for item in sesja.series:
         wyniki.append(
            {
                "exercise": item.exercise,
                "series": item.series,
                "add_weight": add_weight(item.reps, item.rir, item.rep_range_max)
            })

    return wyniki