from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel,EmailStr

app=FastAPI()

class Student(BaseModel):
    name:str
    age:int
    email:EmailStr
    course:list[str]

@app.get("/students/{student_id}")
def std_id(student_id : int, iclude_grade: bool , semester: Optional[str] = None):
    try:
        student_id=int(student_id)
        if student_id<1000 or student_id>9999:
            raise Exception("Invalid Student ID")
        
        
        return {"student_id":student_id}                                              
    except Exception as e:
        return {"Error":str(e)} 

@app.post("/students/register")
def register_student(student:Student):
    return student

@app.put("/students/{student_id}/{email}")
def change_mail(student_id:int,email:EmailStr):
    try:
        if student_id <1000 or student_id >9999:
            raise Exception("Invalid Student ID")
        Student.email = email
        return {"student_id":student_id , "email":email, "message":"Email Updated Successfully"}
    except Exception as e:
        return {"Error":str(e)}