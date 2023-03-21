import random

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from random import choice
from pydantic import  BaseModel
from typing import Union
import faker
import uuid

EDUCATIONNAL_FORM = [
    'EXTRAMUNAL',
    'FULL_TIME',
    'PART_TIME',
    'SHORT_EXTRAMUNAL',
    'SHORT_FULL_TIME',
    'EXTERNAL',
]

faker.Faker.seed(0)
fake = faker.Faker(locale='ru_RU')

fake_up = []
fake_edu_program = []

for _ in range(10):

    fake_up.append(
        {
            'external_id': str(uuid.uuid4()),
            'title': fake.word(),
            'direction': fake.word(),
            'cade_direction': fake.phone_number(),
            'start_year': fake.date(pattern='%Y'),
            'end_year': fake.date(pattern='%Y'),
            'educational_form': random.choice(EDUCATIONNAL_FORM),
            'educational_program': str(uuid.uuid4()),
        }
    )
    fake_edu_program.append(
        {
            'external_id': str(fake.pyint(min_value=100000, max_value=999999)),
            'title': fake.word(),
            'direction': fake.word(),
            'cade_direction': fake.phone_number(),
            'start_year': fake.date(pattern='%Y'),
            'end_year': fake.date(pattern='%Y'),
        }
    )

class Validate(BaseModel):
    title: str
    direction: str
    code_direction: str
    start_year: int
    end_year: int

app = FastAPI()

@app.get('/edu_prog')
def reat_edu_prog(size:int = None):
    return JSONResponse(
        content=jsonable_encoder(fake_edu_program[:size])
    )

@app.get('/up')
def reat_up(size:int = None):
    return JSONResponse(
        content=jsonable_encoder(fake_up[:size])
    )




# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
