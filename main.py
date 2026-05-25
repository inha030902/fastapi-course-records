from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()


class Course(BaseModel):
    course_name: str
    year: str
    semester: str
    grade: str


@app.get("/")
async def welcome():
    return {
        "msg": "FastAPI Course Records Server"
    }


@app.get("/courses")
async def get_courses():
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    return data


@app.post("/courses")
async def add_course(course: Course):
    with open("courses.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    data.append(course.dict())

    with open("courses.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return {
        "msg": "course added successfully"
    }