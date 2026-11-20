from fastapi import APIRouter

from api.schemas.student import StudentCreate, StudentResponse
from services.student_service import get_all_students, insert_student

router = APIRouter(tags=["students"])


@router.post("/add", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    return insert_student(student.model_dump())


@router.get("/students", response_model=list[StudentResponse])
def list_students():
    return get_all_students()
