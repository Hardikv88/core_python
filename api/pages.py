from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

from services.student_service import get_all_students

BASE_DIR = Path(__file__).resolve().parent.parent

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@router.get("/")
def students_page(request: Request):
    students = get_all_students()
    return templates.TemplateResponse(
        request, "students.html", {"students": students}
    )
