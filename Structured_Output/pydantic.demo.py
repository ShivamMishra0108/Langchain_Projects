from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'shivam'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)

new_student = {'name':'shivam','age':32,'email':'abc@gmail.com','cgpa':6}

student = Student(**new_student)

student_dict = dict(student)


print(student_dict['email'])
