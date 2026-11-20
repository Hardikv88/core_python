from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI

from api.students import router as students_router

app = FastAPI(title="Student API")
app.include_router(students_router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
