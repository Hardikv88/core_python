import json
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()

# from api.routers.students import router as students_router

# app = FastAPI(title="Student API")
# app.include_router(students_router)

app = FastAPI()

STUDENTS_FILE = Path(__file__).resolve().parent / "data" / "students.json"


class StudentRequest(BaseModel):
    id: int
    name: str
    city: str


@app.post("/Student", status_code=201)
def Student_user(payload: StudentRequest):
    with STUDENTS_FILE.open() as file:
        students = json.load(file)

    student = payload.model_dump()
    students.append(student)

    with STUDENTS_FILE.open("w") as file:
        json.dump(students, file, indent=2)
        file.write("\n")

    return student


@app.get("/students")
def get_students():
    with STUDENTS_FILE.open() as file:
        return json.load(file)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)