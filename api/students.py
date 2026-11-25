from fastapi import APIRouter, HTTPException

from api.schemas.student import StudentCreate, StudentResponse
from services.student_service import (
    delete_student,
    get_all_students,
    insert_student,
    update_student,
)

router = APIRouter(tags=["students"])


@router.post("/add", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    return insert_student(student.model_dump())


@router.get("/students", response_model=list[StudentResponse])
def list_students():
    return get_all_students()


@router.put("/students/{student_id}", response_model=StudentResponse)
def edit_student(student_id: int, student: StudentCreate):
    updated = update_student(student_id, student.model_dump())
    if updated is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated


@router.delete("/students/{student_id}", status_code=204)
def remove_student(student_id: int):
    if not delete_student(student_id):
        raise HTTPException(status_code=404, detail="Student not found")
