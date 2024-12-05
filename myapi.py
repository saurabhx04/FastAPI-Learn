from fastapi import FastAPI, Path
from typing import Optional

app = FastAPI()

student = {
    1: {"name": "John", "age": 20, "grade": "A"},
    2: {"name": "Jane", "age": 21, "grade": "B"},
}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/student/{student_id}")
async def get_student(student_id: int = Path(description="The ID of the student", gt=0, lt=3)):
    return student[student_id]


@app.get("/get-by-name")
async def get_student_by_name(name: Optional[str] = None):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]

    return {"data": "Not Found"}