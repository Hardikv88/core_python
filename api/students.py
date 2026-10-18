from fastapi import APIRouter

from api.schemas.student import StudentCreate, StudentResponse
from services.student_service import insert_student

router = APIRouter(prefix="/students", tags=["students"])


@router.post("", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    return insert_student(student.model_dump())




