from fastapi import FastAPI
from user_data import get_body_composition_data, get_historical_data, get_segment_data, get_user_info
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    name: str
    age: int
    gender: str
    height: float
    weight: float
    metabolicAge: float

class BodyCompositionData(BaseModel):
    bodyFat: float = None
    globalMuscle: float = None
    bodyMassIndex: float = None
    boneMass: float = None
    visceralFatLevel: float = None
    globalWater: float = None
    dailyCaloryIntake: float = None

class SegmentData(BaseModel):
    segment: str
    fatMass: float = None
    leanBodyMass: float = None

    class Config:
        allow_population_by_field_name = True

class HistoricalData(BaseModel):
    date: str = None
    value: float = None

    class Config:
        allow_population_by_field_name = True

@app.get("/user/{user_id}", response_model=User)
def read_user(user_id: int):
    user_data = get_user_info(user_id)
    return User(**user_data)

@app.get("/user/{user_id}/body-composition", response_model=BodyCompositionData)
def read_body_composition(user_id: int):
    body_composition_data = get_body_composition_data(user_id)
    return BodyCompositionData(**body_composition_data)

@app.get("/user/{user_id}/segment-analysis", response_model=list[SegmentData])
def read_segment_analysis(user_id: int):
    segment_data = get_segment_data(user_id)
    return [SegmentData(**item) for item in segment_data]

@app.get("/user/{user_id}/historical-data/weight", response_model=list[HistoricalData])
async def read_historical_weight_data(user_id: int):
    weight_data = get_historical_data(user_id, "Wk")
    return [HistoricalData(**item) for item in weight_data]

@app.get("/user/{user_id}/historical-data/fat", response_model=list[HistoricalData])
async def read_historical_weight_data(user_id: int):
    fat_data = get_historical_data(user_id, 'FW')
    return [HistoricalData(**item) for item in fat_data]

@app.get("/user/{user_id}/historical-data/muscle", response_model=list[HistoricalData])
async def read_historical_weight_data(user_id: int):
    # Replace this with actual data from your database or API
    muscle_data = get_historical_data(user_id, "mW")
    return [HistoricalData(**item) for item in muscle_data]